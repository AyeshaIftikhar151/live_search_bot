🧠 AI-Powered Live Search Chatbot
Using LangChain, Gemini, and Google Search API

An intelligent chatbot that performs real-time searches using Google Programmable Search Engine, Gemini LLM, and LangChain.
It combines RAG (Retrieval-Augmented Generation) with vector-based document retrieval (Chroma DB) to give live, accurate, and context-aware answers.

🚀 Features

🔍 Live Google Search Integration via Custom Search API

🧩 LangChain-powered pipeline for prompt handling & context management

💾 Chroma Vector Database for document embedding and retrieval

💬 Gemini Model for intelligent, conversational responses

🖥️ Streamlit Web UI for interactive chatbot interface

🛠️ Tech Stack
Component	Description
Python 3.10+	Core programming language
LangChain	LLM workflow orchestration
Google Gemini API	AI reasoning & text generation
ChromaDB	Local vector store for embeddings
Streamlit	Frontend web interface
Google CSE (Custom Search JSON API)	Real-time search data
⚙️ Installation & Setup

Clone the Repository

git clone https://github.com/AyeshaIftikhar151/live_search_bot.git
cd live_search_bot


Activate Virtual Environment

conda activate lanchain_env


or if using venv:

python -m venv lanchain_env
lanchain_env\Scripts\activate


Install Dependencies

pip install -r requirements.txt


Create .env File
Inside your project folder, add this file:

GOOGLE_API_KEY=your_gemini_api_key
GOOGLE_CSE_KEY=your_custom_search_api_key
GOOGLE_CX=your_search_engine_id

💡 Run the Project

To start the chatbot web app:

streamlit run webui.py

🧱 Folder Structure
live_search_bot/
│
├── ingest.py               # Script for data ingestion & vector embedding
├── search_bot.py           # Core chatbot logic (LangChain + Gemini)
├── webui.py                # Streamlit web interface
├── chroma_db/              # Vector database storage
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .env                    # API keys (not uploaded to GitHub)

🧭 Future Improvements

🤖 Add multi-domain document retrieval

🗣️ Integrate speech-to-text for voice queries

📚 Expand RAG capabilities using web-based retrievers

☁️ Deploy on Streamlit Cloud or HuggingFace Spaces

📜 License

This project is licensed under the MIT License.

👩‍💻 Author

Ayesha Iftikhar
🌐 GitHub Profile

🌟 Show your support

If you like this project, give it a ⭐ on GitHub!