from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "neo4j123")
)

with driver.session() as session:
    session.run("""
        CREATE (a:APTGroup {
            name:'APT30'
        })
    """)

print("Node Created Successfully")

driver.close()