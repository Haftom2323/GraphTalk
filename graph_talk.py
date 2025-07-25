from neo4j import GraphDatabase
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Neo4j credentials from .env
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Google Gemini setup
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Translate natural language to Cypher
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

    # Clean the response
    query = response.text.strip()
    query = query.replace("```cypher", "").replace("```", "").strip()
    return query


# Query Neo4j
def query_neo4j(cypher_query: str):
    results = []
    with driver.session() as session:
        data = session.run(cypher_query)
        for record in data:
            results.append(dict(record))
    return results

# Format results
def format_results(results):
    if not results:
        return "No results found."
    output = "Results:\n"
    for row in results:
        for value in row.values():
            output += f"- {value}\n"
    return output


# Master function
def answer_user_question(question: str):
    print(f"\n🔍 Question: {question}")
    cypher = translate_to_cypher(question)
    print(f"\n🧾 Cypher Query:\n{cypher}")
    results = query_neo4j(cypher)
    print(f"\n📦 Raw Results:\n{results}")
    answer = format_results(results)
    print(f"\n💬 Answer:\n{answer}")

# Example
answer_user_question("Who directed The Matrix?")
