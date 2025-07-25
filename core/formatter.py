from core.gemini_utils import rephrase_results

def format_results(question: str, results: list) -> str:
    if not results:
        return "No results found."

    flat_results = []
    for row in results:
        for value in row.values():
            flat_results.append(str(value))

    return rephrase_results(question, flat_results)
