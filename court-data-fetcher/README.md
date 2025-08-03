# Court-Data Fetcher & Mini Dashboard

## Court Targeted
Faridabad District Court – https://districts.ecourts.gov.in/faridabad

## Tech Stack
- Python 3 + Flask
- Selenium + BeautifulSoup
- SQLite for query logging
- HTML/CSS for frontend

## How to Run Locally

```bash
git clone <your_repo_link>
cd court-data-fetcher
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
python app.py
