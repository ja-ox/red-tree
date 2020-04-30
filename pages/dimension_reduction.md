Here we present a brief overview of Dimension Reduction, before discussing the specific methods appropriate to our problem.

# Dimensionality reduction

Dimensionality reduction an umbrella term for techniques which transform high-dimensional data into a lower-dimensional representation.

These methods can be further divided into two subgroups:

- The first and simplest is known as **feature selection**, where a subset of the original variables (features) is chosen.
- The second is known as **feature extraction** (also known as feature projection, feature embedding, feature learning, representation learning, latent feature representation etc) - where a general transformation of the data from n dimensional space to lower m dimensional space is performed, creating a new set of variables as functions of the old set.

## Motivations

There are multiple reasons to perform dimension reduction:

1. Make data more computationally easy to deal with by reducing the volume ("the curse of dimensionality")
2. Extract 'meaningful' high-level information from raw information which may not be easily interpretable ("intrinsic variables")
3. Embed the data in a space where clusters of related points are more easily separable (classification)
4. Understand better the underlying topology of the data - its "true" latent shape.

The caveat is that while performing the reduction, we wish to retain the maximum amount of information describing the data as possible. Depending on the motivation for the reduction, some information may be more important than others, and so this will inform the technique you use (based on the assumptions it makes etc).

For example, in a clustering problem, it may be the case that we care only about separating clusters from eachother (e.g. in a classification problem), and hence methods which preserve local-connectivity only may be appropriate (e.g. t-SNE). However, we may not only wish to distinguish clusters from eachother, but say which clusters are closer related to eachother (e.g. investigating the relatedness between different groups) and hence we would require a method which preserves not only local-connectivity (intra-cluster) but also global connectivity (inter-cluster) (e.g. UMAP).

# Approaches

## Linear

PCA and related methods are the classical approach to dimension reduction: they take data in n dimensions and recompute an n dimensional basis of the space spanned by the data with the basis vectors ordered in terms of how much variance within the data they explain (a measure of how informative each dimension is, how well ti describes the data).

The caveat is that these approaches find the optimal *linear* transformation of the data, and hence may perform poorly on data whose "true latent shape" is non-linear. E.g. consider a swiss-roll embedded in 3d space.

- PCA, ICA, SVD, Factor Analysis

## Non-Linear

To combat the limitations of linear approaches to such data, various methods have been proposed.

### Kernel methods

A non-linear function is composed on the euclidean distance measure used in traditional linear methods in order to allow these to learn non-linear embeddings of the data in higher-dimensional feature space. Due to the [kernel trick](https://en.wikipedia.org/wiki/Kernel_method#Mathematics:_the_kernel_trick), this computationally tractable.

This relies on choosing the appropriate kernel function capturing the similarity of your data, which is data/domain specific.

### Graph-based

Since the 1970's, it has been recognised that the Laplacian matrix of a graph contains sufficient structural information about the graph to compute the *mincut* - the minimum weight of edges cut necessary to partition the graph into *k* disjoint subgraphs.*

Hence, if we have graph structured data (or if we can find a way to represent usual euclidean-structured data sensibly as a graph), these properties can be taken advantage of to create dimension reduction (and clustering) techniques on this data.

- Spectral Clustering/Laplacian Eigenmaps/Diffusion maps
- t-SNE
- UMAP

\* <sup>**Note:** this is only one of several equivalent justifications:</sup>

><sup>Also, justification of spectral clustering algorithms does not only come from this graph cut perspective and in fact encompasses several approaches that we will not detail here: perturbation approaches or hitting time considerations [138],
a polarization theorem [[23]](https://www.merl.com/publications/docs/TR2002-42.pdf), consistency derivations [135, 84], etc.</sup>

<sup>- [*Approximating Spectral Clustering via Sampling: a Review*](https://arxiv.org/pdf/1901.10204.pdf) (2.2.3)</sup>

#### Euclidean > Graph

There are multiple strategies for transforming Euclidean data into graph structured data. The main idea behind all of these is to create a measure of similarity/affinity between points, such that when this function is applied to two points it returns the weight of the edge connecting them (and weight 0 if unconnected).

From this graph, the Adjacency Matrix (aka Weight Matrix, Similarity Matrix, Affinity Matrix) can be created, and the graph Laplacian can be constructed from it. There are 3 standard forms of Laplacian Matrix.

# Our problem

However, all of these approaches are designed to compute dimension reduction on data which is entirely described by a graph, or whose individual datapoints are converted into nodes of a graph.

In our problem, each individual datapoint is *itself* a graph. More specifically, a tree whose topology is defined by the ICD-10 structure, and whose node-weights are defined by whether or not the patient has a record of each disease (node/leaf).

Our intuition is to use Graph-autoencoders (GAEs) to learn a dimension reduced form of this data, and compare it to classical methods. The question is, what classical methods exist for such data?

1. **Pruning the tree** prune the tree at various levels (all nodes, all parent classes of nodes etc). At the leaf level this is equivalent to one hot encoding the diseases.
2. **Shrinkage** a technique used for multi-level categorical data, combines levels together (note: in this context level refers to children of a category, and not hierarchical levels).
3. **Fusion via lasso regression** similar to 2. but in a data informed way. May require an objective function to regress, i.e. the reduction will be specific to the problem you wish to solve with the dimension reduction, and not problem-agnostic?

And use these as the benchmark to compare our investigative method, GAEs.
