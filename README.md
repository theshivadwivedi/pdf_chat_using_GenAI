# 📄 PDF Chat using GenAI (RAG Application)

An end-to-end **Generative AI application** that allows users to upload a PDF and ask questions based strictly on the document content using **Retrieval Augmented Generation (RAG)**.

Built with **LangChain (LCEL)**, **Gemini LLM**, **Hugging Face Embeddings**, **FAISS**, and a clean **Streamlit UI**.

---

## 🚀 Live Features

- 📤 Upload any PDF document  
- 💬 Ask natural language questions  
- 🧠 Context-aware answers (no hallucination)  
- ⚡ Fast semantic search using vector embeddings  
- 🖥️ Clean UI (no custom CSS)  
- 🔒 Secure API key handling via `.env`

---

## 🧠 How It Works (RAG Pipeline)

**English:**
1. PDF is loaded and split into chunks  
2. Chunks are converted into embeddings  
3. Embeddings are stored in FAISS (vector database)  
4. User query is embedded and matched semantically  
5. Relevant chunks are passed to Gemini LLM  
6. LLM answers strictly from retrieved context  


## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Language | Python |
| LLM | Gemini (Free tier) |
| Framework | LangChain (LCEL) |
| Embeddings | Hugging Face |
| Vector DB | FAISS |
| UI | Streamlit |
| Env Management | python-dotenv |
| Version Control | Git & GitHub |

---

## 📁 Project Structure
pypdf_llm/
│
├── app.py # Streamlit UI
├── pdf_loader.py # PDF loading & chunking
├── vector_store.py # Embeddings & FAISS
├── llm_chain.py # LCEL-based RAG chain
├── config.py # Environment config
├── requirements.txt
├── .gitignore
└── README.md

