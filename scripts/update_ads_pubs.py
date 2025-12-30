#!/usr/bin/env python3
# RUN IN TERMINAL AS:
# $./scripts/update_ads_pubs.py
# $./scripts/update_ads_pubs.py "JIV" --metrics --metrics-only
# $./scripts/update_ads_pubs.py --delta-year 2025 --metrics-only
# $./scripts/update_ads_pubs.py "JIV" _data/papers_all.yml --sdss _data/papers_sdssv.yml --metrics _data/ads_metrics.yml
#
import os, sys, re, time, json, math, unicodedata, html, argparse
from typing import List, Dict
import requests, yaml

ADS_API = "https://api.adsabs.harvard.edu/v1"
TOKEN = os.getenv("ADS_DEV_KEY")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
DEFAULT_LIBRARY_NAME = "JIV"
DEFAULT_ALL_YML = "_data/papers_all.yml"
DEFAULT_SDSS_YML = "_data/papers_sdssv.yml"
DEFAULT_METRICS_YML = "_data/ads_metrics.yml"

# Map BibTeX month tokens to two-digit numbers
BIB_MONTHS = {
    "jan":"01","feb":"02","mar":"03","apr":"04","may":"05","jun":"06",
    "jul":"07","aug":"08","sep":"09","oct":"10","nov":"11","dec":"12"
}


# ---- helpers ----

def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr); sys.exit(1)

def norm(s: str) -> str:
    """lowercase, strip accents & extra spaces for robust matching"""
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()

def clean_title(title: str) -> str:
    """Strip ADS-provided HTML tags/entities and normalize whitespace."""
    if not title:
        return ""
    title = html.unescape(title)
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title

def find_library_id(library_name: str) -> str:
    r = requests.get(f"{ADS_API}/biblib/libraries?rows=2000", headers=HEADERS)
    r.raise_for_status()
    libs = r.json().get("libraries", [])
    for lib in libs:
        if lib.get("name") == library_name:
            return lib.get("id")
    names = ", ".join(l.get("name") for l in libs)
    die(f'Library "{library_name}" not found. Available: {names}')

def get_bibcodes_for_library(library_id: str) -> list[str]:
    base = f"{ADS_API}/biblib/libraries/{library_id}"
    headers = {**HEADERS, "Accept": "application/json"}
    for url in (base, base + "/"):
        r = requests.get(url, headers=headers, params={"rows": 2000})
        if r.status_code == 200:
            data = r.json() or {}
            docs = data.get("documents") or data.get("docs") or []
            # docs may be a list of bibcodes or objects; normalize to bibcodes
            if docs and isinstance(docs[0], dict):
                return [d.get("bibcode") for d in docs if d.get("bibcode")]
            return docs
        elif r.status_code == 404:
            continue  # try the alternate URL form
        else:
            raise SystemExit(f"{r.status_code} {r.reason} for {url}\nResponse: {r.text[:500]}")
    raise SystemExit(f"Library {library_id} not found at {base} (tried with and without trailing slash).")

