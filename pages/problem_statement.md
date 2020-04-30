# Problem Statement

> Medical data is increasingly large and complex. A number of important variables are tree-structured (hierarchical multi-level categorical/binary variables), as is the case for “ICD-10” variables. ICD-10 is a standard system established by the WHO to encode every possible diagnosis or disease. The standard way to incorporate such variables is one hot encoding of the nodes, but this leads to the 'curse of dimensionality' when e.g. we have over 20000 nodes in the tree. There is the further problem of sparsity of data, with many nodes having very few data points. As such, dimension reduction via methods of 'clustering' several nodes together is worth exploring. There are several classical methods for clustering individual multi-level categorical variables, but the literature is sparse on methods for complex tree structured categories. Here we investigate adaptations of classical methods to perform clustering ("fusion") on leaves and branches of trees, as well as Graph Autoencoders.

Each patient has a set of binary-indicator variables for disease presence/absence. This is a one-hot encoding of the leaf nodes of the ICD-10 disease classification tree.

Hence each patient can have this data sensibly modelled as a tree, where nodes are weighted by presence/absence of disease (`1` vs `0`):

![](https://ars.els-cdn.com/content/image/1-s2.0-S1532046414002639-gr1.jpg)

How do we, given this tree data for each patient, sensibly perform dimension reduction?

- **Idea 1:** Cluster data into parent nodes
- **Idea 2:** Sum all data points, i.e. one tree with nodes weighted by disease presence across population.
