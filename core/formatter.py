def format_results(results):
    if not results:
        return "No results found."
    output = ""
    for row in results:
        for value in row.values():
            output += f"- {value}\n"
    return output
