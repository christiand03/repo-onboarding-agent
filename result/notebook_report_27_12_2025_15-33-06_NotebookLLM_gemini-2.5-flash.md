# Notebook (DSF_Project_clustering_classification.ipynb): clustering-and-classification-uni documentation

## 1. Executive Summary
This notebook implements an end-to-end pipeline for clustering and classification of news articles using the BBC News dataset. The process involves comprehensive text preprocessing, followed by text embedding using a Sentence Transformer model. Dimensionality reduction is applied via PCA to optimize the embeddings. Spectral Clustering is then performed to group articles into categories, achieving a V-Measure score of 0.726 against true labels. Finally, Support Vector Machine (SVM) and Random Forest classifiers are trained and evaluated, yielding average weighted F1 scores of 0.946 and 0.944 respectively, demonstrating strong classification performance.

## 2. Technical Prerequisites
### Environment
*   **Dependencies:**
    *   pandas
    *   numpy
    *   matplotlib
    *   seaborn
    *   regex
    *   umap-learn
    *   nltk
    *   sentence-transformers
    *   scikit-learn
    *   scipy
*   **External Configuration:** None detected.
### Data Lineage
*   **Source:** Local CSV files:
    *   `C:\Users\Debbertin\Downloads\BBC News Train.csv` (for training data)
    *   `C:\Users\Debbertin\Downloads\BBC News Test.csv` (for test data)

## 3. Methodology & Justification
*   **Step 1: Environment Setup and Data Loading**
    *   NLTK libraries for stopwords, wordnet, and omw-1.4 are downloaded and initialized.
    *   A custom `preprocess_text` function is defined to clean textual data. This function performs lowercasing, removes punctuation, tokenizes text, eliminates English stopwords, and applies lemmatization to standardize words.
    *   The BBC News dataset is loaded from specified local CSV paths into pandas DataFrames for both training and testing.
    *   Text columns from these DataFrames are extracted and preprocessed using the defined function.
    *   The 'Category' column from the training DataFrame is converted to numerical codes to serve as true labels for evaluation.

*   **Step 2: Text Embedding and Normalization**
    *   A `SentenceTransformer` model (`all-MiniLM-L6-v2`) is initialized. This is a lightweight pre-trained model capable of generating high-quality sentence embeddings.
    *   Preprocessed training and test text data are encoded into dense vector embeddings using this model.
    *   The generated embeddings are then L2-normalized. This normalization step is crucial for subsequent cosine similarity calculations and ensures all vectors have a consistent scale, improving model performance.

*   **Step 3: Dimensionality Reduction (PCA)**
    *   Principal Component Analysis (PCA) is applied to both the normalized training and test embeddings. The `n_components` parameter is set to 200, which is observed to retain approximately 95-96% of the total variance. This reduction aims to decrease computational load and mitigate the curse of dimensionality while preserving essential features for downstream tasks.

*   **Step 4: Cosine Similarity Matrix Generation and Normalization**
    *   A cosine similarity matrix is computed from the PCA-transformed training embeddings (`X_pca`) to measure the pairwise similarity between all documents.
    *   Initial checks confirm no NaN values and the matrix is symmetric, but it contains negative values and diagonal elements slightly deviating from 1.
    *   To address this, the diagonal of the matrix is explicitly set to 1 (indicating perfect self-similarity).
    *   The matrix is then normalized using `MinMaxScaler` to map all values to the range [0, 1]. Any values exceeding 1 after scaling are capped to 1. This normalization is performed to prepare the affinity matrix for Spectral Clustering, which typically operates best with non-negative, normalized similarities.

*   **Step 5: Spectral Clustering**
    *   Spectral Clustering is applied to the normalized cosine similarity matrix. The number of clusters (`n_clusters`) is set to 5, aligning with the known number of categories in the BBC News dataset, and `affinity` is set to 'precomputed' to use the custom similarity matrix.
    *   The `v_measure_score` is calculated to evaluate the quality of the clustering results against the true labels, yielding a score of 0.726. This metric assesses both homogeneity and completeness of the clusters.

*   **Step 6: Visualization of Clusters (t-SNE and UMAP)**
    *   t-SNE (t-Distributed Stochastic Neighbor Embedding) is applied to the PCA-reduced training embeddings to project them into a 2-dimensional space, facilitating visualization of clusters.
    *   UMAP (Uniform Manifold Approximation and Projection) is also used to reduce the dimensionality of the PCA-transformed data to 2D for another visualization. These plots help in qualitatively assessing the separation and compactness of the clusters identified by Spectral Clustering.

