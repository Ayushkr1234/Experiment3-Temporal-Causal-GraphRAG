from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "neo4j123"   # use the password you chose

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

with driver.session() as session:
    result = session.run(
        "RETURN 'Neo4j Connected Successfully' AS message"
    )

    for record in result:
        print(record["message"])

driver.close()