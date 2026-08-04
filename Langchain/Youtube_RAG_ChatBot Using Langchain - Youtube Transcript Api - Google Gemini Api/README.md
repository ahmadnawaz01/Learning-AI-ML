# 📺 YouTube Video RAG Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **LangChain**, **Google Gemini**, and **FAISS**. This application enables users to enter any YouTube video URL and interact with the video's transcript through natural language conversations.

Instead of manually searching through long videos, the chatbot retrieves the most relevant transcript segments using semantic search and provides context-aware answers powered by Google Gemini. Users can summarize videos, ask detailed questions, clarify concepts, and explore video content interactively.

---

# ✨ Features

- 🎥 Process any YouTube video using its URL
- 📝 Automatically extract video transcripts
- 🔍 Semantic search using FAISS vector database
- 🤖 AI-powered question answering with Google Gemini
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Interactive chat interface built with Streamlit
- ⚡ Fast responses through cached vector embeddings
- 🔄 Streaming responses using LangChain LCEL
- 🧠 Context-aware answers instead of hallucinated responses
- 💾 Persistent chat history using Streamlit Session State

---
# ⚠️ Deployment Note

This project relies on **youtube-transcript-api**, which fetches transcripts by making unauthenticated HTTP requests to YouTube.

Cloud hosting providers (such as Streamlit Community Cloud, AWS, Google Cloud, or Vercel) often use shared data-centre IP addresses that may be blocked by YouTube's anti-bot systems.

As a result, transcript retrieval can fail with errors such as:

```
RequestBlocked

Could not retrieve a transcript
```

For the most reliable experience, run the application locally using your residential internet connection.

---

# 🚀 Demo Workflow

1. Paste a YouTube video URL.
2. Click **Process Video**.
3. The application:
   - Extracts the transcript.
   - Splits it into meaningful chunks.
   - Converts chunks into vector embeddings.
   - Stores them inside a FAISS vector database.
4. Ask questions naturally.
5. The chatbot retrieves the most relevant transcript chunks and generates accurate answers using Google Gemini.

---

# 🏗️ Project Architecture

```
                  ┌──────────────────────────────┐
                  │      Streamlit App UI        │
                  │           app.py            │
                  └──────────────┬──────────────┘
                                 │
                    YouTube URL / Chat Input
                                 ▼
┌──────────────────────────────────────────────────────────────┐
│                   RAG Pipeline (rag_pipeline.py)             │
│                                                              │
│ Transcript → Text Splitter → Embeddings → FAISS Retriever    │
└──────────────────────────────────────────────────────────────┘
                                 │
                          Retrieved Context
                                 ▼
                    Prompt Template (LangChain)
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │     Google Gemini LLM        │
                  │    Streaming Response        │
                  └──────────────────────────────┘
```

---

# 📂 Project Structure

```
youtube-rag-chatbot/
│
├── app.py
├── rag_pipeline.py
├── utils.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

# ⚙️ How It Works

## 1. Transcript Extraction

The application uses **youtube-transcript-api** to retrieve the transcript directly from YouTube without requiring the official YouTube Data API.

The transcript is downloaded and converted into a single document that serves as the knowledge base for the chatbot.

---

## 2. Document Chunking

Large transcripts cannot be sent directly to the language model due to context limitations.

To solve this, the transcript is divided using:

- RecursiveCharacterTextSplitter

Configuration:

- Chunk Size: **1000**
- Chunk Overlap: **200**

This preserves semantic continuity between chunks while keeping them within the model's context window.

---

## 3. Embedding Generation

Each transcript chunk is converted into a high-dimensional vector representation using:

**Google Gemini Embeddings**

```
gemini-embedding-2
```

These embeddings capture the semantic meaning of text rather than exact keyword matches.

---

## 4. Vector Database

The generated embeddings are stored locally using:

**FAISS (Facebook AI Similarity Search)**

Benefits:

- Extremely fast similarity search
- Lightweight
- No external database required
- Efficient retrieval for large transcripts

---

## 5. Retrieval-Augmented Generation (RAG)

When the user asks a question:

1. The question is embedded.
2. FAISS finds the most relevant transcript chunks.
3. Retrieved context is inserted into the prompt.
4. Google Gemini generates an answer using only the retrieved context.

This significantly reduces hallucinations and improves factual accuracy.

---

## 6. LangChain LCEL Pipeline

The application uses the **LangChain Expression Language (LCEL)** to create a modular RAG pipeline.

Pipeline flow:

```
Question
      │
      ▼
Retriever
      │
      ▼
Retrieved Documents
      │
      ▼
Prompt Template
      │
      ▼
Google Gemini
      │
      ▼
Streaming Response
```

---

# 🧩 Components

## app.py

Responsible for:

- Streamlit UI
- Sidebar controls
- Chat interface
- Session management
- Caching
- User interaction

Uses:

- `st.session_state`
- `@st.cache_resource`

to avoid rebuilding embeddings every time the page refreshes.

---

## rag_pipeline.py

Implements the complete Retrieval-Augmented Generation pipeline.

Responsibilities:

- Transcript extraction
- Document loading
- Text chunking
- Embedding generation
- FAISS indexing
- Retriever configuration
- Prompt template
- Gemini integration
- Streaming responses

---

## utils.py

Contains helper functions.

### get_video_id(url)

Extracts video IDs from multiple YouTube URL formats:

- youtube.com/watch?v=
- youtu.be/
- youtube.com/embed/
- mobile URLs

---

### format_docs()

Formats retrieved LangChain documents into a clean context string before sending them to Gemini.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| Google Gemini | LLM |
| Gemini Embeddings | Vector Embeddings |
| FAISS | Vector Database |
| youtube-transcript-api | Transcript Extraction |
| python-dotenv | Environment Variables |

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/ahmadnawaz01/Youtube_RAG_ChatBot-Using-Langchain---Youtube-Transcript-Api---Google-Gemini-Api.git

cd youtube-rag-chatbot
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv myvenv

myvenv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv myvenv

source myvenv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=your_gemini_api_key
```

You can obtain a free API key from **Google AI Studio**.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Paste a YouTube URL and start chatting.

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Large Language Models (LLMs)
- LangChain Expression Language (LCEL)
- Prompt Engineering
- Streamlit Application Development
- FAISS Vector Databases
- Google Gemini Integration
---

# 👨‍💻 Author

**Ahmad Nawaz**

BS Computer Science  
University of Central Punjab (UCP), Lahore

GitHub: [https://github.com/ahmadnawaz01](https://github.com/ahmadnawaz01)

LinkedIn: [https://linkedin.com/in/your-linkedin-profile](https://www.linkedin.com/in/ahmad-nawaz-0099cs)

---

⭐ If you found this project useful, consider giving it a star!