*   **Step 7: Supervised Classification (SVM & Random Forest)**
    *   **Support Vector Machine (SVM):** An SVM classifier with an RBF kernel, C=1.0, and gamma='scale' is trained on the PCA-reduced training data (`X_pca`) and true labels. The model is then used to predict categories for the test dataset (`X_pca_test`). Cross-validation with a weighted F1-score (5-fold) is performed on the training set, yielding an average F1 score of 0.946, indicating robust classification performance.
    *   **Random Forest Classifier:** A Random Forest classifier with 100 estimators is trained on the PCA-reduced training data and true labels. Predictions are made on the test data. Cross-validation (5-fold) using a weighted F1-score on the training set results in an average F1 score of 0.944, demonstrating competitive performance for multi-class classification.

## 4. Key Configuration & Hyperparameters (only if applicable)
| Parameter | Value | Context |
| :--- | :--- | :--- |
| `PCA.n_components` | 200 | Number of principal components retained for dimensionality reduction. |
| `SentenceTransformer` | 'all-MiniLM-L6-v2' | Specifies the pre-trained Sentence-BERT model used for generating embeddings. |
| `SpectralClustering.n_clusters` | 5 | The number of clusters to form. |
| `SpectralClustering.affinity` | 'precomputed' | Indicates that a precomputed similarity matrix is provided. |
| `SpectralClustering.random_state` | 42 | Seed for random number generation for reproducibility. |
| `TSNE.n_components` | 2 | The dimension of the embedded space for visualization. |
| `TSNE.random_state` | 42 | Seed for random number generation for reproducibility. |
| `TSNE.perplexity` | 70 | Related to the number of nearest neighbors used in t-SNE. |
| `TSNE.max_iter` | 1000 | Maximum number of iterations for the optimization. |
| `UMAP.n_neighbors` | 40 | Number of neighboring points to consider for manifold approximation. |
| `UMAP.min_dist` | 0.1 | The effective minimum distance between embedded points. |
| `UMAP.metric` | 'euclidean' | The metric used to compute distances in high dimensional space. |
| `UMAP.n_components` | 2 | The dimension of the embedded space for visualization. |
| `UMAP.random_state` | 42 | Seed for random number generation for reproducibility. |
| `SVC.kernel` | 'rbf' | Specifies the kernel type used in the Support Vector Machine. |
| `SVC.C` | 1.0 | Regularization parameter; the strength of the regularization is inversely proportional to C. |
| `SVC.gamma` | 'scale' | Kernel coefficient for 'rbf', 'poly' and 'sigmoid'. If 'scale' is passed, it uses 1 / (n_features * X.var()). |
| `SVC.random_state` | 42 | Seed for random number generation for reproducibility. |
| `RandomForestClassifier.n_estimators` | 100 | The number of trees in the forest. |
| `RandomForestClassifier.random_state` | 42 | Seed for random number generation for reproducibility. |
| `RandomForestClassifier.n_jobs` | -1 | Number of jobs to run in parallel. -1 means using all processors. |

## 5. Results & Visualizations (this is not implemented yet so skip this step)

## 6. Artifacts & Storage
*   **Outputs:** No explicit artifacts (e.g., model files, processed data) are saved to disk by this notebook.
*   **Location:** Not applicable.

---

<br>
<br>

# Notebook (DSF_Project_legacy_code.ipynb): clustering-and-classification-uni documentation

## 1. Executive Summary
This notebook delves into various unsupervised learning techniques for clustering text data. It commences with the critical step of vectorizing preprocessed text using TF-IDF. Subsequently, it systematically explores optimal cluster determination for K-Means using both the Elbow Method and Silhouette Score before applying the K-Means algorithm. The analysis extends to density-based clustering, implementing both DBSCAN and HDBSCAN with cosine similarity. Finally, it constructs a K-Nearest Neighbors graph and performs a connectivity analysis to understand the data's inherent structure.

## 2. Technical Prerequisites
### Environment
*   **Dependencies:**
    *   pandas
    *   numpy
    *   matplotlib
    *   seaborn
    *   regex
    *   umap-learn
    *   nltk
    *   sentence-transformers
    *   scikit-learn
    *   scipy
*   **External Configuration:** None detected.
### Data Lineage
*   **Source:** Text data is utilized after being preprocessed into `preprocessed_train_data` and `preprocessed_test_data`. These datasets are then vectorized using `TfidfVectorizer` to produce `X_train_tfidf` and `X_test_tfidf`, which serve as the primary input for all clustering algorithms. The original source of the `newsgroups_train.data` is inferred to be from `sklearn.datasets`.

## 3. Methodology & Justification
*   **Step 1: Text Data Vectorization**
    *   Preprocessed textual data (`preprocessed_train_data`, `preprocessed_test_data`) is transformed into numerical feature vectors using `TfidfVectorizer` from `sklearn.feature_extraction.text`. This step is fundamental, as it converts unstructured text into a quantitative format (TF-IDF scores) that machine learning algorithms can process. The resulting matrices (`X_train_tfidf`, `X_test_tfidf`) capture the importance of words within documents relative to the entire corpus.
