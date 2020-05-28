# -*- coding: utf-8 -*-
"""
Script to plot ICD-10 disease classification tree.
"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import pickle
from pathlib import Path
from datetime import datetime

import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import SpectralClustering
import plotly.graph_objects as go


def main(plot_subtrees, prog='twopi', save_fig=True, similarity_edges=None, include_root=False):
    # Initialise graph
    G=nx.Graph() #DiGraph()
    
    # Load file
    #url = 'https://biobank.ctsu.ox.ac.uk/crystal/coding.cgi?id=19&nl=1'
    dir = Path(r"C:\Users\Jacob\Downloads\autoencoders")
    file = dir / "coding19.tsv"
    
    # Load file as dataframe
    df = pd.read_csv(file, sep='\t')
    
    # Generate nodes and edges from file
    edges = list(zip(df['parent_id'], df['node_id']))
    
    # Add edges to graph
    if include_root:
        G.add_edges_from(edges)
    else:
        G.add_edges_from([edge for edge in edges if 0 not in edge])
    
    
    if plot_subtrees:
        # Create unrooted subtrees
        G2 = nx.Graph()
        G2.add_edges_from([edge for edge in G.edges if 0 not in edge])
    
        # Plot graph
        fig, axes = plt.subplots(nrows=6, ncols=4, sharey=True, sharex=True, figsize=(16,24))
        ax = axes.flatten()
        
        for j, c in enumerate(nx.connected_components(G2)):
            root = min(c)
            edges = set([edge for edge in G2.edges for node in c if node in edge])
            graph = nx.Graph()
            graph.add_edges_from(edges)
            pos = graphviz_layout(graph, prog=prog, root=root, args='')
            
            nx.draw(graph, pos, node_size=2, alpha=0.5, node_color="#00B7EB", 
                    with_labels=False, ax=ax[j], arrowstyle='-')
            ax[j].set_axis_off()
    
    else:
        # Use radial tree representation
        pos = graphviz_layout(G, prog=prog, root=0, args='')
        #nx.draw(G, pos, node_size=0.5, alpha=0.5, node_color="#00B7EB", 
        #        with_labels=False, arrowstyle='-')
    
    if similarity_edges:
        G = add_similarity_edges(G, similarity_edges, df)
    
    timestamp = datetime.now().strftime("%d-%b-%Y-%H%M%S)")
    
    # Save figure
    if save_fig:
        plt.savefig(dir / f"plot_{timestamp}.png", dpi=2000, figsize=(120,20))
    plt.show()
    
    return G, pos, df

def plot_plotly(G, pos, df, similarity_edges=None, plot_tree_edges=True):
    
    # Edge positions
    edge_x = []
    edge_y = []
    
    if plot_tree_edges:
        for edge in G.edges():
            x0, y0 = G.nodes[edge[0]]['pos']
            x1, y1 = G.nodes[edge[1]]['pos']
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
        
    # Labels
    node_dict = df[['coding','node_id']].set_index('coding').to_dict()
    node_dict['node_id'][0] = '' # Adding root label
        
    if False:
        for edge in similarity_edges:
            x0, y0 = G.nodes[node_dict['node_id'][edge[0]]]['pos']
            x1, y1 = G.nodes[node_dict['node_id'][edge[1]]]['pos']
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')
    
    # Node positions
    
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)
        
    if similarity_edges:
        title = 'Cluster'
    else:
        title = 'Number of children'
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='Rainbow',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title=title,
                xanchor='left',
                titleside='right'
            ),
            line_width=2))
    
    # Labels
    label_dict = df[['node_id','coding']].set_index('node_id').to_dict()
    label_dict['coding'][0] = '' # Adding root label
    node_text = [label_dict['coding'][node] for node in G.nodes()]
    node_trace.text = node_text
    
    # Colourings
    if True: # colour nodes based on cluster membership
        node_trace.marker.color = cluster(G) #node_adjacencies
        
    else: # colour based on number of children
        node_adjacencies = []

        for adjacencies in G.adjacency():
            node_adjacencies.append(len(adjacencies[1]) - 1)
        node_trace.marker.color = cluster(G) #node_adjacencies
            
    # Figure
    fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                    title='<br>ICD-10 Tree',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="Python code: <a href='https://ja-ox.github.io/red-tree/'> https://ja-ox.github.io/red-tree/</a>",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    
    fig.write_html(r'C:\Users\Jacob\Downloads\autoencoders\icd10_tree.html', auto_open=True)
    #fig.show()

    return fig

def add_similarity_edges(G, similarity_edges, df):
    
    node_dict = df[['coding','node_id']].set_index('coding').to_dict()
    node_dict['node_id'][0] = '' # Adding root label
    
    for edge in similarity_edges:
        G.add_edge(node_dict['node_id'][edge[0]],
                   node_dict['node_id'][edge[1]])
        #G.add_edge(node_dict['node_id'][edge[1]],
        #           node_dict['node_id'][edge[0]])
        
    return G
    
def cluster(G):
    """
    Given a graph G, performs spectral clustering on the nodes.
    """
    adjacency_matrix = nx.to_numpy_matrix(G)
    sc = SpectralClustering(50, affinity='precomputed', n_init=100, assign_labels='discretize')
    sc.fit_predict(adjacency_matrix)
    
    return sc.labels_
    
if __name__ == "__main__":
    
    dir = Path(r"C:\Users\Jacob\Downloads\autoencoders")
    
    with open(dir / 'data' / 'similarity_edges.txt', 'rb') as fp:
        similarity_edges = pickle.load(fp)
        
    G, pos, df = main(plot_subtrees=False, prog='dot', similarity_edges=similarity_edges) #prog='dot' #dendrogram-ish tree
    
    for n, p in pos.items():
        G.node[n]['pos'] = p
        
    fig = plot_plotly(G, pos, df, similarity_edges=similarity_edges)
    
    # Plot
    
    ### CHANGE BACK TO DIGRAPH IF APPROPRIATE
