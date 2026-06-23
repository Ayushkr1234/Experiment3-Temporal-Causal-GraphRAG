import pandas as pd
import torch

from torch_geometric.nn import GATConv

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

num_nodes = len(entities)

x = torch.eye(num_nodes)

class GAT(torch.nn.Module):

    def __init__(self):

        super().__init__()

        self.gat1 = GATConv(
            num_nodes,
            64,
            heads=2
        )

        self.gat2 = GATConv(
            128,
            32,
            heads=1
        )

    def forward(
        self,
        x,
        edge_index
    ):

        x = self.gat1(
            x,
            edge_index
        )

        x = torch.relu(x)

        x = self.gat2(
            x,
            edge_index
        )

        return x

model = GAT()

embeddings = model(
    x,
    edge_index
)

import pandas as pd

print(embeddings.shape)

emb_df = pd.DataFrame(
    embeddings.detach().numpy()
)

emb_df.to_csv(
    "gat_embeddings.csv",
    index=False
)

print("GAT embeddings saved")