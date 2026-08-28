# 🤖 Aura — AI Personal Assistant

> **Your intelligent assistant for tasks, emails, calendar, notes, expenses, and web search — powered by AI and automation.**

Aura is an **AI-powered personal assistant** built with **n8n, Google Gemini, and Google Workspace**. It understands natural-language commands and automatically selects the right tool to complete the task.

---

## ✨ What Can Aura Do?

| 🧩 Feature        | ⚡ Capability                       |
| ----------------- | ---------------------------------- |
| ✅ **Tasks**       | Create, view & delete Google Tasks |
| 📅 **Calendar**   | Create & retrieve events           |
| 📧 **Gmail**      | Send & retrieve emails             |
| 📝 **Notes**      | Create, read & update Google Docs  |
| 💰 **Expenses**   | Track expenses in Google Sheets    |
| 🌐 **Web Search** | Search the web with SerpApi        |
| 🧮 **Calculator** | Perform accurate calculations      |
| 🧠 **Memory**     | Maintain conversation context      |

---

## 🏗️ How It Works

```text
              👤 User
                │
                ▼
        ┌───────────────┐
        │    Webhook    │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │   🤖 Aura     │
        │   AI Agent    │
        └───────┬───────┘
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
     Google   Google    Gmail
    Calendar  Tasks
        │       │
        ├───────┼────────┐
        ▼       ▼        ▼
      Docs    Sheets   Search
                         │
                         ▼
                    Calculator
                │
                ▼
        ┌───────────────┐
        │   Response    │
        └───────────────┘
```

---

## 🛠️ Tech Stack

**AI & Automation**

* 🤖 n8n
* 🧠 Google Gemini 3.1 Flash Lite
* 💾 n8n Simple Memory

**Integrations**

* 📅 Google Calendar
* 📧 Gmail
* ✅ Google Tasks
* 📝 Google Docs
* 📊 Google Sheets
* 🔎 SerpApi

**Frontend**

* 🎨 Streamlit
* 🐍 Python

---

# 🚀 Setup & Execution

## 1️⃣ Start n8n with Docker

Create persistent storage:

```bash
docker volume create n8n_data
```

Run n8n:

```bash
docker run -d --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

Open:

**http://localhost:5678**

---

## 2️⃣ Import Aura Workflow

In n8n:

**Workflows → Import from File**

Import:

```text
N8N Project - Personal Assistant Workflow (1).json
```

Configure the required credentials:

* 🔑 Google Gemini API
* 🔎 SerpApi
* 🔐 Google Workspace OAuth2

  * Google Tasks
  * Google Calendar
  * Gmail
  * Google Sheets
  * Google Docs

Then:

**Save → Activate**

---

## 3️⃣ Configure the Webhook

The workflow expects a **POST** request.

Your `.env` file should contain:

```env
N8N_WEBHOOK_URL="http://localhost:5678/webhook/your-webhook-id"
```

Example request:

```json
{
  "name": "Create a task to learn MongoDB",
  "sessionId": "user_session_12345"
}
```

---

# 🎨 Run the Streamlit Frontend

Create a virtual environment:

```bash
python -m venv venv
```

### Windows CMD

```bash
venv\Scripts\activate
```

### PowerShell

```bash
.\venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install streamlit requests python-dotenv
```

Create `.env`:

```env
N8N_WEBHOOK_URL="http://localhost:5678/webhook/your-webhook-id"
```

Start Aura:

```bash
streamlit run app.py
```

Open:

**http://localhost:8501**

---

# 💬 Example Commands

```text
"Create a task to learn DSA."

"Schedule a meeting tomorrow at 3 PM."

"Send an email to my supervisor."

"Add 500 to my food expenses."

"Create a note about Machine Learning."

"Search for the latest AI news."

"Calculate 25% of 50000."
```

---

## 🔐 Security

> ⚠️ **Never commit API keys, OAuth credentials, tokens, or `.env` files to GitHub.**

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

---

## 📌 Project Status

🚧 **In Development**

Built with ❤️ using **n8n + Google Gemini + Google Workspace**

### ⭐ Aura

**Think it. Ask it. Automate it.**
