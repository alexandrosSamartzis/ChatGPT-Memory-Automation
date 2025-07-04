# utils/save_memory.py

import sqlite3
from pathlib import Path
from datetime import datetime
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from config import DB_PATH, MEMORY_DIR


def save_memory(
    title, date=None, purpose="", tags=None, summary="", filename_slug=None
):
    """
    Save a memory shard into both the SQLite DB and a Markdown file.
    """
    # Prepare data
    date_str = date or datetime.today().strftime("%Y-%m-%d")
    tags_str = ", ".join(tags) if isinstance(tags, list) else (tags or "")

    # Create a safe filename
    if not filename_slug:
        filename_slug = title.lower().replace(" ", "_").replace("/", "-")

    md_filename = f"{filename_slug}_{date_str}.md"
    md_path = MEMORY_DIR / md_filename
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    # Write memory to markdown file
    md_content = f"""# {title}

**Date**: {date_str}  
**Tags**: {tags_str}

## Purpose
{purpose}
print("Print this")
## Summary
{summary}
"""

    md_path.write_text(md_content, encoding="utf-8")

    # Save memory to SQLite DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO memory_shards (title, date, purpose, tags, filepath, summary)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (title, date_str, purpose, tags_str, str(md_path), summary),
    )

    conn.commit()
    conn.close()

    print(f"✅ Memory saved to DB and Markdown: {md_path.name}")
    return md_path
