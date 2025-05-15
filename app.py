# app.py
from pathlib import Path
import sys
import streamlit as st
from utils.save_from_formatted import save_from_formatted_summary
from utils.search_memory import search_by_keyword

sys.path.append(str(Path(__file__).resolve().parents[1]))

st.set_page_config(page_title="🧠 ChatGPT Memory Assistant", layout="wide")
st.title("🧠 ChatGPT Memory Automation")

# ────────────────────────────────────────────────────────────────
# 📋 SIDEBAR SEARCH
# ────────────────────────────────────────────────────────────────

st.sidebar.header("🔍 Search Memory")
keyword = st.sidebar.text_input("Search by keyword")

if keyword:
    results = search_by_keyword(keyword)
    st.subheader("🔎 Search Results")
    for row in results:
        st.markdown(f"### 🧠 {row[1]} ({row[2]})")
        st.markdown(f"**Purpose**: {row[3]}")
        st.markdown(f"**Tags**: `{row[4]}`")
        with st.expander("📝 Summary"):
            st.markdown(row[6])

st.divider()

# ────────────────────────────────────────────────────────────────
# 📥 MEMORY ENTRY FORM
# ────────────────────────────────────────────────────────────────

st.subheader("📥 Paste a ChatGPT Memory Summary")

raw_input = st.text_area(
    "Paste your full markdown-formatted summary here",
    height=300,
    placeholder="Paste a memory summary like:\n\n# 🧠 Memory Shard: ...\n**Date:** ...\n## 🎯 Purpose...\n...",
)

if st.button("💾 Save Memory"):
    if raw_input.strip():
        save_from_formatted_summary(raw_input)
        st.success("✅ Memory saved to DB and markdown file.")
    else:
        st.warning("⚠️ Please paste a summary before saving.")
