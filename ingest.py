"""
ingest.py
---------
Ingest documents into ChromaDB using Gemini embeddings.
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader

# Load environment
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def ingest_data(file_path: str, persist_directory: str = "chroma_db"):
    """Load text file, create embeddings, and store in ChromaDB."""
    print("🔍 Loading document...")
    loader = TextLoader(file_path)
    docs = loader.load()

    print("✨ Creating embeddings with Gemini...")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

    print("💾 Storing in ChromaDB...")
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    vectordb.persist()
    print("✅ Ingestion complete! Data saved to", persist_directory)


if __name__ == "__main__":
    ingest_data("sample.txt")
