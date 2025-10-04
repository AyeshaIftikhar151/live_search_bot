# 🧠 Live Search Bot
An AI chatbot using LangChain + Gemini + Google Custom Search API for real-time RAG-based responses.

## Features
- Live Google search integration
- Gemini-2.5-flash model for responses
- Optional Chroma vector database for private data
- Modular design (ingest, search, webui)

## Run locally
```bash
conda create -n lanchain_env python=3.10 -y
conda activate lanchain_env
pip install -r requirements.txt
python webui.py
