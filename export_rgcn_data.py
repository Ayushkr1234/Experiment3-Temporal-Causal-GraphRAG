from neo4j import GraphDatabase
import pandas as pd

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j","neo4j123")
)

triples = []

with driver.session() as session:

    result = session.run("""
    MATCH (a)-[r]->(b)
    RETURN
    coalesce(a.name,a.id) AS head,
    type(r) AS rel,
    coalesce(b.name,b.id) AS tail
    """)

    for row in result:
        triples.append([
            row["head"],
            row["rel"],
            row["tail"]
        ])

df = pd.DataFrame(
    triples,
    columns=["head","relation","tail"]
)

df.to_csv(
    "rgcn_triples.csv",
    index=False
)

print(df.shape)

driver.close()