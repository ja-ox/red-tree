# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:22:50 2020

@author: Jacob
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from scipy.cluster.hierarchy import dendrogram

# Initialise graph
G=nx.Graph()

# Load file
#url = 'https://biobank.ctsu.ox.ac.uk/crystal/coding.cgi?id=19&nl=1'
dir = Path(r"C:\Users\Jacob\Downloads\autoencoders")
file = dir / "coding19.tsv"

# Load file as dataframe
df = pd.read_csv(file, sep='\t')

# REDUCED DF
#df = df[df['coding'].str.contains('A')]

# Generate nodes and edges from file
#nodes = set(df['node_id'].unique())
edges = list(zip(df['node_id'], df['parent_id']))

# Add edges to graph
#G.add_nodes_from(nodes, color = 'blue')
G.add_edges_from(edges)

G2 = nx.Graph()
G2.add_edges_from([edge for edge in G.edges if 0 not in edge])

#%%

# Use radial tree representation
pos = graphviz_layout(G, prog='twopi', root=0, args='')

#%%

# Plot graph
fig, axes = plt.subplots(nrows=6, ncols=4, sharey=True, sharex=True,
                         figsize=(16,24))
ax = axes.flatten()

for j, c in enumerate(nx.connected_components(G2)):
    root = min(c)
    edges = set([edge for edge in G2.edges for node in c if node in edge])
    graph = nx.Graph()
    graph.add_edges_from(edges)
    pos = graphviz_layout(graph, prog='twopi', root=root, args='')
    
    nx.draw(graph, pos, node_size=2, alpha=0.5, node_color="#00B7EB", 
            with_labels=False, ax=ax[j])
    ax[j].set_axis_off()

timestamp = datetime.now().strftime("%d-%b-%Y-%H%M%S)")
# Save figure
#plt.axis('equal')
plt.savefig(dir / f"plot_{timestamp}.png", dpi=500)
plt.show()
