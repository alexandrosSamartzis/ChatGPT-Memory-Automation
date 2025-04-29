from search_memory import search_by_keyword, search_by_tag, search_by_date_range

print("\n🔍 Keyword Search:")
for row in search_by_keyword("subtitle"):
    print(row)

print("\n🏷️ Tag Search:")
for row in search_by_tag("streamlit"):
    print(row)

print("\n📆 Date Range Search:")
for row in search_by_date_range("2025-04-01", "2025-04-30"):
    print(row)
