# Temporal-Causal GraphRAG Reasoning and Next-TTP Prediction for Cyber Threat Intelligence

## Project Overview

This project implements a Cyber Threat Intelligence (CTI) pipeline that combines Knowledge Graphs, Neo4j, Google Gemini, GraphRAG, and Markov Chain based prediction to analyze attack patterns and predict future attacker behavior.

The objective is to extract threat intelligence from CTI reports, represent the information as a Knowledge Graph, and perform reasoning to predict likely future attack techniques (TTPs).

---

## Technologies Used

* Python 3.12
* Neo4j Graph Database
* Pandas
* Google Gemini API
* MITRE ATT&CK Dataset
* GraphRAG
* Markov Chain Model
* Git & GitHub

---

## Dataset Used

### 1. Attackmitre.xlsx

Contains:

* APT Group Names
* Software Techniques
* Software IDs
* References

Used to build the APT Knowledge Graph.

### 2. MitreEnterprise.xlsx

Contains MITRE ATT&CK entities such as:

* Techniques
* Threat Groups
* Malware
* Software
* Descriptions
* Examples

Used as ATT&CK reference data.

---

## Project Workflow

### Phase 1: APT Knowledge Graph Creation

The Attackmitre dataset was processed using Python and Pandas.

Nodes Created:

* APT Groups
* Techniques

Relationships Created:

* USES

Example:

APT30 → USES → T1059

Results:

* 76 APT Group Nodes
* 164 Technique Nodes
* 2402 USES Relationships

Stored in Neo4j.

---

### Phase 2: CTI Report Processing

A sample CTI report was created and processed using Google Gemini.

Extracted Information:

* Threat Actors
* Tools
* Vulnerabilities
* ATT&CK Tactics
* ATT&CK Techniques
* Targets
* Temporal Expressions
* Entity Relationship Triples
* Confidence Scores

Output generated:

Extracted_data_1.json

---

### Phase 3: Attack Knowledge Graph Creation

The extracted JSON file was parsed and inserted into Neo4j.

Nodes Created:

* Threat Actors
* Tools
* Vulnerabilities
* Targets
* Time Entities

Relationships Created:

* USED
* EXPLOITED
* ESTABLISHED
* EXFILTRATED_TO
* OCCURRED_IN

Results:

* 13 Entity Nodes
* 9 Relationships

---

### Phase 4: GraphRAG Reasoning

Graph data was retrieved from Neo4j and provided to Gemini as contextual information.

GraphRAG Workflow:

Neo4j Graph → Retrieval → Gemini Reasoning → Predicted Next TTP

Example Query:

"What is the likely next attack technique after PowerShell execution?"

Example Prediction:

* Likely Tactic: Discovery
* Likely Technique: T1082 (System Information Discovery)

---

### Phase 5: Next-TTP Prediction

A Markov Chain model was implemented to predict the next attack tactic based on observed attack sequences.

Example:

Execution → Persistence → Discovery

Given:

Execution → Persistence

Predicted:

Discovery

---

## Implemented Models

### Implemented

* Markov Chain
* LLM-only (Google Gemini)
* GraphRAG

### Proposed / Future Work

The following models were identified in the project specification but were not fully implemented due to time constraints:

* TransE
* RotatE
* GAT
* R-GCN
* Temporal GNN

These models can be integrated in future versions to improve link prediction and temporal reasoning.

---

## Project Structure

```text
experiment3/
│
├── data/
│   ├── Attackmitre.xlsx
│   └── MitreEnterprise.xlsx
│
├── reports/
│   └── report1.txt
│
├── output/
│   └── Extracted_data_1.json
│
├── create_apt_nodes.py
├── create_techniques.py
├── extract_cti.py
├── attack_kg.py
├── graph_rag.py
├── markov_prediction.py
└── README.md
```

## Key Achievements

✔ Created an APT Knowledge Graph using MITRE ATT&CK data

✔ Extracted CTI entities and relationships using Google Gemini

✔ Generated Attack Knowledge Graph in Neo4j

✔ Implemented GraphRAG-based reasoning

✔ Implemented Markov Chain based Next-TTP prediction

✔ Stored all graph data inside Neo4j

✔ Managed project using Git and GitHub

---

## Conclusion

This project demonstrates an end-to-end Cyber Threat Intelligence pipeline that integrates Knowledge Graphs, Neo4j, Large Language Models, and GraphRAG techniques for threat analysis and attack prediction. The system successfully extracts intelligence from CTI reports, builds graph representations, performs reasoning, and predicts future attack behavior.
