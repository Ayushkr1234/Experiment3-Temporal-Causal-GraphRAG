import pandas as pd
import torch
from torch_geometric.nn import GATConv

df = pd.read_csv(
    "temporal_triples.csv"
)

entities = sorted(
    list(
        set(df["head"])
        |
        set(df["tail"])
    )
)

entity2id = {
    e:i
    for i,e in enumerate(entities)
}

edge_index = torch.tensor([
    [
        entity2id[h]
        for h in df["head"]
    ],
    [
        entity2id[t]
        for t in df["tail"]
    ]
], dtype=torch.long)

timestamps = torch.tensor(
    df["timestamp"].values,
    dtype=torch.float
)

num_nodes = len(entities)

x = torch.eye(num_nodes)

class TemporalGNN(
    torch.nn.Module
):

    def __init__(self):

        super().__init__()

        self.gat = GATConv(
            num_nodes,
            32,
            heads=1
        )

    def forward(
        self,
        x,
        edge_index
    ):

        return self.gat(
            x,
            edge_index
        )

model = TemporalGNN()

embeddings = model(
    x,
    edge_index
)

print(
    embeddings.shape
)