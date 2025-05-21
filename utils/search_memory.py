# utils/search_memory.py

import sqlite3
import sys
from pathlib import Path
from config import DB_PATH

sys.path.append(str(Path(__file__).resolve().parents[1]))


def search_by_keyword(keyword):
    """Search memory shards by keyword in title, purpose, or summary."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT * FROM memory_shards
    WHERE title LIKE ? OR purpose LIKE ? OR summary LIKE ?
    ORDER BY date DESC
    """
    pattern = f"%{keyword}%"
    cursor.execute(query, (pattern, pattern, pattern))
    results = cursor.fetchall()
    conn.close()
    return results


def search_by_tag(tag):
    """Search memory shards by tag (matches partial tag strings)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT * FROM memory_shards
    WHERE tags LIKE ?
    ORDER BY date DESC
    """
    cursor.execute(query, (f"%{tag}%",))
    results = cursor.fetchall()
    conn.close()
    return results


def search_by_date_range(start_date, end_date):
    """Search memory shards between two ISO date strings."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT * FROM memory_shards
    WHERE date BETWEEN ? AND ?
    ORDER BY date ASC
    """
    cursor.execute(query, (start_date, end_date))
    results = cursor.fetchall()
    conn.close()
    return results


def search_by_multiple_keywords(keywords):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    conditions = " OR ".join(
        ["title LIKE ? OR purpose LIKE ? OR summary LIKE ?" for _ in keywords]
    )
    patterns = [f"%{k}%" for k in keywords for _ in range(3)]

    cursor.execute(f"SELECT * FROM memory_shards WHERE {conditions}", patterns)
    results = cursor.fetchall()
    conn.close()
    return results
