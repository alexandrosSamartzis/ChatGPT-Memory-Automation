# database/init_db.py
import sqlite3
from pathlib import Path
import sys
from config import DB_PATH

sys.path.append(str(Path(__file__).resolve().parents[1]))


def initialize_database():
    # Make sure the database folder exists
    db_folder = DB_PATH.parent
    db_folder.mkdir(parents=True, exist_ok=True)

    # Connect to the SQLite database (creates file if not exists)
    conn = sqlite3.connect(DB_PATH)

    # Create the memory_shards table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS memory_shards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        date TEXT,
        purpose TEXT,
        tags TEXT,
        filepath TEXT NOT NULL,
        summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    conn.execute(create_table_query)
    conn.commit()
    conn.close()
    print(f"✅ Database initialized at {DB_PATH}")


if __name__ == "__main__":
    initialize_database()
