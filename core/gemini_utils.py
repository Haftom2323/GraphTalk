import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Translation function
def translate_to_cypher(question: str) -> str:
    prompt = (
        "Translate the following natural language question into a Cypher query.\n"
        "Assume the schema is:\n"
        "(:Person)-[:DIRECTED]->(:Movie), (:Person)-[:ACTED_IN]->(:Movie), "
        "Movie has 'title', Person has 'name'.\n\n"
        f"Natural language: {question}\n"
        "Cypher:"
    )
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.replace("```cypher", "").replace("```", "").strip()

# Rephrasing function
def rephrase_results(question: str, results: list[str]) -> str:
    joined_results = ", ".join(results)

    prompt = (
        "You are an AI assistant helping users understand graph database answers.\n"
        f"Question: {question}\n"
        f"Raw Results: {joined_results}\n\n"
        "Write a clear and conversational answer in natural language. "
        "Avoid listing values with bullets. Make it feel like a helpful response."
    )

    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
