import pandas as pd
from neo4j import GraphDatabase

# Load Excel
df = pd.read_excel("data/attackmitre.xlsx")

# Neo4j connection
driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4j123")   # replace if your password is different
)

with driver.session() as session:

    for _, row in df.iterrows():

        apt_group = str(row["APT Group Name"])

        techniques = row["Software Techniques"]

        if pd.isna(techniques):
            continue

        # Split techniques by ;
        technique_list = str(techniques).split(";")

        for tech in technique_list:

            tech = tech.strip()

            if tech == "":
                continue

            session.run("""
                MERGE (a:APTGroup {name:$apt})
                MERGE (t:Technique {id:$tech})
                MERGE (a)-[:USES]->(t)
            """,
            apt=apt_group,
            tech=tech)

driver.close()

print("Techniques and relationships created successfully!")