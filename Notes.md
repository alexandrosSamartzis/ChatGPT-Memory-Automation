# Subtitle App Memory – April 2025

## Purpose

Build a UI for memory automation of ChatGPT chats.

## Key Points

- Uses local models via Ollama
- Streamlit-based app
- Stores memory shards locally

## Tags

#language #gpt #project #subtitle

# ChatGPT Memory Automation - Project Initialization

# Profile: ChatGPT Memory Automation

# This profile sets up the environment, dependencies, and structure for your memory assistant app.

# 1. Project Folder Structure Suggestion

project_structure = """
CChatGPT-Memory-Automation/
├── app.py
├── config.py
├── memory/
├── database/
│ └── init_db.py
├── utils/
├── assets/
├── requirements.txt
├── README.md
└── .env
"""

# 2. Environment Setup: Create a Python virtual environment (Unix-based shell)

shell_setup_commands = """

# Create virtual environment

python3 -m venv .venv

# Activate it

source .venv/bin/activate

# Install required packages

pip install streamlit openai sqlite-utils typer python-dotenv

# Freeze dependencies

pip freeze > requirements.txt
"""

# 3. .gitignore Suggestions

gitignore_content = """
.venv/
**pycache**/
.env
_.db
memory/_.txt
memory/\*.json
"""

# 4. README.md Bootstrap

readme_intro = """

# ChatGPT Memory Automation 🧠💾

A Streamlit-based personal memory assistant that:

- Stores and manages summaries of your ChatGPT chats
- Allows prompt injection based on local memory files
- Supports keyword search and memory indexing
- Optional summarization via local LLMs or OpenAI API

## Quickstart

1. Clone the repo
2. Create a virtual environment
3. Run `streamlit run app.py`
   """

# 5. Initial Placeholder Code for app.py

app_placeholder = """
import streamlit as st
from config import \*

st.set_page_config(page_title=PROJECT_NAME)

st.title(PROJECT_NAME)
st.write(DESCRIPTION)

st.sidebar.title("📁 Project Profile")
st.sidebar.markdown(f"**Project**: {PROJECT_NAME}")
st.sidebar.markdown(f"**Version**: {VERSION}")
st.sidebar.markdown(f"**Author**: {AUTHOR}")
st.sidebar.markdown(f"**Model**: {'Local - ' + LOCAL_MODEL_NAME if USE_LOCAL_MODEL else 'OpenAI - ' + OPENAI_MODEL}")
st.sidebar.markdown(f"**Summary Format**: {DEFAULT_SUMMARY_FORMAT}")
"""

# 6. Config File: config.py

config_file = """
from pathlib import Path

PROJECT_NAME = "ChatGPT Memory Automation"
VERSION = "0.1"
AUTHOR = "Kazi"
DESCRIPTION = "Streamlit app to manage, summarize, and retrieve ChatGPT memory summaries."

BASE_DIR = Path(**file**).resolve().parent
MEMORY_DIR = BASE_DIR / "memory"
DB_PATH = BASE_DIR / "database" / "memory.db"
ENV_PATH = BASE_DIR / ".env"

USE_LOCAL_MODEL = True
LOCAL_MODEL_NAME = "mistral"
USE_OPENAI = False
OPENAI_MODEL = "gpt-3.5-turbo"

DEFAULT_SUMMARY_FORMAT = "json"
SUMMARY_TAGS = ["project", "goal", "tech", "todo"]
"""

print("Project structure created. Next steps:")
print("1. Create folders and files as listed above")
print("2. Set up your environment with the shell commands")
print("3. Populate README.md and .gitignore")
print("4. Add config.py for your project profile")
print("5. Start developing in app.py")
