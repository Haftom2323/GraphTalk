import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

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