def chunked(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

def coerce_int(val) -> int:
    try:
        return int(val)
    except Exception:
        return 0

def norm_key(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def pick_section(data: Dict, *needles: str) -> Dict:
    for key, value in (data or {}).items():
        key_lc = key.lower()
        if any(n in key_lc for n in needles):
            return value or {}
    return {}

def pick_metric_value(section: Dict, keys: List[str]) -> int:
    if not section:
        return 0
    key_norms = [norm_key(k) for k in keys]
    for k, v in section.items():
        if norm_key(k) in key_norms:
            return coerce_int(v)
    for k, v in section.items():
        nk = norm_key(k)
        if any(needle in nk for needle in key_norms):
            return coerce_int(v)
    return 0

def pick_histogram(histograms: Dict, names: List[str]) -> Dict:
    if not histograms:
        return {}
    for name in names:
        if name in histograms:
            return histograms[name] or {}
    for k, v in histograms.items():
        k_lc = k.lower()
        if any(name in k_lc for name in names):
            return v or {}
    return {}

def pick_hist_values(block: Dict) -> List:
    if not block:
        return []
    for k, v in block.items():
        if k in ("year", "years"):
            continue
        if isinstance(v, list):
            return v
    return []

def histogram_series(histograms: Dict, names: List[str]) -> List[Dict]:
    block = pick_histogram(histograms, names)
    if not block:
        return []

    # Format A: arrays of years + counts
    years = block.get("year") or block.get("years") or []
    values = block.get("count") or pick_hist_values(block)
    if years and values:
        return [{"year": coerce_int(y), "value": coerce_int(v)} for y, v in zip(years, values)]

    # Format B: dict of labels -> dict(year -> value)
    if isinstance(block, dict):
        preferred = None
        for key in ("all publications", "all citations", "all reads", "all downloads"):
            if key in block:
                preferred = block[key]
                break
        if preferred is None:
            for value in block.values():
                if isinstance(value, dict):
                    preferred = value
                    break
        if isinstance(preferred, dict):
            series = [{"year": coerce_int(y), "value": coerce_int(v)} for y, v in preferred.items()]
            return sorted(series, key=lambda x: x["year"])

    return []

def time_series_indices(time_series: Dict) -> List[Dict]:
    if not time_series:
        return []
    years = set()
    for key in ("h", "g", "i10", "read10"):
        years.update((time_series.get(key) or {}).keys())
    series = []
    for year in sorted(coerce_int(y) for y in years):
        series.append({
            "year": year,
            "h_index": coerce_int((time_series.get("h") or {}).get(str(year), 0)),
            "g_index": coerce_int((time_series.get("g") or {}).get(str(year), 0)),
            "i10_index": coerce_int((time_series.get("i10") or {}).get(str(year), 0)),
            "read10_index": coerce_int((time_series.get("read10") or {}).get(str(year), 0)),
        })
    return series

def build_citations_series(histograms: Dict) -> List[Dict]:
    block = pick_histogram(histograms, ["citations"])
    if not isinstance(block, dict):
        return []
    current_year = int(time.strftime("%Y"))
    combined = {}
    for label, series in block.items():
        if "normalized" in label.lower():
            continue
        if not isinstance(series, dict):
            continue
        for year, val in series.items():
            y = coerce_int(year)
            if y > current_year:
                continue
            combined[y] = combined.get(y, 0) + coerce_int(val)
    if not combined:
        return []
    return sorted(
        [{"year": coerce_int(y), "value": coerce_int(v)} for y, v in combined.items()],
        key=lambda x: x["year"],
    )

def year_value(series: List[Dict], year: int, key: str = "value") -> int:
    for item in series or []:
        if coerce_int(item.get("year")) == year:
            return coerce_int(item.get(key))
    return 0

def year_delta(series: List[Dict], year_from: int, year_to: int, key: str = "value") -> int:
    return year_value(series, year_to, key=key) - year_value(series, year_from, key=key)

def trim_leading_zeros(series: List[Dict]) -> List[Dict]:
    for i, item in enumerate(series or []):
        if coerce_int(item.get("value")) != 0:
            return series[i:]
    return series or []

def latest_year_from_series(*series_list: List[Dict]) -> int:
    current_year = int(time.strftime("%Y"))
    years = []
    for series in series_list:
        for item in series or []:
            year = item.get("year")
            if year is None:
                continue
            y = coerce_int(year)
            if y <= current_year:
                years.append(y)
    return max(years) if years else current_year

def read_existing_delta_year(path: str) -> int:
    if not path or not os.path.exists(path):
        return 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return 0
    val = data.get("delta_year")
    if not val:
        val = (data.get("metrics") or {}).get("delta_year")
    return coerce_int(val)

def fetch_metrics(bibcodes: List[str]) -> Dict:
    if not bibcodes:
        return {}
    headers = {**HEADERS, "Content-Type": "application/json"}
    payload = {"bibcodes": bibcodes}
    last_err = None
    for attempt in range(3):
        try:
            r = requests.post(f"{ADS_API}/metrics", headers=headers, json=payload, timeout=60)
            r.raise_for_status()
            return r.json() or {}
        except requests.exceptions.RequestException as exc:
            last_err = exc
            time.sleep(2 * (attempt + 1))
    raise SystemExit(f"ADS metrics request failed after retries: {last_err}")

def build_metrics_payload(metrics_raw: Dict, mapped: List[Dict], delta_year: int = 0) -> Dict:
    basic = pick_section(metrics_raw, "basic")
    citation = pick_section(metrics_raw, "citation")
    reads = pick_section(metrics_raw, "read")
    indicators = metrics_raw.get("indicators") or pick_section(metrics_raw, "indicators")
    time_series = metrics_raw.get("time series") or pick_section(metrics_raw, "time series")
    histograms = metrics_raw.get("histograms") or pick_section(metrics_raw, "histogram")

    papers_series = histogram_series(histograms, ["publications", "papers", "pubs"])
    if not papers_series:
        counts = {}
        for m in mapped:
            year = m.get("year")
            if year and str(year).isdigit():
                counts[int(year)] = counts.get(int(year), 0) + 1
        papers_series = [{"year": y, "value": counts[y]} for y in sorted(counts.keys())]

    citations_series = build_citations_series(histograms)
    reads_series = trim_leading_zeros(histogram_series(histograms, ["reads", "read"]))
    indices_series = time_series_indices(time_series)

    total_papers = pick_metric_value(basic, ["number of papers", "papers", "publications", "pubs"])
    if total_papers == 0:
        total_papers = len(mapped)

    total_citations = pick_metric_value(citation, ["total number of citations", "citations", "total citations", "citations total"])
    if total_citations == 0:
        total_citations = sum(coerce_int(m.get("citations")) for m in mapped)

    h_index = pick_metric_value(indicators, ["h", "h-index", "h_index", "hindex"])
    if h_index == 0:
        h_index = pick_metric_value(basic, ["h-index", "h_index", "hindex"])

    g_index = pick_metric_value(indicators, ["g", "g-index", "g_index", "gindex"])
    if g_index == 0:
        g_index = pick_metric_value(basic, ["g-index", "g_index", "gindex"])

    if delta_year:
        latest_year = delta_year
    else:
        latest_year = latest_year_from_series(papers_series, citations_series, indices_series)
    prev_year = latest_year - 1

    metrics = {
        "total_papers": total_papers,
        "total_citations": total_citations,
        "h_index": h_index,
        "g_index": g_index,
        "deltas": {
            "total_papers": year_value(papers_series, latest_year),
            "total_citations": year_value(citations_series, latest_year),
            "h_index": year_delta(indices_series, prev_year, latest_year, key="h_index"),
            "g_index": year_delta(indices_series, prev_year, latest_year, key="g_index"),
        },
    }

    return {
        "as_of": time.strftime("%Y-%m-%d"),
        "delta_year": latest_year,
        "metrics": metrics,
        "plots": {
            "papers_per_year": papers_series,
            "citations_per_year": citations_series,
            "reads_per_year": reads_series,
            "indices_per_year": indices_series,
        },
    }

def fetch_bibtex_months(bibcodes: List[str]) -> Dict[str, Dict[str, str]]:
    """
    Query ADS /export/bibtex for many bibcodes at once and extract BibTeX month.
    Returns { bibcode: {"token": "jun", "num": "06"} } for those that have it.
    """
    if not bibcodes:
        return {}
    out: Dict[str, Dict[str,str]] = {}
    headers = {**HEADERS, "Content-Type": "application/json"}

    for chunk in chunked(bibcodes, 100):
        r = requests.post(f"{ADS_API}/export/bibtex", headers=headers, json={"bibcode": chunk}, timeout=30)
        r.raise_for_status()
        text = (r.json() or {}).get("export", "")

        # Split concatenated bibtex entries; key is the bibcode after @TYPE{
        for m in re.finditer(r'@[\w\-]+\{([^,]+),(.*?)\n\}\s*', text, flags=re.S):
            code = m.group(1).strip()
            body = m.group(2)
            mm = re.search(r'(?mi)^\s*month\s*=\s*[{\"]?([A-Za-z]{3})', body)
            if mm:
                token = mm.group(1).lower()
                num = BIB_MONTHS.get(token)
                if num:
                    out[code] = {"token": token, "num": num}
    return out

def derive_sortdate_from_fields(pub: str, year: str, arxiv_id: str, refereed: bool,
                                bibcode: str) -> tuple[str, str, str]:
    """
    Returns (sortdate, month_token, month_num).
      - Refereed journals: use BibTeX month -> YYYY-MM-15
      - arXiv e-prints: YYMM from arXiv id -> 20YY-MM-31
      - Fallbacks: refereed -> YYYY-06-30, else YYYY-01-01
    """
    # 1) refereed journal month from BibTeX
    if refereed and pub and pub != "arXiv e-prints":
        mm = BIBTEX_MONTH_BY_BIBCODE.get(bibcode) or {}
        mnum = mm.get("num")
        if year and mnum:
            return f"{year}-{mnum}-15", mm.get("token",""), mnum

    # 2) arXiv month from arXiv ID (YYMM.xxxxx)
    if pub == "arXiv e-prints" and arxiv_id and len(arxiv_id) >= 4 and arxiv_id[:4].isdigit():
        yy = arxiv_id[:2]; mnum = arxiv_id[2:4]
        return f"20{yy}-{mnum}-31", "", mnum

    # 3) fallbacks
    if year:
        if refereed:
            return f"{year}-06-30", "jun", "06"
        else:
            return f"{year}-01-01", "jan", "01"

    return "", "", ""

def fetch_metadata_for_bibcodes(bibcodes: List[str]) -> List[Dict]:
    """Use /search/query in chunks to pull fields we need."""
    fields = [
        "bibcode", "title", "author", "year", "pub", "volume", "page",
        "page_range", "doi", "identifier", "citation_count", "pubdate",
        "property"
    ]
    out = []
    for chunk in chunked(bibcodes, 50):
        q = ' OR '.join([f'bibcode:"{b}"' for b in chunk])
        params = {"q": q, "fl": ",".join(fields), "rows": 200}
        r = requests.get(f"{ADS_API}/search/query", headers=HEADERS, params=params)
        r.raise_for_status()
        docs = r.json().get("response", {}).get("docs", [])
        out.extend(docs)
        time.sleep(0.1)  # be gentle
    return out

def extract_arxiv(identifier_list: list, doi: str = "", bibcode: str = "", pub: str = "") -> str:
    """
    Return a clean arXiv id like '2507.06989' (no version), from:
    - 'arXiv:2507.06989' or 'arXiv:2507.06989v2 [astro-ph.SR]'
    - 'https://arxiv.org/abs/2507.06989' (or /pdf/)
    - DOI form '10.48550/arXiv.2507.06989'
    - ADS bibcode '2025arXiv250706989K' (fallback)
    """
    ids = identifier_list or []

    # 1) Explicit arXiv:... strings
    for x in ids:
        if not isinstance(x, str):
            continue
        m = re.match(r"^arXiv:(?P<id>\d{4}\.\d{4,5})(?:v\d+)?", x, re.I)
        if m:
            return m.group("id")

    # 2) URLs to arxiv abs/pdf
    for x in ids:
        if not isinstance(x, str):
            continue
        m = re.search(r"arxiv\.org/(?:abs|pdf)/(?P<id>[\w\.\-]+)", x, re.I)
        if m:
            return m.group("id").split("v")[0]  # strip version if present

    # 3) DOI form for arXiv (DataCite)
    if doi and doi.lower().startswith(("10.48550/arxiv.", "10.48550/arxiv:")):
        return doi.split("arxiv", 1)[1].lstrip(".:").split("v")[0]

    # 4) Fallback: ADS arXiv bibcode encodes YYMM.number
    if bibcode and ("arXiv" in bibcode or (pub and pub == "arXiv e-prints")):
        m = re.search(r"arXiv(?P<id>\d{4}\.\d{4,5})", bibcode, re.I)
        if m:
            return m.group("id")

    return ""

def format_authors_html(authors: List[str], my_lastnames=("Villaseñor","Villasenor")) -> str:
    if not authors: return ""
    mynorms = [norm(n) for n in my_lastnames]
    fmt = []
    for a in authors:
        last = a.split(",")[0] if "," in a else a.split()[-1]
        is_me = norm(last) in mynorms
        fmt.append(f"<strong>{a}</strong>" if is_me else a)
    return ", ".join(fmt)

def map_doc(d: Dict) -> Dict:
    title   = clean_title((d.get("title") or [""])[0])
    authors = d.get("author") or []
    ids     = d.get("identifier") or []
    doi     = (d.get("doi") or [""])[0] if d.get("doi") else ""
    pub     = d.get("pub", "")
    year    = str(d.get("year", "")) if d.get("year") else ""
    bibcode = d.get("bibcode", "")
    props   = d.get("property") or []
    refereed_flag = ("REFEREED" in props)

    # ADS url (robust fallback)
    adsurl = f"https://ui.adsabs.harvard.edu/abs/{bibcode}" if bibcode else ""
    if not adsurl:
        for x in ids:
            if isinstance(x, str) and "ui.adsabs.harvard.edu/abs/" in x:
                adsurl = x; break
    if not adsurl:
        adsurl = "https://ui.adsabs.harvard.edu/"

    # arXiv id (robust)
    arxiv = extract_arxiv(ids, doi=doi, bibcode=bibcode, pub=pub)

    # Prefer publisher HTML for title (never arXiv), then DOI, else ADS
    best_url = pick_primary_url(doi, ids, adsurl)

    # Display-friendly authors
    authors_display = [format_author_display(a) for a in authors]
    me_index = next((i for i, a in enumerate(authors) if is_me(a)), -1)

    # NEW: single chronological key using BibTeX month or arXiv month
    sortdate, month_token, month_num = derive_sortdate_from_fields(
        pub=pub, year=year, arxiv_id=arxiv, refereed=refereed_flag, bibcode=bibcode
    )

    return {
        "bibcode": bibcode,
        "title": title,
        "authors": authors,
        "authors_html": format_authors_html(authors),
        "authors_short_html": format_authors_short_html(authors, max_authors=8),
        "authors_display": authors_display,
        "me_index": me_index,
        "n_authors": len(authors),
        "year": year,
        "pub": pub,
        "volume": d.get("volume", ""),
        "page": (d.get("page") or [""])[0] if d.get("page") else "",
        "page_range": (d.get("page_range") or [""])[0] if d.get("page_range") else "",
        "doi": doi,
        "arxiv": arxiv,
        "adsurl": adsurl,
        "best_url": best_url,
        "refereed": refereed_flag,          # was: ("REFEREED" in (d.get("property") or []))
        "citations": d.get("citation_count", 0),
        "month": month_token,                         # NEW (e.g., 'jun' if known)
        "month_num": month_num,                       # NEW (e.g., '06' or '' )
        "sortdate": sortdate,                         # NEW ('YYYY-MM-DD')
    }

def write_yaml(path: str, items: List[Dict]):
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(items, f, sort_keys=False, allow_unicode=True)

def is_me(name: str, my_lastnames=("Villaseñor","Villasenor")) -> bool:
    last = name.split(",")[0] if "," in name else name.split()[-1]
    return norm(last) in [norm(x) for x in my_lastnames]

def format_author_display(name: str) -> str:
    # ADS gives "Last, First Middle" → make "First Middle Last"
    if "," in name:
        last, first = [p.strip() for p in name.split(",", 1)]
        if "," in first:
            first, suffix = [p.strip() for p in first.split(",", 1)]
            return f"{first} {last}, {suffix}".strip()
        return f"{first} {last}".strip()
    return name

def format_authors_html(authors):
    """Full list; semicolon-separated; bold my name."""
    out = []
    for a in authors or []:
        disp = format_author_display(a)
        out.append(f"<strong>{disp}</strong>" if is_me(a) else disp)
    return "; ".join(out)

def format_authors_short_html(authors, max_authors=8):
    """Up to N authors; always include me if present; add 'et al.'"""
    authors = authors or []
    N = max_authors
    total = len(authors)
    mine_idx = next((i for i, a in enumerate(authors) if is_me(a)), None)

    show = authors[:N]
    me_included = any(is_me(a) for a in show)

    etal = total > N
    if etal and not me_included and mine_idx is not None:
        # Replace last slot with me so I'm visible
        show = authors[:N-1] + [authors[mine_idx]]

    parts = []
    for a in show:
        disp = format_author_display(a)
        parts.append(f"<strong>{disp}</strong>" if is_me(a) else disp)

    s = "; ".join(parts)
    if etal:
        s += ", <em>et&nbsp;al.</em>"
    return s

def pick_primary_url(doi: str, identifiers: list, adsurl: str) -> str:
    """Prefer publisher HTML (EDP/IOP/OUP/etc.), then DOI, else ADS. Never arXiv for the title."""
    ids = identifiers or []
    preferred_domains = (
        "aanda.org", "edpsciences.org",        # A&A (EDP)
        "academic.oup.com", "oxfordacademic.com",  # OUP/MNRAS
        "iopscience.iop.org",                  # IOP (ApJ/AJ)
        "nature.com", "science.org",
        "springer.com", "onlinelibrary.wiley.com",
        "cambridge.org", "ras.ac.uk"
    )
    doi_url = None
    for x in ids:
        if isinstance(x, str) and x.startswith("http"):
            if "arxiv.org" in x:
                continue  # never choose arXiv here; we show it as a badge
            if any(dom in x for dom in preferred_domains):
                return x
            if "doi.org/" in x:
                doi_url = x
    if doi:
        return f"https://doi.org/{doi}"
    if doi_url:
        return doi_url
    return adsurl

def add_tags(m):
    # robust, accent/case-insensitive thanks to your norm()
    title = norm(m.get("title", ""))
    journal = norm(m.get("pub", ""))  # sometimes "Sloan" appears here

    tags = []
    # SDSS / Sloan
    if "sdss" in title or "sloan" in title or "sdss" in journal or "sloan" in journal:
        tags.append("sdssv")

    # Algols
    if "algol" in title:
        tags.append("algols")

    # B-type binaries (several phrasings)
    if "b-type binaries" in title:
        tags.append("bbc")

    # Low metallicity contexts (incl. SMC/LMC mentions)
    if "bloem" in title:
        tags.append("bloem")

    m["tags"] = tags
    return m

def parse_args():
    parser = argparse.ArgumentParser(
        description="Sync ADS publications and optional metrics to YAML."
    )
    parser.add_argument(
        "library_name",
        nargs="?",
        default=DEFAULT_LIBRARY_NAME,
        help=f"ADS library name (default: {DEFAULT_LIBRARY_NAME})",
    )
    parser.add_argument(
        "out_all",
        nargs="?",
        default=DEFAULT_ALL_YML,
        help=f"Output YAML for all publications (default: {DEFAULT_ALL_YML})",
    )
    parser.add_argument(
        "--sdss",
        nargs="?",
        const=DEFAULT_SDSS_YML,
        default=None,
        metavar="PATH",
        help=f"Optional SDSS subset output (default: {DEFAULT_SDSS_YML})",
    )
    parser.add_argument(
        "--metrics",
        nargs="?",
        const=DEFAULT_METRICS_YML,
        default=None,
        metavar="PATH",
        help=f"Write metrics YAML (default: {DEFAULT_METRICS_YML})",
    )
    parser.add_argument(
        "--delta-year",
        type=int,
        default=None,
        help="Year used for delta calculations (default: reuse existing metrics year if set).",
    )
    parser.add_argument(
        "--metrics-only",
        action="store_true",
        help="Only refresh metrics using an existing publications file.",
    )
    return parser.parse_args()

def main():
    if not TOKEN:
        die("ADS_DEV_KEY is not set in environment.")

    args = parse_args()
    library_name = args.library_name
    out_all = args.out_all
    out_sdss = args.sdss
    out_metrics = args.metrics
    metrics_only = args.metrics_only

    if metrics_only and not out_metrics:
        out_metrics = DEFAULT_METRICS_YML
    delta_year = args.delta_year
    if not delta_year:
        delta_year = read_existing_delta_year(out_metrics)
    if not delta_year:
        delta_year = coerce_int(time.strftime("%Y"))

    if metrics_only:
        if not os.path.exists(out_all):
            die(f"{out_all} not found; run without --metrics-only first.")
        with open(out_all, "r", encoding="utf-8") as f:
            mapped = yaml.safe_load(f) or []
        bibs = [m.get("bibcode") for m in mapped if m.get("bibcode")]
    else:
        lib_id = find_library_id(library_name)
        bibs = get_bibcodes_for_library(lib_id)
        if not bibs:
            die("No bibcodes found in library.")

        docs = fetch_metadata_for_bibcodes(bibs)

        # Build a month map from BibTeX for refereed, non-arXiv items
        ref_bibcodes = [d.get("bibcode","") for d in docs
                        if d.get("pub") != "arXiv e-prints" and "REFEREED" in (d.get("property") or [])]
        global BIBTEX_MONTH_BY_BIBCODE
        BIBTEX_MONTH_BY_BIBCODE = fetch_bibtex_months(ref_bibcodes)

        mapped = [map_doc(d) for d in docs]
        mapped = [add_tags(m) for m in mapped]         # keep your tagging step
        # mapped.sort(key=lambda x: (x.get("year",""), x.get("bibcode","")), reverse=True)
        mapped.sort(key=lambda x: (x.get("sortdate",""), x.get("bibcode","")), reverse=True)

        write_yaml(out_all, mapped)
        print(f"Wrote {len(mapped)} items to {out_all}")

    if out_metrics:
        metrics_raw = fetch_metrics(bibs)
        metrics_payload = build_metrics_payload(metrics_raw, mapped, delta_year=delta_year)
        write_yaml(out_metrics, metrics_payload)
        print(f"Wrote metrics to {out_metrics}")

    # if out_sdss:
    #     filtered = [m for m in mapped if "sdssv" in (m.get("tags") or [])]
    #     write_yaml(out_sdss, filtered)
    #     print(f"Wrote {len(filtered)} SDSS/Sloan items to {out_sdss}")

if __name__ == "__main__":
    main()
