# -*- coding: utf-8 -*-
"""
Script to compare different embedding (network dimension reduction) techniques
"""
import numpy as np
from collections import OrderedDict
from functools import partial
from time import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter

from sklearn import manifold, datasets, decomposition
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.utils import check_random_state

#############################
## FUNCTIONS
#############################

def plot_manifolds(methods, X, color, columns=False, cmap=plt.cm.Spectral, v1=4, v2=-72):
    """
    Given a series of manifold embedding methods, plots the results on data X.
    """
    if columns:
        n_points = len(X[0])
    else:
        n_points = len(X)
    fig = plt.figure(figsize=(15, 10))
    fig.suptitle(f"Manifold Learning with {n_points} points, {n_neighbors} neighbors", 
             fontsize=14)
    
    # Add 3d scatter plot
    ncols = 5
    nrows = int(np.ceil(len(methods)/(ncols-1)))
    ax = fig.add_subplot(nrows, ncols, 1, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=cmap)
    ax.view_init(v1, v2)

    # Plot results
    for i, (label, method) in enumerate(methods.items()):
        t0 = time()
        Y = method.fit_transform(X)
        t1 = time()
        print(f'{label}: {t1-t0:.2g} sec')
        ax = fig.add_subplot(nrows, ncols, 2 + i + (i//4))
        if columns:
            ax.scatter(Y.T[0], Y.T[1], c=color, cmap=cmap)
        else:
            ax.scatter(Y[:, 0], Y[:, 1], c=color, cmap=cmap)
        ax.set_title(f'{label}: {t1-t0:.2g} sec')
        ax.xaxis.set_major_formatter(NullFormatter())
        ax.yaxis.set_major_formatter(NullFormatter())
        ax.axis('tight')

    plt.show()

###########################
## SETUP
###########################

# Next line to silence pyflakes. This import is needed.
Axes3D

# Parameters
n_points = 1000
n_neighbors = 10
n_components = 2
cmap = plt.cm.Spectral #rainbow

###########################
## DATA
###########################
# Create S-curve
X, color = datasets.make_s_curve(n_points, random_state=0)


# Create our sphere.
random_state = check_random_state(0)
p = random_state.rand(n_points) * (2 * np.pi - 0.55)
t = random_state.rand(n_points) * np.pi

# Sever the poles from the sphere.
indices = ((t < (np.pi - (np.pi / 8))) & (t > ((np.pi / 8))))
colors = p[indices]
sphere_data = np.zeros((sum(indices),3))
sphere_data[:,0] = np.sin(t[indices]) * np.cos(p[indices])
sphere_data[:,1] = np.sin(t[indices]) * np.sin(p[indices])
sphere_data[:,2] = np.cos(t[indices])

###########################
## METHODS
###########################

# Set-up manifold methods
LLE = partial(manifold.LocallyLinearEmbedding,
              n_neighbors, n_components, eigen_solver='auto')

methods = OrderedDict()
methods['LLE'] = LLE(method='standard')
methods['LTSA'] = LLE(method='ltsa')
methods['Hessian LLE'] = LLE(method='hessian')
methods['Modified LLE'] = LLE(method='modified')
methods['Isomap'] = manifold.Isomap(n_neighbors, n_components)
methods['MDS'] = manifold.MDS(n_components, max_iter=100, n_init=1)
methods['SE'] = manifold.SpectralEmbedding(n_components=n_components,
                                           n_neighbors=n_neighbors)
methods['t-SNE'] = manifold.TSNE(n_components=n_components, init='pca',random_state=0)
# Set-up linear methods
methods['PCA'] = decomposition.PCA(n_components)
methods['ICA'] = decomposition.FastICA(n_components)
#methods['NMF'] = decomposition.NMF(n_components) #Negative vals
methods['Factor Analysis'] = decomposition.FactorAnalysis(n_components)
#methods['LDA'] = LinearDiscriminantAnalysis(n_components) # Supervised method, requires class labels
methods['Kernel PCA (rbf)'] = decomposition.KernelPCA(n_components, kernel="rbf")
methods['Kernel PCA (poly)'] = decomposition.KernelPCA(n_components, kernel="poly")
methods['Kernel PCA (sigmoid)'] = decomposition.KernelPCA(n_components, kernel="sigmoid")
methods['Kernel PCA (cosine)'] = decomposition.KernelPCA(n_components, kernel="cosine")



###########################
## PLOTS
###########################

# S-Curve
plot_manifolds(methods, X, color=color, cmap=cmap)

# Sphere
plot_manifolds(methods, sphere_data, color=colors, cmap=cmap, v1=40, v2=-10)
