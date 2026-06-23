from neo4j import GraphDatabase
import pandas as pd

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4j123")
)

with driver.session() as session:

    result = session.run("""
    MATCH (a)-[r]->(b)
    RETURN
    coalesce(a.name,a.id) AS head,
    type(r) AS relation,
    coalesce(b.name,b.id) AS tail
    """)

    triples = []

    for row in result:
        triples.append([
            row["head"],
            row["relation"],
            row["tail"]
        ])

df = pd.DataFrame(
    triples,
    columns=["head","relation","tail"]
)

df.to_csv(
    "triples.tsv",
    sep="\t",
    index=False,
    header=False
)

print("Triples exported:", len(df))

driver.close()