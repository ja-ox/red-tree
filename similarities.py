# -*- coding: utf-8 -*-
"""
Code to:
    
    1. Import UK Biobank data
    2. Select only ICD-10 columns
    3. Compute similarity/distance matrix of disease x disease pairwise
    4. Perform hierarchical clustering on results for dim reduction
"""

import networkx as nx
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean, pdist, squareform

# # Load file
# file = ''
# df = pd.read_csv(file)


n = 1000 # Number of patients
m = 10 # Number of diseases

# Random array of morbidities per patient
data = [np.random.choice([0, 1], size=(m,), p=[0.2, 0.8]) for patient in range(n)]
cols = [f'41270.{i}' for i in range(m)]
df = pd.DataFrame(data, columns = cols)

# Select only ICD-10 columns
mask = df.columns.str.startswith('41270')
df = df[df.columns[mask]]

# Transpose dataframe for easier computing of similarity etc
df = df.T
df.index = cols

## MULTIMORBIDITIES

# Generate Similarity Matrix

def similarity_func(u, v):
    return 1/(1+euclidean(u,v))

similarities = pdist(df, similarity_func) # Similarity measure
dists = pdist(df) # Distance measure
df_euclid = pd.DataFrame(squareform(dists), columns=df.index, index=df.index)

# Generate clusters


# Visualise clusters

## ICD-10 TREE
