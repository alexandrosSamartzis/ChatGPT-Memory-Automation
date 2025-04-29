import re
from save_memory import save_memory


def extract_field(text, pattern):
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1) if match else None


def save_from_formatted_summary(raw_text):
    title = extract_field(raw_text, r"^# 🧠 Memory Shard: (.+)$")
    date = extract_field(raw_text, r"\*\*Date:\*\* (.+)")
    purpose = extract_field(raw_text, r"## 🎯 Purpose\s+(.+?)\n(?:##|---)")
    summary = extract_field(raw_text, r"## 📌 Key Points\s+(.+?)\n(?:##|---)")
    tags_raw = extract_field(raw_text, r"## 🏷️ Tags\s+(.+)")
    tags = [tag.strip().lstrip("#") for tag in re.findall(r"#?(\w[\w\-]*)", tags_raw)]

    # Fallback title slug
    slug = (
        title.lower().replace(" ", "_").replace("/", "-") if title else "memory_entry"
    )

    save_memory(
        title=title or "Untitled Memory",
        date=date,
        purpose=purpose,
        tags=tags,
        summary=summary,
        filename_slug=slug,
    )
