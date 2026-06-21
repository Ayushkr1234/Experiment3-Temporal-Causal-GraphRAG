import json
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4j123")
)

with open(
    "output/Extracted_data_1.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

triples = data["threat_intelligence"]["entity_relation_triples"]

with driver.session() as session:

    for triple in triples:

        head = triple["subject"]
        relation = triple["predicate"]
        tail = triple["object"]

        relation = relation.upper().replace(" ", "_")

        query = f"""
        MERGE (h:Entity {{name:$head}})
        MERGE (t:Entity {{name:$tail}})
        MERGE (h)-[:{relation}]->(t)
        """

        session.run(
            query,
            head=head,
            tail=tail
        )

driver.close()

print("Attack Knowledge Graph Created")