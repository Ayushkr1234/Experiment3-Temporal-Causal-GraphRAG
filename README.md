# Temporal-Causal GraphRAG for Cyber Threat Intelligence Prediction

## Overview

This project implements a Temporal-Causal GraphRAG framework for Cyber Threat Intelligence (CTI) analysis and attack prediction using the MITRE ATT&CK framework, Neo4j Knowledge Graphs, Graph Neural Networks, Knowledge Graph Embeddings, and Large Language Models.

The system extracts threat intelligence entities and relationships from CTI reports, constructs attack knowledge graphs, performs graph-based reasoning, and predicts potential future attacker actions using multiple machine learning and graph learning approaches.

---

## Objectives

* Build a Cyber Threat Intelligence Knowledge Graph using MITRE ATT&CK data.
* Extract entities and relationships from CTI reports using Gemini LLM.
* Store and query attack knowledge in Neo4j.
* Implement GraphRAG-based reasoning for attack prediction.
* Evaluate Knowledge Graph Embedding models.
* Generate graph representations using Graph Neural Networks.
* Explore temporal attack sequence modeling.

---

## Technologies Used

### Programming Language

* Python 3.12

### Database

* Neo4j Community Edition

### Libraries

* pandas
* neo4j
* google-generativeai
* pykeen
* torch
* torch-geometric

### Models Implemented

* Markov Chain
* GraphRAG + Gemini
* TransE
* RotatE
* Relational Graph Convolutional Network (R-GCN)
* Graph Attention Network (GAT)
* Temporal Graph Neural Network (Simplified)

---

## Project Architecture

MITRE ATT&CK Dataset

↓

Knowledge Graph Construction

↓

Neo4j Graph Database

↓

CTI Report Ingestion

↓

Gemini-based Entity & Relation Extraction

↓

Attack Knowledge Graph

↓

GraphRAG Retrieval

↓

Threat Prediction & Analysis

↓

Knowledge Graph Embeddings / Graph Neural Networks

---

## Dataset Information

### MITRE ATT&CK Dataset

The MITRE ATT&CK dataset is used to create the primary cybersecurity knowledge graph.

Statistics:

* Entities: 252
* Relation Types: 12
* Triples: 2415

### Extracted CTI Graph

Statistics:

* Attack Graph Nodes: 15
* Attack Graph Relationships: 13

---

## Implemented Modules

### 1. CTI Extraction

File:

```text
extract_cti.py
```

Functionality:

* Reads CTI reports.
* Uses Gemini LLM to extract:

  * Threat Actors
  * Techniques
  * Vulnerabilities
  * Targets
  * Temporal Expressions
  * Entity Relationship Triples

Output:

```text
output/Extracted_data_1.json
```

---

### 2. Attack Knowledge Graph

File:

```text
attack_kg.py
```

Functionality:

* Imports extracted entities and relationships into Neo4j.
* Creates attack graph nodes and edges.

---

### 3. GraphRAG

File:

```text
graph_rag.py
```

Functionality:

* Retrieves graph context from Neo4j.
* Uses Gemini for reasoning over attack relationships.
* Predicts likely next attacker actions.

Example Prediction:

* Tactic: Discovery
* Technique: T1082 (System Information Discovery)

---

### 4. Markov Chain Model

Functionality:

* Learns attack transitions.
* Predicts likely next attack techniques.

Purpose:

* Baseline attack prediction model.

---

### 5. Knowledge Graph Embedding Models

#### TransE

Files:

```text
train_transe.py
evaluate_transe.py
```

Results:

| Metric  | Value |
| ------- | ----: |
| Hits@1  | 0.000 |
| Hits@3  | 0.022 |
| MRR     | 0.037 |
| Hits@10 | 0.093 |

---

#### RotatE

Files:

```text
train_rotate.py
evaluate_rotate.py
```

Results:

| Metric  | Value |
| ------- | ----: |
| Hits@1  | 0.049 |
| Hits@3  | 0.087 |
| MRR     | 0.102 |
| Hits@10 | 0.181 |

Observation:

RotatE outperformed TransE across all evaluation metrics.

---

### 6. R-GCN

Files:

```text
export_rgcn_data.py
rgcn_model.py
```

Functionality:

* Converts graph triples into graph neural network format.
* Generates node embeddings.

Output:

```text
rgcn_embeddings.csv
```

Embedding Shape:

```text
torch.Size([252, 32])
```

---

### 7. GAT

File:

```text
gat_model.py
```

Functionality:

* Learns attention-based node representations.
* Generates graph embeddings.

Output:

```text
gat_embeddings.csv
```

Embedding Shape:

```text
torch.Size([252, 32])
```

---

### 8. Temporal GNN

Files:

```text
generate_temporal_data.py
temporal_gnn.py
```

Functionality:

* Creates temporal attack sequences.
* Incorporates timestamp information into graph learning.
* Demonstrates temporal attack representation.

Output:

```text
temporal_triples.csv
```

Embedding Shape:

```text
torch.Size([252, 32])
```

---

## Project Structure

```text
experiment3/
│
├── attack_kg.py
├── extract_cti.py
├── graph_rag.py
├── export_triples.py
│
├── train_transe.py
├── evaluate_transe.py
│
├── train_rotate.py
├── evaluate_rotate.py
│
├── export_rgcn_data.py
├── rgcn_model.py
│
├── gat_model.py
│
├── generate_temporal_data.py
├── temporal_gnn.py
│
├── triples.tsv
├── rgcn_triples.csv
├── temporal_triples.csv
│
├── rgcn_embeddings.csv
├── gat_embeddings.csv
│
├── transe_model/
├── rotate_model/
│
└── README.md
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Experiment3-Temporal-Causal-GraphRAG.git
cd Experiment3-Temporal-Causal-GraphRAG
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install pandas
pip install neo4j
pip install google-generativeai
pip install pykeen
pip install torch
pip install torch-geometric
```

---

## Future Work

* Temporal Graph Networks (TGN)
* Dynamic Knowledge Graph Embeddings
* Multi-hop Attack Path Prediction
* Explainable Threat Intelligence Reasoning
* Real-time CTI Stream Processing
* Automated ATT&CK Technique Recommendation

---

## Conclusion

This project demonstrates an end-to-end Cyber Threat Intelligence pipeline integrating Knowledge Graphs, GraphRAG, Large Language Models, Knowledge Graph Embeddings, and Graph Neural Networks. The framework enables extraction, representation, reasoning, and prediction of cyber attack behaviors using ATT&CK-based threat intelligence knowledge.

---

## Author

Ayush Kumar

B.Tech Computer Science and Engineering

SRM University AP
