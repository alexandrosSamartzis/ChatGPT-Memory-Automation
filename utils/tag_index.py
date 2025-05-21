def get_tag_and_word_index():
    import sqlite3
    from collections import Counter
    from config import DB_PATH

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT tags, summary FROM memory_shards")
    rows = cursor.fetchall()
    conn.close()

    tag_set = set()
    word_counter = Counter()

    for tags, summary in rows:
        # Tags handling
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
        tag_set.update(tag_list)
        # Summary word indexing (null-safe)
        if summary:
            words = summary.lower().split()
            words = [w.strip(",.():;\"'") for w in words if len(w) > 3]
            word_counter.update(words)

    top_words = [w for w, count in word_counter.most_common(100)]
    return sorted(tag_set), sorted(top_words)
