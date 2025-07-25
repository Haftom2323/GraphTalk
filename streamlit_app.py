import streamlit as st
import random

from core.gemini_utils import translate_to_cypher
from core.neo4j_utils import query_neo4j
from core.formatter import format_results

st.set_page_config(page_title="GraphTalk", layout="centered")

st.title("GraphTalk")
st.markdown(
    """
    Ask natural language questions about your **Neo4j movie database** using Gemini + Neo4j.
    """
)

examples = [
    "Who directed The Matrix?",
    "What movies did Tom Hanks act in?",
    "Who are the top 3 most prolific actors by number of movies?",
    "Which movies did Tom Hanks act in?",
    "What movies did Keanu Reeves star in?",
    "Show me movies that Meg Ryan acted in?"
]

with st.expander("Need inspiration?"):
    st.write("Try one of these example questions:")
    st.code(random.choice(examples))


question = st.text_input("Ask your question", placeholder="e.g., Who directed The Matrix?")

if st.button("Ask") and question.strip():
    with st.spinner("Translating to Cypher and querying Neo4j..."):
        try:
            cypher = translate_to_cypher(question)
            results = query_neo4j(cypher)
            answer = format_results(results)

        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    st.markdown("**Generated Cypher Query:**")
    st.code(cypher, language="cypher")

    if answer.strip():
        st.success("Here's what I found:")
        st.markdown(answer.replace("-", "•"))
    else:
        st.warning("No results found for this query.")

elif question.strip() == "":
    st.info("Type your question and press **Ask**")
