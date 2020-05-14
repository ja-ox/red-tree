Project on dimension reduction for tree-structured data. See the [project description](/pages/project_description.md) for more info.

`generate_icd10_graph.py`

Downloads the ICD-10 parent/child node relationships from the UK Biobank website. Generates an interactive graph showing the tree structure.

`similarities.py`

Loads either the UK Biobank [data](https://github.com/ja-ox/red-tree/wiki/Data) or simulated toy data, where columns are diseases, rows are patients, columns have value either `1` or `0` (presence/absence).

Generates similarity/distance matrix for pairwise disease x disease data, using given similarity measure.

`embedding_test.py`

Given toy data, demonstrates manifold embedding using various linear and non-linear dimension reduction techniques (3.d. to 2.d).
