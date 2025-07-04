# 🧠 ChatGPT Memory Automation

A personal memory assistant built with **Streamlit** and **SQLite** to manage, store, search, and reuse **summarized ChatGPT conversations** (memory shards).

This app allows you to manually create memory summaries, search them intelligently, and generate prompt starters to resume previous ideas, projects, or conversations efficiently.

---

## 🚀 Features

- ✏️ **Manual Memory Summarization**  
  Summarize important ChatGPT conversations and save them locally as `.md` or `.json`.

- 🗃️ **SQLite Database Indexing**  
  Memory shards are stored and indexed with title, date, tags, purpose, and full summary text.

- 🔍 **Search and Filter Memories**  
  Quickly find relevant memories using keywords or tags.

- 🧠 **Prompt Injection Generator**  
  Generate context-rich prompts from saved memories to resume ChatGPT chats or projects.

- 🛠️ **Streamlit Frontend**  
  User-friendly interface to manage and interact with your personal memory archive.

- 🔄 **Future-Proof Architecture**  
  Designed to evolve: can later support embedding search, full-text indexing (FTS5), and API exposure.

---

## 🏗️ Project Structure

ChatGPT-Memory-Automation/
├── app.py # Main Streamlit app
├── config.py # Project settings and paths
├── memory/ # Memory summary files (.md/.json)
├── database/
│ └── init_db.py # Script to initialize SQLite database
├── utils/ # Utility functions (save, search)
├── assets/ # (Optional) Static assets or icons
├── requirements.txt # Python package dependencies
├── README.md # Project documentation
└── .env # API keys and environment configs

---

## ⚙️ Installation & Setup

1. **Clone the Repository**

```bash
    git clone https://github.com/yourusername/chatgpt-memory-automation.git
    cd chatgpt-memory-automation
```

2. Create a Conda Environment
   conda create -n chatgpt_memory_cleansing python=3.10
   conda activate chatgpt_memory_cleansing

3. Install Required Packages

pip install -r requirements.txt

4. Initialize the Database

python database/init_db.py

5. Run the App

streamlit run app.py

⸻

✏️ How to Create a Memory Shard 1. Select a ChatGPT conversation you want to store. 2. Use the following prompt inside ChatGPT:
“Summarize this conversation as a memory shard. Include: Title, Date, Purpose, Key Points, Next Steps, Tags. Output in clean Markdown format.” 3. Save the output in the /memory folder. 4. Optionally register it into the database via the app or utility functions.

⸻

🔮 Roadmap
• Add Full-Text Search (FTS5) support
• Integrate local embeddings for semantic search
• Build advanced prompt composer
• Optional: expose API endpoints
• Migrate to PostgreSQL if scaling up

⸻

📜 License

MIT License

⸻

🤝 Contributions

Contributions are welcome!
Feel free to open an issue or submit a pull request to expand functionalities, fix bugs, or improve documentation.

⸻

🧠 Philosophy

Build your own Second Brain.
Remember everything. Resume anything. Continue smarter.

⸻

⚡ Ready to Build?

If yes, next step: create and save your first memory shard!

---