*   **Step 2: K-Means Optimal Cluster Determination (Elbow Method)**
    *   The Elbow Method is employed to estimate the optimal number of clusters (`k`) for the K-Means algorithm. By iterating K-Means with varying numbers of clusters (from 1 to 25) and plotting the inertia (sum of squared distances of samples to their closest cluster center), a visual "elbow" point is sought. This point typically indicates diminishing returns for adding more clusters, suggesting a good trade-off between cluster tightness and model complexity.
*   **Step 3: K-Means Optimal Cluster Determination (Silhouette Score)**
    *   Complementing the Elbow Method, the Silhouette Score is calculated for a range of cluster numbers (from 10 to 25). The silhouette score measures how similar an object is to its own cluster compared to other clusters, with higher scores indicating better-defined and more separated clusters. The `k` value yielding the maximum silhouette score is chosen as the optimal number of clusters.
*   **Step 4: K-Means Clustering Implementation**
    *   With an `optimal_clusters` value of 20 determined from previous analysis, K-Means clustering is performed on the `X_train_tfidf` dataset. This step partitions the data points into 20 distinct groups, assigning each point a cluster label based on its proximity to the cluster centroids.
*   **Step 5: DBSCAN Clustering**
    *   DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is applied to the `X_train_tfidf` dataset. Before applying DBSCAN, cosine similarity is computed between all data points, normalized, and converted into a distance matrix (where distance = 1 - similarity). DBSCAN then identifies clusters based on the density of data points, effectively grouping densely packed points while marking sparse regions as noise.
*   **Step 6: DBSCAN Evaluation**
    *   The quality of the DBSCAN clustering is assessed using the Silhouette Score. Importantly, noise points (labeled as -1 by DBSCAN) are excluded from this calculation to provide a more meaningful evaluation of the identified clusters.
*   **Step 7: Distance Matrix Diagonal Initialization**
    *   An explicit check and correction (`np.fill_diagonal(cosine_distance_matrix, 0)`) are performed to ensure that the diagonal elements of the cosine distance matrix are exactly zero. This is a crucial preprocessing step for algorithms that use 'precomputed' distance metrics, as the distance of any data point to itself must logically be zero.
*   **Step 8: HDBSCAN Clustering**
    *   HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) is employed as an advanced density-based clustering algorithm. Similar to DBSCAN, it operates on the precomputed cosine distance matrix. HDBSCAN offers advantages in identifying clusters of varying densities and is generally more robust to parameter selection compared to DBSCAN.
*   **Step 9: K-Nearest Neighbors Graph Construction**
    *   A K-Nearest Neighbors (KNN) graph is constructed for the `X_train_tfidf` data. This graph connects each data point to its `k` (set to 10) nearest neighbors based on cosine similarity, creating a sparse representation of the data's local structure.
*   **Step 10: Graph Connectivity Analysis**
    *   The `connected_components` algorithm from `scipy.sparse.csgraph` is used to determine the number of distinct connected components within the constructed KNN graph. This analysis provides insight into the overall connectivity and inherent grouping within the dataset based on neighborhood relationships.

## 4. Key Configuration & Hyperparameters (only if applicable)
| Parameter | Value | Context |
| :--- | :--- | :--- |
| `random_state` | 42 | Seed for the random number generator, used in K-Means for centroid initialization to ensure reproducibility. |
| `n_init` | 10 | Number of times the K-Means algorithm will be run with different centroid seeds. The final results will be the best output of `n_init` consecutive runs. |
| `cluster_range` (K-Means Elbow) | 1-25 | The range of `k` values (number of clusters) explored during the Elbow Method to identify the optimal `k`. |
| `cluster_range` (K-Means Silhouette) | 10-25 | The range of `k` values (number of clusters) explored for calculating the Silhouette Score. |
| `optimal_clusters` (K-Means) | 20 | The final chosen number of clusters for the K-Means model, derived from the evaluation methods. |
| `eps` (DBSCAN) | 0.4 | The maximum distance between two samples for one to be considered as in the neighborhood of the other in DBSCAN. |
| `min_samples` (DBSCAN/HDBSCAN) | 5 | The minimum number of samples in a neighborhood for a point to be considered as a core point in DBSCAN and HDBSCAN. |
| `min_cluster_size` (HDBSCAN) | 5 | The smallest size grouping that a cluster can be for HDBSCAN. |
| `k` (k-neighbors graph) | 10 | The number of nearest neighbors considered when constructing the K-Nearest Neighbors graph. |

## 5. Results & Visualizations (this is not implemented yet so skip this step)

## 6. Artifacts & Storage
*   **Outputs:** None detected.
*   **Location:** None detected.

---