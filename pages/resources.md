# Resources

### Dimension reduction

- [Proximity in Dimension Reduction, Clustering, and Classification](http://mypage.iu.edu/~mtrosset/Courses/675/notes.pdf) (Trosset)

### Network Embedding

- [Network Embedding: An Overview](https://arxiv.org/abs/1911.11726) (2019)
  >  The advantage of node embedding as a technique is that it does not require feature engineering by domain experts.

- https://paperswithcode.com/task/network-embedding
- [To Embed or Not: Network Embedding as a Paradigm in Computational Biology](https://www.frontiersin.org/articles/10.3389/fgene.2019.00381/full) (2019)
- [Graph-adaptive Nonlinear Dimensionality Reduction](https://arxiv.org/pdf/1801.09390.pdf) (Kernel-PCA on graphs)
- https://jlmelville.github.io/smallvis/spectral.html

### Graph Neural Networks (GNN)

- https://en.wikipedia.org/wiki/Recursive_neural_network#Extension_to_graphs
- [A Comprehensive Survey on Graph Neural Networks](https://arxiv.org/abs/1901.00596) (2019)
- [Graph Neural Networks: A Review of Methods and Applications](https://arxiv.org/pdf/1812.08434.pdf) (2019)
- [The Graph Neural Network Model](https://repository.hkbu.edu.hk/cgi/viewcontent.cgi?article=1000&context=vprd_ja) (2007)
- https://github.com/thunlp/GNNPapers
- [Graph-based dimensionality reduction](https://perso.uclouvain.be/michel.verleysen/papers/bookLezoray12jl.pdf)
- [Deep Learning on Graphs with Graph Convolutional Networks](http://deeploria.gforge.inria.fr/thomasTalk.pdf)
- https://tkipf.github.io/graph-convolutional-networks/
- https://towardsdatascience.com/a-gentle-introduction-to-graph-neural-network-basics-deepwalk-and-graphsage-db5d540d50b3
- [Cambridge Reading Group: GNNs](http://cbl.eng.cam.ac.uk/pub/Intranet/MLG/ReadingGroup/2018-11-14_GNNs.pdf)

### Graph Autoencoders

- ...

### Dimension reduction on graph / tree data points

Lots of literature on dimension reduction using linear techniques.
Lots of lit on dim red using non-linear techniques. Subset of these take results from Spectral theory, considering datapoints as nodes on a graph, and computing the edges via similarity.

However, little literature on when each individual datapoint is a graph.

- [Dimension Reduction in Principal Component Analysis for Trees](https://arxiv.org/abs/1202.2371) (PCA on trees)
- [Tree distance metrics](https://cran.r-project.org/web/packages/Quartet/vignettes/Tree-distance-metrics.pdf) (measures distance between different structured trees)

#### multi-level categorical variable / Categorical regressor / shrinkage / fused lasso

(Multi-level refers to multiple children)

- https://stats.stackexchange.com/questions/146907/principled-way-of-collapsing-categorical-variables-with-many-levels
- https://stats.stackexchange.com/questions/227125/preprocess-categorical-variables-with-many-values/277302#277302
- https://stats.stackexchange.com/questions/349513/variable-selection-with-tree-structured-covariates
- [A Note on Coding and Standardization of Categorical Variables in (Sparse) Group Lasso Regression](https://arxiv.org/abs/1805.06915)
- [Elements of Statistical Learning](http://www-stat.stanford.edu/~tibs/ElemStatLearn/) (p.329)

#### Hierarchical clustering ✔️

- [Hierarchical clustering algorithm for categorical data using a probabilistic rough set model](https://www.sciencedirect.com/science/article/abs/pii/S0950705114001300) (2014)
- https://en.wikipedia.org/wiki/Cluster_analysis
- https://en.wikipedia.org/wiki/Numerical_taxonomy

### ICD-10

Hierarchical clustering of tree (3.6):

- https://books.google.co.uk/books?id=K-RhDwAAQBAJ&pg=PA105&lpg=PA105&dq=icd10+dimension+reduction+tree


### Misc

- [Treelets — A Tool for Dimensionality Reduction and Multi-Scale Analysis of Unstructured Data](https://www.stat.cmu.edu/~annlee/AISTATS-07_treelets.pdf)
- [Dimensionality reduction for tree-like data](http://www.bioinformatics.org/labnotes/dr-tree/bm-20160630.html)
- [Efficient Additive Kernels via Explicit Feature Maps](http://www.robots.ox.ac.uk/~vedaldi/assets/pubs/vedaldi11efficient.pdf)
- https://www.ijcai.org/Proceedings/2018/0452.pdf
- https://arxiv.org/abs/1801.09390
- https://www-users.cs.umn.edu/~saad/PDF/agadir.pdf
- https://perso.uclouvain.be/michel.verleysen/papers/bookLezoray12jl.pdf
- https://sites.tufts.edu/eeseniordesignhandbook/files/2018/05/Graph_Embedding_for_Dimensionality_Reduction_Anuththari_Gamage.pdf
- https://easychair.org/publications/paper/pccS
- https://www.sciencedirect.com/science/article/abs/pii/S0031320309001460


### Nichols

- https://git.fmrib.ox.ac.uk/fsl/funpack
- https://git.fmrib.ox.ac.uk/fsl/funpack/-/tree/master/funpack%2Fdata%2Fhierarchy (19 or 2, biggest files)
