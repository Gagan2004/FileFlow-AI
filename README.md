# 🧠 FileFlow-AI

**FileFlow-AI** is a powerful AI-powered terminal assistant that lets you control your **local file system** using **natural language**. Just describe what you want to do — and it will understand, suggest a terminal command, and run it (safely). Powered by **Groq's blazing-fast LLMs**.

---

## ⚙️ Core Functionality

- 💬 Converts natural prompts like:
  - _“Create 10 folders with random names”_
  - _“Rename all .txt files to .log”_
  - _“Delete the last created folder”_
- 🧠 Uses **Groq API** to generate valid terminal commands
- 🖥️ Executes commands on **Windows (CMD)** only (Linux support coming)
- 🛡️ Built-in **safety filter** to block dangerous commands
- 📝 Automatically logs each prompt, command, and result

---

## 📦 Features

- Interactive assistant powered by LLM
- File & directory-aware logic (coming soon)
- Logs all activity in `logs/session_log.txt`
- Translates Linux-style commands to Windows equivalents
- Modular, clean Python codebase

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/FileFlow-AI.git
cd FileFlow-AI
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Your Groq API Key

Create a `.env` file in the root folder and paste:

```
GROQ_API_KEY=your_groq_api_key_here
```

> 🗝️ Get your key from [https://console.groq.com/docs/quickstart](https://console.groq.com/docs/quickstart)

---

## ▶️ Usage

Run the assistant with:

```bash
python main.py
```

Example interaction:

```text
📝 Your request (or type 'exit'): make 5 folders for each weekday
🤖 Thinking...
🛠️ Suggested Command: mkdir Monday Tuesday Wednesday Thursday Friday
✅ Run this command? (y/n): y
📤 Output: [Command executed successfully]
```

---

## 🧱 Project Structure

```
FileFlow-AI/
├── main.py                 # Main application loop
├── groq_api.py             # API wrapper for Groq model
├── executor_windows.py     # Windows-specific command executor
├── utils.py                # Helpers: clean, safety, parsing
├── logs/
│   └── session_log.txt     # Logs all commands & results
├── .env                    # Your Groq API key (not committed)
├── requirements.txt
└── README.md
```

---

## 🔐 Safety Measures

- Blocks known dangerous commands (`del`, `format`, `shutdown`, etc.)
- All executions require confirmation (`y/n`)
- Logs every interaction for auditability

---

## 🌟 Example Prompts

- `Create 5 folders named after planets`
- `List all text files in this directory`
- `Rename all .log files to .bak`
- `Delete the most recently modified folder`

---



## 🤝 Contributing

PRs, feedback, and feature requests are welcome!  
Please open an issue first to discuss changes.

---

**FileFlow-AI — _Talk to your terminal. Let AI do the typing._**
