from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from models.schemas import FilingSearchResult, Filing, InsiderResponse, InsiderTransaction, TodayFilingsResponse
from data.filing_index import search_filings, get_filing_by_key, get_insider_filings, get_today_filings, FILINGS

router = APIRouter(prefix="/api/v1", tags=["search"])


@router.get("/search", response_model=FilingSearchResult)
def search(
    q: Optional[str] = Query(None, description="Full-text search query"),
    form_type: Optional[str] = Query(None, regex="^(4|8-K|10-Q|10-K)$", description="Form type filter"),
    sector: Optional[str] = Query(None, regex="^(tech|healthcare|energy|finance)$", description="Sector filter"),
    limit: int = Query(20, ge=1, le=100, description="Max results to return"),
):
    results = search_filings(query=q, form_type=form_type, sector=sector, limit=limit)
    return FilingSearchResult(total=len(results), results=results)


@router.get("/filing/{cik}/{form_type}/{accession}", response_model=Filing)
def get_filing(cik: str, form_type: str, accession: str):
    filing = get_filing_by_key(cik, form_type, accession)
    if not filing:
        raise HTTPException(status_code=404, detail="Filing not found")
    return filing


@router.get("/insider/{ticker}", response_model=InsiderResponse)
def get_insider(ticker: str):
    filings = get_insider_filings(ticker.upper())
    if not filings:
        raise HTTPException(status_code=404, detail=f"No Form 4 filings found for ticker {ticker}")
    company_name = filings[0].company_name if filings else ""
    transactions = []
    for f in filings:
        # Parse insider info from description
        desc = f.description
        # e.g. "Form 4: Timothy D. Cook (CEO) — Purchase 5000 shares at $150.00/share"
        parts = desc.split(" — ")
        if len(parts) >= 2:
            meta = parts[0].replace("Form 4: ", "")
            transaction_detail = parts[1]
            ttype = "Purchase" if "Purchase" in transaction_detail else "Sale"
            shares_str = transaction_detail.split(" ")[2] if len(transaction_detail.split(" ")) > 2 else "0"
            try:
                shares = int(shares_str.replace(",", ""))
            except:
                shares = 0
            price_str = transaction_detail.split("$")[1].split("/")[0] if "$" in transaction_detail else "0"
            try:
                price = float(price_str.replace(",", ""))
            except:
                price = 0.0
            name_parts = meta.split("(")
            name = name_parts[0].strip() if name_parts else "Unknown"
            title = name_parts[1].replace(")", "") if len(name_parts) > 1 else None
        else:
            name = "Unknown Insider"
            title = None
            ttype = "Unknown"
            shares = 0
            price = 0.0

        transactions.append(InsiderTransaction(
            insider_name=name,
            insider_title=title,
            transaction_type=ttype,
            shares=shares,
            price_per_share=price,
            filing_date=f.filing_date,
            ticker=ticker.upper(),
            company_name=company_name,
        ))

    return InsiderResponse(
        ticker=ticker.upper(),
        company_name=company_name,
        total_transactions=len(transactions),
        transactions=transactions,
    )


@router.get("/filings/today", response_model=TodayFilingsResponse)
def get_today():
    filings = get_today_filings()
    form4 = [f for f in filings if f.form_type == "4"]
    eightk = [f for f in filings if f.form_type == "8-K"]
    return TodayFilingsResponse(
        date=filings[0].filing_date if filings else "",
        form_4_count=len(form4),
        eight_k_count=len(eightk),
        filings=filings,
    )
