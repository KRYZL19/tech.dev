import random
from datetime import date, timedelta
from models.schemas import Filing, InsiderTransaction

TODAY = date.today().isoformat()

COMPANIES = [
    {"ticker": "AAPL", "cik": "0000320193", "name": "Apple Inc.", "sector": "tech"},
    {"ticker": "MSFT", "cik": "0000789019", "name": "Microsoft Corporation", "sector": "tech"},
    {"ticker": "GOOGL", "cik": "0001652044", "name": "Alphabet Inc.", "sector": "tech"},
    {"ticker": "AMZN", "cik": "0001018724", "name": "Amazon.com Inc.", "sector": "tech"},
    {"ticker": "NVDA", "cik": "0001045810", "name": "NVIDIA Corporation", "sector": "tech"},
    {"ticker": "TSLA", "cik": "0001318605", "name": "Tesla Inc.", "sector": "tech"},
    {"ticker": "META", "cik": "0001326801", "name": "Meta Platforms Inc.", "sector": "tech"},
    {"ticker": "NFLX", "cik": "0001065280", "name": "Netflix Inc.", "sector": "tech"},
    {"ticker": "AMD", "cik": "0000002488", "name": "Advanced Micro Devices", "sector": "tech"},
    {"ticker": "INTC", "cik": "0000050863", "name": "Intel Corporation", "sector": "tech"},
    {"ticker": "ORCL", "cik": "0000737671", "name": "Oracle Corporation", "sector": "tech"},
    {"ticker": "CRM", "cik": "0001108524", "name": "Salesforce Inc.", "sector": "tech"},
    {"ticker": "ADBE", "cik": "0000796343", "name": "Adobe Inc.", "sector": "tech"},
    {"ticker": "CSCO", "cik": "0000858877", "name": "Cisco Systems", "sector": "tech"},
    {"ticker": "PYPL", "cik": "0001626517", "name": "PayPal Holdings", "sector": "tech"},
    {"ticker": "UBER", "cik": "0001563158", "name": "Uber Technologies", "sector": "tech"},
    {"ticker": "SNAP", "cik": "0001564408", "name": "Snap Inc.", "sector": "tech"},
    {"ticker": "SQ", "cik": "0001512673", "name": "Block Inc.", "sector": "tech"},
    {"ticker": "SHOP", "cik": "0001590605", "name": "Shopify Inc.", "sector": "tech"},
    {"ticker": "ABNB", "cik": "0001559720", "name": "Airbnb Inc.", "sector": "tech"},
    {"ticker": "JPM", "cik": "0000019617", "name": "JPMorgan Chase & Co.", "sector": "finance"},
    {"ticker": "BAC", "cik": "0000070858", "name": "Bank of America", "sector": "finance"},
    {"ticker": "WFC", "cik": "0000072961", "name": "Wells Fargo & Co.", "sector": "finance"},
    {"ticker": "GS", "cik": "0000886982", "name": "Goldman Sachs", "sector": "finance"},
    {"ticker": "MS", "cik": "0000895421", "name": "Morgan Stanley", "sector": "finance"},
    {"ticker": "V", "cik": "0001366312", "name": "Visa Inc.", "sector": "finance"},
    {"ticker": "MA", "cik": "0001141391", "name": "Mastercard Inc.", "sector": "finance"},
    {"ticker": "BLK", "cik": "0001364742", "name": "BlackRock Inc.", "sector": "finance"},
    {"ticker": "SCHW", "cik": "0000736709", "name": "Charles Schwab", "sector": "finance"},
    {"ticker": "AXP", "cik": "0000049627", "name": "American Express", "sector": "finance"},
    {"ticker": "C", "cik": "0000831001", "name": "Citigroup Inc.", "sector": "finance"},
    {"ticker": "USB", "cik": "0000096108", "name": "U.S. Bancorp", "sector": "finance"},
    {"ticker": "PNC", "cik": "0000713676", "name": "PNC Financial", "sector": "finance"},
    {"ticker": "TFC", "cik": "0001543043", "name": "Truist Financial", "sector": "finance"},
    {"ticker": "COF", "cik": "0000927628", "name": "Capital One", "sector": "finance"},
    {"ticker": "JNJ", "cik": "0000200406", "name": "Johnson & Johnson", "sector": "healthcare"},
    {"ticker": "UNH", "cik": "0000731766", "name": "UnitedHealth Group", "sector": "healthcare"},
    {"ticker": "PFE", "cik": "0000078003", "name": "Pfizer Inc.", "sector": "healthcare"},
    {"ticker": "ABBV", "cik": "0001159139", "name": "AbbVie Inc.", "sector": "healthcare"},
    {"ticker": "MRK", "cik": "0000310158", "name": "Merck & Co.", "sector": "healthcare"},
    {"ticker": "LLY", "cik": "0000594743", "name": "Eli Lilly", "sector": "healthcare"},
    {"ticker": "TMO", "cik": "0000097745", "name": "Thermo Fisher", "sector": "healthcare"},
    {"ticker": "ABT", "cik": "0000001800", "name": "Abbott Laboratories", "sector": "healthcare"},
    {"ticker": "DHR", "cik": "0000943614", "name": "Danaher Corporation", "sector": "healthcare"},
    {"ticker": "BMY", "cik": "0000014272", "name": "Bristol-Myers Squibb", "sector": "healthcare"},
    {"ticker": "AMGN", "cik": "0000318154", "name": "Amgen Inc.", "sector": "healthcare"},
    {"ticker": "GILD", "cik": "0000887395", "name": "Gilead Sciences", "sector": "healthcare"},
    {"ticker": "CVS", "cik": "0000648030", "name": "CVS Health", "sector": "healthcare"},
    {"ticker": "ISRG", "cik": "0001144960", "name": "Intuitive Surgical", "sector": "healthcare"},
    {"ticker": "VRTX", "cik": "0000875320", "name": "Vertex Pharmaceuticals", "sector": "healthcare"},
    {"ticker": "XOM", "cik": "0000034088", "name": "Exxon Mobil", "sector": "energy"},
    {"ticker": "CVX", "cik": "0000093410", "name": "Chevron Corporation", "sector": "energy"},
    {"ticker": "COP", "cik": "0001168165", "name": "ConocoPhillips", "sector": "energy"},
    {"ticker": "SLB", "cik": "0000087347", "name": "Schlumberger", "sector": "energy"},
    {"ticker": "EOG", "cik": "0001321885", "name": "EOG Resources", "sector": "energy"},
    {"ticker": "MPC", "cik": "0001513957", "name": "Marathon Petroleum", "sector": "energy"},
    {"ticker": "PSX", "cik": "0001577026", "name": "Phillips 66", "sector": "energy"},
    {"ticker": "OXY", "cik": "0000797464", "name": "Occidental Petroleum", "sector": "energy"},
    {"ticker": "BKR", "cik": "0001444406", "name": "Baker Hughes", "sector": "energy"},
    {"ticker": "HAL", "cik": "0000045072", "name": "Halliburton", "sector": "energy"},
    {"ticker": "DVN", "cik": "0001090012", "name": "Devon Energy", "sector": "energy"},
    {"ticker": "FANG", "cik": "0001533048", "name": "Diamondback Energy", "sector": "energy"},
]

