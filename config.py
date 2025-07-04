# config.py

from pathlib import Path

# General Project Info
PROJECT_NAME = "ChatGPT Memory Automation"
VERSION = "0.1"
AUTHOR = "Alexandros Samartzis"
DESCRIPTION = (
    "Streamlit app to manage, summarize, and retrieve ChatGPT memory summaries."
)

# Paths
BASE_DIR = Path(__file__).resolve().parent
MEMORY_DIR = BASE_DIR / "memory"
DB_PATH = BASE_DIR / "database" / "memory.db"
ENV_PATH = BASE_DIR / ".env"

# Model Preferences
USE_LOCAL_MODEL = True
LOCAL_MODEL_NAME = "mistral"
USE_OPENAI = False
OPENAI_MODEL = "gpt-4o"

# Defaults
DEFAULT_SUMMARY_FORMAT = "json"
SUMMARY_TAGS = ["project", "goal", "tech", "todo"]
