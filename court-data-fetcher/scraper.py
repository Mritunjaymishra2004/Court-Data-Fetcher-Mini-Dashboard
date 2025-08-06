# Simulated scraping logic (replace with Selenium for real court scraping)

def fetch_case_details(case_type, case_number, year):
    # Dummy data for submission
    html = "<html><body><h1>Mock HTML</h1></body></html>"

    result = {
        "parties": f"{case_type}-{case_number}/{year} Plaintiff vs Defendant",
        "filing_date": "2023-01-01",
        "next_hearing": "2025-09-01",
        "order_pdf": "https://example.com/x.pdf"
    }

    return result, html
