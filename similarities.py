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
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

n = 1000 # Number of patients
m = 10 # Number of diseases

# Simulated data - random array of morbidities per patient
simulate = False

if simulate:
    data = [np.random.choice([0, 1], size=(m,), p=[0.2, 0.8]) for patient in range(n)]
    cols = [f'41270.{i}' for i in range(m)]
    df = pd.DataFrame(data, columns = cols)
else:
    ## Load file
    file = r'C:\Users\Jacob\Downloads\autoencoders\data\ukb_latest-ICD10-onehot.tsv'
    df = pd.read_csv(file, sep='\t', nrows=100)
    cols = df.columns
    

# Select only ICD-10 columns
mask = df.columns.str.startswith('41270')
df = df[df.columns[mask]]

#%%

# Renaming columns
col_dict_file = r'C:\Users\Jacob\Downloads\autoencoders\data\ukb_latest-ICD10-onehot_icd10_map.txt'
df_dict = pd.read_csv(col_dict_file, sep='\t')
df_dict = df_dict[['value', 'code']]
code_dict = df_dict.set_index('value').T.to_dict('records')[0]

df.columns = [code_dict[int(val.replace('41270-0.',''))] for val in df.columns]
cols = df.columns

#%%

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

n = len(cols)

# Visualise similarities
fig, ax = plt.subplots(dpi=500)
fig.set_size_inches(20,17)
sns.heatmap(df_euclid.head(n=n).iloc[:,:n], square=True, figure=fig)
plt.show()

#plt.imshow(df_euclid.values, interpolation="nearest", cmap='Blues')
#plt.show()

# Generate edges

# Create graph


# Generate clusters


# Visualise clusters

## ICD-10 TREE
