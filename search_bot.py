"""
search_bot.py
--------------
High-accuracy live search chatbot using:
- Google Custom Search API
- Gemini-2.5-flash
- Conflict detection and reasoning
- System date fallback for time-sensitive queries
"""

import os
import requests
import datetime
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_KEY = os.getenv("GOOGLE_CSE_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    google_api_key=GOOGLE_API_KEY
)

def google_search(query, num_results=5):
    """
    Perform Google Custom Search and return a list of formatted search results
    including title, snippet, and source link.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": GOOGLE_CSE_KEY, "cx": GOOGLE_CX, "q": query, "num": num_results}
    response = requests.get(url, params=params)
    results = response.json()

    formatted_results = []
    if "items" in results:
        for item in results["items"]:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            formatted_results.append(f"{title}\n{snippet}\nSource: {link}")
    else:
        formatted_results.append("No results found.")
    return formatted_results

def live_search_chatbot(question: str) -> str:
    """
    Fetch Google search results and generate a high-accuracy answer with Gemini.
    Detects conflicts, uses system date, and includes sources.
    """
    search_results = google_search(question)
    context = "\n".join(search_results)
    today = datetime.datetime.now().strftime("%A, %B %d, %Y")

    prompt = f"""
You are a highly accurate assistant. Use the Google search results below.

System date: {today}

Search Results:
{context}

Instructions:
- Detect and explain contradictions in results.
- Prefer authoritative sources and mention them.
- For date/time questions, trust the system date.
- If the question is logically contradictory, explain why.
- Give concise, clear answers and include sources.

User Question: {question}
"""
    response = llm.invoke(prompt)
    return response.content

# -----------------------
# Optional CLI testing
# -----------------------
if __name__ == "__main__":
    print("🤖 High-Accuracy Live Search Bot Ready! (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        answer = live_search_chatbot(user_input)
        print("Bot:", answer)
