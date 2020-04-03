# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:22:50 2020

@author: Jacob
"""

import networkx as nx
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Importing libraries for graph visualisation
try:
    import pygraphviz
    from networkx.drawing.nx_agraph import graphviz_layout
except ImportError:
    try:
        import pydot
        from networkx.drawing.nx_pydot import graphviz_layout
    except ImportError:
        raise ImportError("This example needs Graphviz and either "
                          "PyGraphviz or pydot")

# Initialise graph
G=nx.Graph()

# Load file
#url = 'https://biobank.ctsu.ox.ac.uk/crystal/coding.cgi?id=19&nl=1'
dir = Path(r"C:\Users\Jacob\Downloads")
file = dir / "coding19.tsv"

# Load file as dataframe
df = pd.read_csv(file, sep='\t')

# Generate nodes and edges from file
nodes = set(df['node_id'].unique())
edges = list(zip(df['node_id'], df['parent_id']))

# Add edges to graph
G.add_nodes_from(nodes, color = 'blue')
G.add_edges_from(edges)

# Plot graph
n = 20
plt.figure(figsize=(n,n))
pos = graphviz_layout(G, prog='twopi', args='')
nx.draw(G, pos, node_size=1, alpha=0.5, node_color="blue", with_labels=False)
plt.axis('equal')
# Save figure
plt.savefig(dir / "plot.png", dpi=2000)
plt.show()
