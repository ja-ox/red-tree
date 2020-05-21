### Week 1:

#### Q's
- Literature reading
  - Understand existing dimension reduction techniques
       - linear methods
       - kernel methods
       - non-linear methods / manifold embedding techniques
       - Additional dimension reduction techniques worth exploring:
          - t-SNE
          - sparse PCA (ICA) (SPAMS http://spams-devel.gforge.inria.fr/)
          - UMAP
- Exploring data
- Before jumping into the real data for any actual testing etc though try simulated data
  - E.g. start off with one chapter (I, II etc)
  - small scale initially
  - choose disorders with many leaves

> #### A's
> 
> - Most non-linear dimension reduction techniques use mathematical principles very similar to Spectral clustering under the hood, i.e:
>    - create graph representation of data
>    - create matrix representation of graph containing 'distance' information of from one node to another  
>        - either using Graph Laplacian (normal, symmetric, or r.w.)  
>        - or using the similarity measure chosen to create the graph (thresholded or otherwise), create a similarity matrix or matrix encompassing similar information
> - These methods, as well as GNN's, seem to be designed to take in data where each datapoint is a node in a graph, not where features of each datapoint form a graph (ICD-10 variables).

### Week 2:

#### Q's

- How to transform raw data into ingestable format for graph autoencoders
- How to formulate problem
- Inherent tree-structure vs data informed approach

> #### A's
> 
> - Create graph representation of total dataset with nodes corresponding to diseases, and edges corresponding to comorbidities within individual patients, and relationships defined by ICD-10.
> - Perform clustering (dim reduction) on _this_ graph using traditional/GNN methods.
> - Compare performance vs naive clustering by just pruning the tree at various depths.
> - Do we weight the comorbidity edges? Proportional to appearance in dataset? Do we threshold it? Only more than n occurrences get represented, but then the edges have no weights?
> - Wrote code to visualise ICD-10 structure and basic code to create pruned representations of it.

### Week 3:

#### Q's

- Two naive methods for measuring similarity of different variable for 'clustering' of dimensions:
  - Hierarchical clustering on _data_ 
      - linear correlation, other measures of distance disease x disease matrix
      - Similarity matrix subjects by diseases
  - Pruning on _tree_
- For testing the GNN combined method vs the 2 simple methods create toy example (i.e. disease clusters as predictors for...):
  - age
  - BP
  - Comorbidity covid?
- Add parent, gandparent etc columns - see how this compares
- Colour code diagram according to where leaf sits in hierarchical clustering driven by incidence data (need to cluster on actual data before able to do this)

> #### A's
> 
> - Began exploring data.
> - Have got understanding of data structure as created by [funpack](https://github.com/ja-ox/red-tree/wiki/Data) commands here.
> - Have written boilerplate code to load data, do initial transformations (i.e. create pairwise disease x disease similarity/distance matrix)
> - Began exploring similarity measures - there are a lot. Seems to be domain specific which is chosen.

### Week 4

#### Q's

- Add parent grandparent etc as nodes to similarity matrix
- Summary plots
  - what is the histogram of number of events across (done both ways)
  - matrix of incidence outcome positives
  - subjects x diseases
    - histogram across both axes
  - Similarly, simple correlation matrices done both ways
    - comorbidities vs similarity across subjects
    - Barplot for top several layers of tree

- Avg number of diseases per patient etc
- Investigate different distance measures - Hamming, Walls?

> #### A's
>
>- [Explanation for why PCA is inappropriate for this problem](https://stats.stackexchange.com/questions/159705/would-pca-work-for-boolean-binary-data-types)
>- Next step: when considering graph clustering/dim reduction architectures, in addition to GAEs the pooling layers of convGNNs themselves can be used to create dimension-reduced representations of graphs e.g. [Hierarchical Graph Representation Learning with Differentiable Pooling](https://arxiv.org/pdf/1806.08804.pdf)
>
>- Have written code to:
>   - load file
>   - generate patient x disease dataframe (currently only top x patients due to memory/speed/initial stages)
>   - create disease x disease similarity matrix (specific similarity/distance measure parameterised - many options, no canonical answer):
>      -  `‘braycurtis’, ‘canberra’, ‘chebyshev’, ‘cityblock’, ‘correlation’, ‘cosine’, ‘dice’, ‘euclidean’, ‘hamming’, ‘jaccard’, ‘jensenshannon’, ‘kulsinski’, ‘mahalanobis’, ‘matching’, ‘minkowski’, ‘rogerstanimoto’, ‘russellrao’, ‘seuclidean’, ‘sokalmichener’, ‘sokalsneath’, ‘sqeuclidean’, ‘yule’`
>   - Plot heatmap of similarities
>- Todo:
>   - Extract edges from matrix
>   - Plot edges individually
>   - Plot edges combined with ICD-10
>   - Perform clustering on both representations
>   - Given e.g. [Similarity Network Fusion (SNF) paper](https://www.nature.com/articles/nmeth.2810) (http://compbio.cs.toronto.edu/SNF/SNF/Software.html), consider:
>        - unweighted edges (with incidence thresholded by some similarity score) vs 
>        - weighted edges taking raw/normalised similarity score.   
>     Consider how ICD-10 edge weights should compare. (Hyper-parameter? Again seems like no "canonical" solution here).
>   - Once clusters produced, colour pure ICD-10 by clusters for visualisation
>   - [Circle graph](https://en.wikipedia.org/wiki/Circle_graph#Chromatic_number)? Could have radial ICD-10 tree, and 'chordal' edges from multimorbidities (similarities).

![circle graph example](https://upload.wikimedia.org/wikipedia/commons/3/3f/Ageev_5X_circle_graph.svg)
