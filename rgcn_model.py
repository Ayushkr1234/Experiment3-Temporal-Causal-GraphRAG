import pandas as pd
import torch

from torch_geometric.nn import RGCNConv

df = pd.read_csv(
    "rgcn_triples.csv"
)

entities = sorted(
    list(
        set(df["head"])
        |
        set(df["tail"])
    )
)

relations = sorted(
    df["relation"].unique()
)

entity2id = {
    e:i
    for i,e in enumerate(entities)
}

relation2id = {
    r:i
    for i,r in enumerate(relations)
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

edge_type = torch.tensor([
    relation2id[r]
    for r in df["relation"]
], dtype=torch.long)

num_nodes = len(entities)
num_relations = len(relations)

x = torch.eye(num_nodes)

class RGCN(torch.nn.Module):

    def __init__(self):

        super().__init__()

        self.conv1 = RGCNConv(
            num_nodes,
            64,
            num_relations
        )

        self.conv2 = RGCNConv(
            64,
            32,
            num_relations
        )

    def forward(
        self,
        x,
        edge_index,
        edge_type
    ):

        x = self.conv1(
            x,
            edge_index,
            edge_type
        )

        x = torch.relu(x)

        x = self.conv2(
            x,
            edge_index,
            edge_type
        )

        return x

model = RGCN()

embeddings = model(
    x,
    edge_index,
    edge_type
)

import pandas as pd

print(embeddings.shape)

emb_df = pd.DataFrame(
    embeddings.detach().numpy()
)

emb_df.to_csv(
    "rgcn_embeddings.csv",
    index=False
)

print("R-GCN embeddings saved")