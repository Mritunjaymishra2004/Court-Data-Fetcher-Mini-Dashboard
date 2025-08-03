import sqlite3

def log_query(case_type, case_number, year, html):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            year INTEGER,
            query_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            raw_html TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO queries (case_type, case_number, year, raw_html)
        VALUES (?, ?, ?, ?)
    """, (case_type, case_number, year, html))
    conn.commit()
    conn.close()
