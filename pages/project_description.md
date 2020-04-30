## Dimension Reduction of Complex Structured Data in UK Biobank with Autoencoders

### Description
This project focuses on the fundamental problem of the large number and complexity of variables in the UK Biobank, a massive prospective study of disease.  UK Biobank has data on 500,000 individuals, comprised of measurement on 1000’s of different variables.  A number of important variables have are tree-valued, as is the case for “ICD-10” variables.  ICD-10 is a standard system established by the WHO to encode every possible diagnosis or disease.  Every time a UK Biobank subject has an in- or out-patient visit to hospital, one or more ICD-10 codes are recorded. 

However, ICD-10 is a tree-valued variable.  For example, a diagnosis of “Rheumatoid arthritis” (M05.3) is a leaf at the end of the tree:

- Chapter XIII (Diseases of the musculoskeletal system)
  - Block M05–M14 (Inflammatory polyarthropathies)
    - Condition M05 (Seropositive rheumatoid arthritis)
      - Subcategory 3 (Rheumatoid arthritis) 

Also, the number of levels vary, with other diagnosis being ‘flatter’; for example, Pyogenic arthritis (M00) has no subcategory.  Such data present great analysis challenges, as there are over 19,154 individual diagnoses, and simply representing this as a factor variable with 19,154 possible levels (one per leaf) is inefficient as many diagnoses are never or rarely seen. It could be that a Block M05-M15 diagnosis is quite common, but each different children-leaves is relatively rare, a structure that is lost when considering a leaf-wise analysis.  And this is just one type of tree-valued variable in the UK Biobank.

The purpose of this project is to investigate data reduction strategies that respect the tree-valued structure of variables like ICD10 diagnoses.  As PCA, the go-to data reduction method, isn’t designed for such data, the student will investigate different approaches, including kernel methods [1], like kernel PCA & kernel-based autoencoders [2], and autoencoders specifically developed for tree-valued data [3].  Once a reduced dimension representation is found, the latent variables will tested for association with brain imaging phenotypes and other health outcomes.

This 8-week project comprises of the following tasks:

1. A literature review of general data reduction methods, and then specifically methods that accommodate tree-valued data.
2. Implement a simulation framework using the structure of ICD10 data in UK Biobank as a template.  This will involve generating synthetic data that has signals induced by ICD10 diagnoses of varying complexity.
3. Evaluation of several data reduction techniques in terms of their ability to detect known effects in the synthetic data, and discover sensible associations between diagnoses and brain imaging phenotypes and health outcome variables.


This project can act as a foundation for a DPhil, which may include:
1. Development of new data reduction methods for tree-valued data.
2. Development of new methods for association, considering the “variable n” problem associated with ICD10 data (i.e. some healthy subjects rarely if ever visit a hospital, while others have many visits, meaning the number of ICD10 diagnosis per subject varies greatly).
3. Develop methods for association that integrate the tree-valued data with all other variables, allowing both large-scale mass univariate and multivariate analyses.

Data availability: Profs. Smith and Nichols both have existing access to the UK Biobank data, imaging and extensive behavioural and demographic variables.

### References:

1. S.V.N. Vishwanathan and A.J. Smola. [Fast kernels on strings and trees.](https://www.stat.purdue.edu/~vishy/papers/VisSmo02.pdf) In Proceedings of Neural Information Processing Systems (NIPS), 2003.  
2. Laforgue, P., Clémençon, S., & d’Alché-Buc, F. (2018). [Autoencoding any Data through Kernel Autoencoders.](http://proceedings.mlr.press/v89/laforgue19a/laforgue19a.pdf)  
3. Irsoy, O., & Alpaydin, E. (2015). [Autoencoder trees.](http://proceedings.mlr.press/v45/Irsoy15.pdf) ACML 2015 - 7th Asian Conference on Machine Learning, (section 2), 378–390.

---

## Concise summary of the project

1. Review UK Biobank project and specifically motivation of imaging/non-imaging associations; review ICD10 & tree-structured data; review methods for data reduction on tree-structured data
2. Devise [simulations](#Simulations) using real UK Biobank data, and evaluate different approaches to data reduction, their effectiveness for detecting interpretable structure.
3. Apply to real data, compare ICD10 dimension reduction methods on 'positive control' prediction or association exercises, like with age.

## Motivation for project

CCA-ICA results in Fig 7 depend on a PCA dimension reduction on tabular data, and the concern is that PCA is not a great mechanism for summarising the ICD10 data (here, the ICD10 data was one-hot encoded at the leaf-level, though most of the resulting 19,154 columns were dropped after a sparsity check).

## Simulations

> You could simulate 'noise' data (i.e. random occurrence over the 19,154 diagnoses), and you could simulate 'signal' data for (say) cerebrovascular (I60-I69), where everyone has some leaf with that category, and then for varying mixtures of 'noise' and 'signal' data, can a dimension reduction method sniff out the signal from the noise.

## Suggested reading

#### Background reading for presentation

> Overview of the Biobank and the ICD10 data structure... a few figures from [Cortes et al (2017) Nature Genetics, 49(9):1311–1318](https://www.ncbi.nlm.nih.gov/pubmed/28759005) may be enough to motivate things.  If you are able to do *any* exploration of ICD10 even better.

#### UK Biobank and the imaging data context

- Miller, K. L., Alfaro-Almagro, F., Bangerter, N. K., Thomas, D. L., Yacoub, E., Xu, J., … Smith, S. M. (2016). [Multimodal population brain imaging in the UK Biobank prospective epidemiological study.](https://doi.org/10.1038/nn.4393) Nature Neuroscience, 19(11), 1523–1536.

#### Other reading

- PCA
- CCA
- ICA

#### Autoencoders

- http://www.deeplearningbook.org/contents/autoencoders.html

#### Kernal PCA

- Section 12.3 of [Bishop's book](http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf)
- https://medium.com/@ODSC/implementing-a-kernel-principal-component-analysis-in-python-495f04a7f85f
