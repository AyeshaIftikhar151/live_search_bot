# 🤖 AI-Powered Live Search Chatbot  
### Built with LangChain • Gemini • Google Search API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Gemini](https://img.shields.io/badge/Gemini-LLM-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-blueviolet)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🌟 Overview

The **Live Search Chatbot** is an AI-powered system that performs **real-time information retrieval** using  
**LangChain**, **Google Gemini**, and the **Google Custom Search JSON API**.  

It merges **RAG (Retrieval-Augmented Generation)** with **live Google search** and **vector database lookups** (Chroma DB)  
to deliver **accurate, context-aware, and up-to-date responses** through a **Streamlit-based chatbot interface**.

---

## ✨ Features

✅ Real-time web search using Google CSE  
✅ Context-aware AI responses via Gemini  
✅ ChromaDB-powered vector storage for knowledge retention  
✅ LangChain pipelines for modular prompt flow  
✅ Beautiful and interactive Streamlit web UI  
✅ Secure `.env` configuration for API keys  

---

## 🧱 Tech Stack

| Component | Description |
|------------|-------------|
| **LangChain** | Orchestrates the chatbot pipeline and prompt logic |
| **Gemini API** | LLM engine for natural, intelligent responses |
| **ChromaDB** | Stores and retrieves embedded document data |
| **Google Custom Search API** | Provides live, up-to-date search results |
| **Streamlit** | Web app front-end for user interaction |
| **Python 3.10+** | Core programming language |

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AyeshaIftikhar151/live_search_bot.git
cd live_search_bot
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv lanchain_env
lanchain_env\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Add Environment Variables
Create a .env file in the project root:

ini
Copy code
GOOGLE_API_KEY=your_gemini_api_key
GOOGLE_CSE_KEY=your_custom_search_api_key
GOOGLE_CX=your_custom_search_engine_id
▶️ Run the Application
Launch the Streamlit web UI:

bash
Copy code
streamlit run webui.py
You’ll see the chatbot running locally in your browser at:
👉 http://localhost:8501

📁 Folder Structure
bash
Copy code
live_search_bot/
│
├── ingest.py               # Data ingestion & embedding script
├── search_bot.py           # Core chatbot logic (LangChain + Gemini)
├── webui.py                # Streamlit web interface
├── chroma_db/              # Vector database storage
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .env                    # API keys (excluded from GitHub)
🚀 Future Enhancements
🌐 Add multi-domain document support

🗣️ Integrate speech-to-text for voice queries

💬 Improve RAG pipeline with semantic reranking

☁️ Deploy to Streamlit Cloud / Hugging Face Spaces

👩‍💻 Author
Ayesha Iftikhar
💼 GitHub Profile
📧 ayesharajabsn@gmail.com

📜 License
This project is licensed under the MIT License – feel free to use and modify it.

⭐ If you found this helpful, please star the repository and share it! ⭐
🌟 Show your support ...!!!

