# 🎙️ GraphTalk

**GraphTalk** is a natural language interface for querying a **Neo4j movie graph database** using **Gemini Flash** (Google's LLM). It translates English questions into **Cypher queries**, executes them, and now also formats the results into clean, human-friendly answers — all from a simple **Streamlit** interface.

---

## 🚀 Features

- 🔍 Ask natural language questions about your graph data
- 🤖 Translates English into Cypher using **Gemini Flash**
- 🧠 Queries your **Neo4j** movie database with the generated Cypher
- 💬 Uses **Gemini Flash** again to format the raw Neo4j results into natural language
- 🌐 Streamlit-based, easy-to-use web UI

---

## 📂 Project Structure

```text
GraphTalk/
├── main.py               # (Optional CLI entry point)
├── streamlit_app.py      # 🖥️ Streamlit interface
├── core/
│   ├── __init__.py
│   ├── gemini_utils.py   # Gemini API integration (translation + formatting)
│   ├── neo4j_utils.py    # Neo4j driver and query logic
│   └── formatter.py      # (Legacy) result formatting fallback
├── .env                  # Environment variables (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md
```


---

## 📋 Example Questions

You can try these on your Streamlit app:
- Who directed The Matrix?
- What movies did Tom Hanks act in?
- Who are the top 3 most prolific actors by number of movies?
- What movies did Keanu Reeves star in?
- Show me movies that Meg Ryan acted in.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Haftom2323/GraphTalk.git
cd GraphTalk
```
---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Set up your environment variables

### Create a .env file in the root directory and add:

```bash
GEMINI_API_KEY=your_gemini_api_key
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```
---

## Running the App
### Launch the Streamlit web app:

```bash
python -m streamlit run streamlit_app.py
```
--- 
## 🧠 How It Works
1. You ask a question in plain English (e.g., “What movies did Tom Hanks act in?”)

2. Gemini Flash translates your question into a Cypher query.

3. The Cypher is executed on your Neo4j graph database.

4. The raw query result is sent back to Gemini Flash, which generates a natural language response.

5. The answer is displayed clearly in the app.
---

## 🧪 Requirements
- Python 3.9+

- Neo4j running locally or remotely with access credentials

- Gemini API key (Google Generative AI)