INSIDER_NAMES = [
    ("Timothy D. Cook", "CEO"),
    ("Jeffrey L. Williams", "COO"),
    ("Luca J. Maestri", "CFO"),
    ("Katherine L. Adams", "General Counsel"),
    ("Deirdre A. O'Brien", "SVP Retail"),
    ("Craig T. Federighi", "SVP Engineering"),
    ("Eddy T. Cue", "SVP Services"),
    ("Johny T. Srouji", "SVP Hardware"),
    ("Satya S. Nadella", "CEO"),
    ("Amy E. Hood", "CFO"),
    ("Bradford L. Smith", "President"),
    ("Margaret A. Spata", "General Counsel"),
    ("Scott T. Gusmorino", "SVP Sales"),
    ("Sanjay S. N. Jha", "CEO"),
    ("Mark T. Zuckerberg", "CEO"),
    ("Susan L. Wojcicki", "CEO"),
    ("Jennifer L. Johnson", "CFO"),
    ("David M. Wehner", "CFO"),
    ("Javier E. Olivan", "COO"),
    ("Susan L. Taylor", "General Counsel"),
    ("Gokul K. Rajaram", "Board Member"),
    ("Larry J. Ellison", "Founder & CTO"),
    ("Safra A. Catz", "CEO"),
    ("Jeffrey O. Henley", "Chairman"),
    ("Mark J. Mulready", "SVP Operations"),
    ("James T. Buckhouse", "SVP Engineering"),
    ("Daniel L. K. Zhang", "CFO"),
    ("Brian T. McCarthy", "COO"),
    ("Ronald J. Gill", "CFO"),
    ("Blake J. G. Irving", "CFO"),
    ("Alan J. H. McCreath", "SVP"),
    ("David M. B. S. Kim", "General Counsel"),
]

