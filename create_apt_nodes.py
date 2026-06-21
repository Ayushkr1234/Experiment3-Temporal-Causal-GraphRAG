import pandas as pd
from neo4j import GraphDatabase

df = pd.read_excel("data/attackmitre.xlsx")

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4j123")
)

with driver.session() as session:

    for _, row in df.iterrows():

        apt_group = str(row["APT Group Name"])

        session.run(
            """
            MERGE (a:APTGroup {name:$name})
            """,
            name=apt_group
        )

driver.close()

print("All APT Groups Added")