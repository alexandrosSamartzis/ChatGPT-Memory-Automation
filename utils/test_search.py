from search_memory import search_by_keyword, search_by_tag, search_by_date_range
from save_memory import save_memory

save_memory(
    title="German Subtitle App Setup",
    date="2025-04-29",
    purpose="Initialize the memory assistant project and subtitle simplification.",
    tags=["subtitle", "streamlit", "local model", "ollama"],
    summary="""
Set up Streamlit app to manage ChatGPT memories. Integrated Ollama local models. Confirmed no need for CUDA on Mac M2. Prepared the SQLite database and basic project structure.
""",
)

print("\n🔍 Keyword Search:")
for row in search_by_keyword("subtitle"):
    print(row)

print("\n🏷️ Tag Search:")
for row in search_by_tag("streamlit"):
    print(row)

print("\n📆 Date Range Search:")
for row in search_by_date_range("2025-04-01", "2025-04-30"):
    print(row)
