# app.py
from pathlib import Path
import sys
import streamlit as st
from utils.save_from_formatted import save_from_formatted_summary
from utils.search_memory import search_by_keyword, search_by_multiple_keywords
from utils.tag_index import get_tag_and_word_index

import os

sys.path.append(str(Path(__file__).resolve().parents[1]))

st.set_page_config(page_title="🧠 ChatGPT Memory Assistant", layout="wide")
st.title("🧠 ChatGPT Memory Automation")

# ────────────────────────────────────────────────────────────────
# 📋 SIDEBAR SEARCH
# ────────────────────────────────────────────────────────────────


st.sidebar.header("🔍 Smart Search")

tags, words = get_tag_and_word_index()

search_input = st.sidebar.text_input(
    "Search (use comma to combine)", placeholder="e.g. streamlit, summary"
)

if st.sidebar.button("🔠 Show All Tags & Words"):
    with st.sidebar.expander("📚 Available Terms"):
        st.markdown("**Tags:**  \n" + ", ".join(tags))
        st.markdown("---")
        st.markdown("**Keywords:**  \n" + ", ".join(words))


if search_input:
    search_terms = [t.strip().lower() for t in search_input.split(",") if t.strip()]

    if len(search_terms) == 1:
        results = search_by_keyword(search_terms[0])
    else:
        results = search_by_multiple_keywords(search_terms)

    for row in results:

        try:
            memory_id, title, date, purpose, tags, filepath, summary, created_at = row
        except ValueError:
            st.warning("Skipping malformed row.")
            continue
        st.markdown(f"### 🧠 {title}  \n📅 *{date}*")
        st.markdown(f"**Purpose:** {purpose}")
        st.markdown(f"**Tags:** `{tags}`")

        with st.expander("📝 View Full Summary"):
            st.markdown(summary)

        if st.button(f"📋 Use this memory", key=f"use-{memory_id}"):
            st.session_state["selected_memory"] = row
            st.success(f"Loaded memory: {title}")

with st.sidebar.expander("ℹ️ Search Rules"):
    st.markdown(
        """
**How to search:**
- Type any word or tag: `streamlit`
- Use comma to combine up to 3: `azure, identity, pricing`
- Click 'Show All Tags' to explore your memory dictionary
"""
    )

st.divider()

# ────────────────────────────────────────────────────────────────
# 📥 MEMORY Presentation
# ────────────────────────────────────────────────────────────────

if "selected_memory" in st.session_state:
    memory = st.session_state["selected_memory"]
    st.subheader("🎯 Selected Memory")

    st.markdown(f"### 🧠 {memory[1]}")
    st.markdown(f"**Date:** {memory[2]}")
    st.markdown(f"**Tags:** `{memory[4]}`")
    st.markdown(f"**Purpose:** {memory[3]}")
    st.markdown("---")
    st.markdown(memory[6])

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

with st.expander("📋 Need the summary prompt? Click to view & copy", expanded=False):
    prompt_template = """```markdown
# 🧠 Memory Shard: [Concise Title]

**Date:** [Today's Date]

## 📍 Topic  
[Short description of the topic]

---

## 🎯 Purpose  
[Why this conversation was important]

---

## 📌 Key Points  
- [Main idea 1]
- [Main idea 2]

---

## ✅ Next Steps  
- [Follow-up action 1]

---

## 🏷️ Tags  
#tag1 #tag2 #project #theme
```"""
    st.code(prompt_template, language="markdown")
    st.caption("Copy and paste this into ChatGPT to structure your memory shard.")
if st.button("💾 Save Memory"):
    if raw_input.strip():
        save_from_formatted_summary(raw_input)
        st.success("✅ Memory saved to DB and markdown file.")
    else:
        st.warning("⚠️ Please paste a summary before saving.")


st.divider()
if st.button("❌ Close App"):
    st.warning("Shutting down Memory app...")
    os.system("pkill -f streamlit")
    os._exit(0)
