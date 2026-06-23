from neo4j import GraphDatabase
import google.generativeai as genai

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4j123")
)

question = """
What is the likely next attack technique after PowerShell execution by Patchwork?
"""

with driver.session() as session:

    result = session.run("""
    MATCH p=(a)-[r]->(b)
    RETURN
coalesce(a.name,a.id) AS source,
type(r) AS relation,
coalesce(b.name,b.id) AS target
    LIMIT 100
    """)

    context = ""

    for row in result:
        context += (
            f"{row['source']} "
            f"{row['relation']} "
            f"{row['target']}\n"
        )

prompt = f"""
You are a cybersecurity GraphRAG analyst.

Question:
{question}

Graph Context:
{context}

Answer:
1. Likely next tactic
2. Likely next technique
3. Confidence
4. Evidence
"""

response = model.generate_content(prompt)

print(response.text)

driver.close()