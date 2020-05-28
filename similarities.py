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

n = 500 # Number of patients
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
    df = pd.read_csv(file, sep='\t', nrows=n)
    cols = df.columns
    

# Select only ICD-10 columns
mask = df.columns.str.startswith('41270')
df = df[df.columns[mask]]

# Summary stats
totals = df.sum(axis=1)
avg = np.mean(totals)

# Renaming columns with ICD-10 codes
col_dict_file = r'C:\Users\Jacob\Downloads\autoencoders\data\ukb_latest-ICD10-onehot_icd10_map.txt'
df_dict = pd.read_csv(col_dict_file, sep='\t')
df_dict = df_dict[['value', 'code']]
code_dict = df_dict.set_index('value').T.to_dict('records')[0]

df.columns = [code_dict[int(val.replace('41270-0.',''))] for val in df.columns]
cols = df.columns

# Transpose dataframe so that each row is a disease
df = df.T
df.index = cols

## MULTIMORBIDITIES

# Generate Disease x Disease Similarity Matrix

def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)

# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html
# Metrics intended for boolean-valued vector spaces:

from sklearn.neighbors import DistanceMetric

dist = DistanceMetric.get_metric('sokalsneath')
dists = dist.pairwise(df)
#df_dists = pd.DataFrame(dists, columns=df.index, index=df.index)

m = len(cols)


# DO I need to remove patients which have 0 for everything??? Is this messing up the metrics?

# Want metric that cares when both diseases have TT, ignores NN, and weights by TN NT
# i.e. TT / (TT+NT+TN) ? e.g. DICE and SOKALSNEATH both include TT in denominator (dist)

# Visualise similarities
fig, ax = plt.subplots(dpi=250)
fig.set_size_inches(20,17)
sns.heatmap(dists, square=True, figure=fig)
plt.show()

#plt.imshow(df_euclid.values, interpolation="nearest", cmap='Blues')
#plt.show()

if False:
    plt.bar(list(range(0,len(totals.value_counts())))[:40], [100 * totals.value_counts() / m][0][:40])

#%%

# Generate edges

up_tri = dists.copy()
up_tri[np.tril_indices_from(up_tri)] = np.nan

print(f'   1 : {len(np.argwhere(up_tri == 1))}')
print(f'(0,1): {len(np.argwhere(up_tri < 1)) - len(np.argwhere(up_tri == 0))}')
print(f'   0 : {len(np.argwhere(up_tri == 0))}')

edges = [(cols[i], cols[j]) for i, j in np.argwhere(up_tri == 0)]

import pickle

with open(r'C:\Users\Jacob\Downloads\autoencoders\data\similarity_edges.txt', 'wb') as fp:
    pickle.dump(edges, fp)

# Create graph


# Generate clusters


# Visualise clusters

## ICD-10 TREE