TRANSACTION_TYPES = [
    ("P", "Purchase"),
    ("S", "Sale"),
    ("A", "Award (RSU/Stock Grant)"),
    ("M", "Match to option exercise"),
    ("F", "Taxes withheld"),
]

FORM4_DESCRIPTIONS = [
    "Equity award pursuant to 2020 Stock Incentive Plan",
    "Disposition of shares pursuant to 10b5-1 trading plan",
    "Open market purchase of common stock",
    "Sale of common stock pursuant to Rule 10b5-1",
    "Exercise of stock options",
    "Vesting of restricted stock units",
    "Annual grant of performance stock units",
    "Charitable contribution of shares",
    ("G", "Gift of securities"),
    ("D", "Disposition"),
]

EVENT8K = [
    "Announces strategic partnership with {}",
    "Reports Q{} financial results, beats estimates",
    "Files for voluntary delisting from {} exchange",
    "Appoints new {} to Board of Directors",
    "Announces share repurchase program of ${}B",
    "Receives FDA approval for {} product candidate",
    "Expands operations into {} market",
    "Declares quarterly dividend of ${} per share",
    "Enters into definitive agreement to acquire {}",
    "Reschedules Q{} earnings call to {}",
    "Announces leadership transition, {} to step down",
    "Files Form 8-K disclosing material definitive agreement",
    "Reports cybersecurity incident, no material impact",
    "Announces ${}B infrastructure investment plan",
    "Updates full-year guidance, raises outlook",
    "Completes spin-off of {} subsidiary",
    "Announces ${}B debt offering",
    "Discloses departure of Chief {} Officer",
]

FORM10Q_SECTIONS = [
    "Condensed Consolidated Balance Sheets",
    "Condensed Consolidated Statements of Operations",
    "Management's Discussion and Analysis",
    "Quantitative and Qualitative Disclosures About Market Risk",
    "Controls and Procedures",
    "Legal Proceedings",
    "Unregistered Sales of Equity Securities",
    "Defaults Upon Senior Securities",
    "Mine Safety Disclosures",
]

FORM10K_SECTIONS = [
    "Business",
    "Risk Factors",
    "Unresolved Staff Comments",
    "Properties",
    "Legal Proceedings",
    "Market for Registrant's Common Equity",
    "Management's Discussion and Analysis",
    "Financial Statements and Supplementary Data",
    "Changes in and Disagreements with Accountants",
    "Controls and Procedures",
    "Other Information",
]

_accession_counter = 100000


def next_accession():
    global _accession_counter
    _accession_counter += 1
    return f"{_accession_counter:010d}"


def random_date(days_back=60):
    d = random.randint(0, days_back)
    return (date.today() - timedelta(days=d)).isoformat()


def make_form4(company, filing_date):
    insider = random.choice(INSIDER_NAMES)
    trans = random.choice(TRANSACTION_TYPES)
    shares = random.randint(100, 50000)
    price = round(random.uniform(50, 800), 2)
    acc = next_accession()
    return Filing(
        cik=company["cik"],
        ticker=company["ticker"],
        company_name=company["name"],
        form_type="4",
        filing_date=filing_date,
        accession=acc,
        description=f"Form 4: {insider[0]} ({insider[1]}) — {trans[1]} {shares} shares at ${price}/share",
        sector=company["sector"],
        link_to_html=f"https://www.sec.gov/Archives/edgar/data/{company['cik']}/{acc.replace('0','')}/{company['ticker'].lower()}-form4.htm",
    )


