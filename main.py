from core.gemini_utils import translate_to_cypher
from core.neo4j_utils import query_neo4j
from core.formatter import format_results

def answer_user_question(question: str):
    print(f"\n Question: {question}")
    cypher = translate_to_cypher(question)
    print(f"\n Cypher Query:\n{cypher}")
    results = query_neo4j(cypher)
    print(f"\n Raw Results:\n{results}")
    answer = format_results(question, results)
    print(f"\n Answer:\n{answer}")

if __name__ == "__main__":
    while True:
        user_question = input("Ask a movie-related question (or type 'exit'): ")
        if user_question.lower() == 'exit':
            break
        answer_user_question(user_question)