def make_8k(company, filing_date):
    templates = [
        f"Announces Q{random.randint(1,4)} financial results",
        f"Appoints new {random.choice(['Chief Financial','Chief Technology','Chief Operating'])} Officer",
        f"Announces share repurchase program of ${random.randint(1,10)}B",
        f"Declares quarterly dividend of ${round(random.uniform(0.1, 2.0), 2)} per share",
        f"Enters into agreement to acquire {random.choice(['a','a strategic','a new'])} company",
        f"Updates full-year 2025 guidance, raises revenue outlook",
        f"Reports preliminary Q{random.randint(1,4)} metrics",
        f"Announces $2B infrastructure investment",
        f"Board declares special cash dividend",
    ]
    acc = next_accession()
    return Filing(
        cik=company["cik"],
        ticker=company["ticker"],
        company_name=company["name"],
        form_type="8-K",
        filing_date=filing_date,
        accession=acc,
        description=random.choice(templates),
        sector=company["sector"],
        link_to_html=f"https://www.sec.gov/Archives/edgar/data/{company['cik']}/{acc.replace('0','')}/{company['ticker'].lower()}-8k.htm",
    )


def make_10q(company, filing_date):
    q = random.randint(1, 4)
    acc = next_accession()
    return Filing(
        cik=company["cik"],
        ticker=company["ticker"],
        company_name=company["name"],
        form_type="10-Q",
        filing_date=filing_date,
        accession=acc,
        description=f"Q{q} 2025 Quarterly Report — {company['name']}",
        sector=company["sector"],
        link_to_html=f"https://www.sec.gov/Archives/edgar/data/{company['cik']}/{acc.replace('0','')}/{company['ticker'].lower()}-10q.htm",
    )


def make_10k(company, filing_date):
    acc = next_accession()
    return Filing(
        cik=company["cik"],
        ticker=company["ticker"],
        company_name=company["name"],
        form_type="10-K",
        filing_date=filing_date,
        accession=acc,
        description=f"Annual Report on Form 10-K for fiscal year 2024 — {company['name']}",
        sector=company["sector"],
        link_to_html=f"https://www.sec.gov/Archives/edgar/data/{company['cik']}/{acc.replace('0','')}/{company['ticker'].lower()}-10k.htm",
    )


def generate_filings():
    filings = []

    # Distribute ~200 filings
    # ~80 Form 4 filings (spread across companies, some recent)
    for _ in range(80):
        c = random.choice(COMPANIES)
        d = random_date(90)
        filings.append(make_form4(c, d))

    # ~60 8-K filings
    for _ in range(60):
        c = random.choice(COMPANIES)
        d = random_date(60)
        filings.append(make_8k(c, d))

    # ~40 10-Q filings
    for _ in range(40):
        c = random.choice(COMPANIES)
        d = random_date(120)
        filings.append(make_10q(c, d))

    # ~20 10-K filings
    for _ in range(20):
        c = random.choice(COMPANIES)
        d = random_date(150)
        filings.append(make_10k(c, d))

    # Make ~10 filings dated exactly today for /filings/today
    today = date.today()
    for i in range(10):
        c = COMPANIES[i % len(COMPANIES)]
        ft = "4" if i % 2 == 0 else "8-K"
        if ft == "4":
            f = make_form4(c, today.isoformat())
        else:
            f = make_8k(c, today.isoformat())
        # Override accession to ensure they're included
        f.accession = f"00000000{1000+i}"
        filings.append(f)

    return filings


FILINGS = generate_filings()
FILINGS_BY_CIK = {}
for f in FILINGS:
    FILINGS_BY_CIK.setdefault(f.cik, []).append(f)


def search_filings(query=None, form_type=None, sector=None, limit=20):
    results = FILINGS[:]
    if query:
        q = query.lower()
        results = [r for r in results if q in r.description.lower() or q in r.company_name.lower() or q in r.ticker.lower()]
    if form_type:
        results = [r for r in results if r.form_type == form_type]
    if sector:
        results = [r for r in results if r.sector == sector]
    return results[:limit]


def get_filing_by_key(cik, form_type, accession):
    for f in FILINGS:
        if f.cik == cik and f.form_type == form_type and f.accession == accession:
            return f
    return None


def get_insider_filings(ticker):
    company = next((c for c in COMPANIES if c["ticker"] == ticker.upper()), None)
    if not company:
        return []
    return [f for f in FILINGS if f.ticker == ticker.upper() and f.form_type == "4"]


def get_today_filings():
    today = date.today().isoformat()
    today_filings = [f for f in FILINGS if f.filing_date == today]
    return today_filings
