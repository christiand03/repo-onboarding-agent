# Notebook: clustering-and-classification-uni documentation

## 1. Executive Summary
This notebook implements a comprehensive pipeline for clustering and classifying BBC news articles. It addresses the business problem of automatically categorizing text data by employing advanced natural language processing and machine learning techniques. The methodology involves text preprocessing, generating semantic embeddings using a SentenceTransformer, reducing dimensionality with PCA, performing Spectral Clustering to group similar articles, and finally training and evaluating Support Vector Machine (SVM) and Random Forest classifiers. The project achieved a V-Measure of approximately 0.726 for clustering and demonstrated strong classification performance with average F1 scores of 0.946 for SVM and 0.944 for Random Forest.

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
*   **Source:**
    *   BBC News Train dataset: `C:\Users\Debbertin\Downloads\BBC News Train.csv`
    *   BBC News Test dataset: `C:\Users\Debbertin\Downloads\BBC News Test.csv`

## 3. Methodology & Justification
*   **Step 1: Environment Setup & Text Preprocessing**
    *   Necessary NLTK data resources (stopwords, WordNet, OMW-1.4) are downloaded.
    *   A `preprocess_text` function is defined to clean the textual data. This involves converting text to lowercase, removing punctuation, tokenizing words, filtering out common English stopwords, and lemmatizing words to their base form. This preprocessing step standardizes the text, making it suitable for subsequent numerical encoding and analysis by reducing noise and improving feature quality.
*   **Step 2: Data Loading and Label Preparation**
    *   The BBC News training and testing datasets are loaded from specified local CSV file paths into pandas DataFrames.
    *   The categorical labels for the training articles (`Category` column) are converted into numerical codes (`true_labels`). These numerical labels serve as the ground truth for evaluating the performance of both clustering and classification models.
*   **Step 3: Text Embedding and Normalization**
    *   The preprocessed text data from both training and testing sets is transformed into high-dimensional numerical embeddings using the `all-MiniLM-L6-v2` SentenceTransformer model. This lightweight model efficiently captures the semantic meaning of the text.
    *   The generated embeddings are then normalized using L2 normalization. This ensures that all embedding vectors have a unit norm, which is a standard practice for cosine similarity calculations and can improve the performance of downstream machine learning algorithms.
*   **Step 4: Dimensionality Reduction (PCA)**
    *   Principal Component Analysis (PCA) is applied to the normalized embeddings. The dimensionality is reduced to 200 components for both training and test datasets. This reduction is chosen to retain a significant portion (over 95%) of the original variance, thereby simplifying the data representation while preserving most of its information content, which helps in reducing computational load and potentially mitigating the curse of dimensionality.
*   **Step 5: Cosine Similarity Matrix Generation & Refinement**
    *   A cosine similarity matrix is computed based on the PCA-reduced training embeddings (`X_pca`). This matrix quantifies the semantic similarity between every pair of news articles in the training set.
    *   Checks are performed to ensure the matrix is free of NaN values, symmetric, and non-negative. The diagonal elements are explicitly set to 1, ensuring that each document has perfect similarity with itself, which is crucial for constructing a valid affinity matrix for spectral clustering.
*   **Step 6: Matrix Normalization for Clustering**
    *   The cosine similarity matrix is normalized using `MinMaxScaler` to rescale its values into the range [0, 1]. This transformation converts the similarity values into an appropriate affinity matrix format, where values represent connection strengths, required by the Spectral Clustering algorithm. Values exceeding 1 are clipped to 1 to maintain the valid range.
*   **Step 7: Spectral Clustering**
    *   Spectral Clustering is applied to the normalized cosine similarity matrix to group news articles into 5 distinct clusters. The `affinity='precomputed'` parameter signals the algorithm to use the pre-calculated similarity matrix directly. A fixed `random_state` ensures reproducibility of the clustering results.
*   **Step 8: Clustering Evaluation**
    *   The quality of the generated clusters is quantitatively assessed using the V-Measure score, comparing the `cluster_labels` against the `true_labels`. The V-Measure, a harmonic mean of homogeneity and completeness, provides a robust evaluation of how well the clusters align with the true categories. A V-Measure of 0.726 was achieved.
*   **Step 9: Dimensionality Reduction for Visualization (t-SNE & UMAP)**
    *   t-Distributed Stochastic Neighbor Embedding (t-SNE) and Uniform Manifold Approximation and Projection (UMAP) are employed to further reduce the PCA-transformed embeddings to 2 dimensions. These techniques are specifically chosen for their ability to preserve local and global data structures, making them ideal for visualizing the clusters and intrinsic patterns in a 2D plot. This allows for an intuitive understanding of cluster separation and density.
*   **Step 10: Support Vector Machine (SVM) Classification**
    *   A Support Vector Machine (SVC) classifier, configured with a radial basis function (RBF) kernel, is trained on the PCA-reduced training embeddings and their `true_labels`. This model learns to differentiate between the article categories.
    *   The trained SVM model is then used to predict categories for the PCA-reduced test embeddings.
    *   Cross-validation (5-fold) is performed on the training data, evaluating the model's F1 score (weighted average) against the `cluster_labels`. An average F1 Score of 0.946 was achieved.
*   **Step 11: Random Forest Classification**
    *   A Random Forest Classifier, initialized with 100 estimators and parallel processing enabled (`n_jobs=-1`), is trained on the PCA-reduced training embeddings and their `true_labels`. Random Forests are robust ensemble models known for their high accuracy.
    *   The trained model predicts categories for the PCA-reduced test embeddings.
    *   Cross-validation (5-fold) is conducted on the training data to evaluate the model's F1 score (weighted average) against the `cluster_labels`. An average F1 Score of 0.944 was achieved.

## 4. Key Configuration & Hyperparameters
| Parameter | Value | Context |
| :--- | :--- | :--- |
| `SentenceTransformer` Model | `all-MiniLM-L6-v2` | Pre-trained model used for generating text embeddings, selected for its balance of performance and efficiency. |
| `PCA` `n_components` | `200` | Number of principal components retained, aiming to capture over 95% of the variance in the embeddings. |
| `SpectralClustering` `n_clusters` | `5` | The target number of clusters for the spectral clustering algorithm, matching the number of known categories. |
| `SpectralClustering` `affinity` | `precomputed` | Specifies that a pre-calculated similarity matrix (cosine similarity) will be used as input. |
| `MinMaxScaler` `feature_range` | `(0, 1)` | The target range for scaling the cosine similarity matrix, making it suitable for spectral clustering. |
| `TSNE` `n_components` | `2` | Reduces embeddings to 2 dimensions for visualization purposes. |
| `TSNE` `perplexity` | `70` | Balance between local and global aspects of the data structure for t-SNE visualization. |
| `TSNE` `max_iter` | `1000` | Maximum number of iterations for the t-SNE optimization. |
| `UMAP` `n_neighbors` | `40` | Controls how UMAP balances local versus global structure in its 2D embedding. |
| `UMAP` `min_dist` | `0.1` | Controls how tightly UMAP points are packed together in the 2D embedding. |
| `UMAP` `metric` | `euclidean` | Distance metric used for UMAP calculations. |
| `UMAP` `n_components` | `2` | Reduces embeddings to 2 dimensions for visualization purposes. |
| `SVC` `kernel` | `rbf` | Specifies the kernel function for the Support Vector Machine classifier. |
| `SVC` `C` | `1.0` | Regularization parameter for the SVM classifier. |
| `SVC` `gamma` | `scale` | Kernel coefficient for 'rbf' kernel in SVM. |
| `RandomForestClassifier` `n_estimators` | `100` | Number of trees in the forest for the Random Forest classifier. |
| `RandomForestClassifier` `n_jobs` | `-1` | Uses all available CPU cores for parallel processing during Random Forest training. |
| `random_state` | `42` | Seed used for random number generators across various models (SpectralClustering, TSNE, UMAP, SVC, RandomForest) to ensure reproducibility. |

## 5. Results & Visualizations
*(This section is currently not implemented.)*

## 6. Artifacts & Storage
*   **Outputs:** None generated.
*   **Location:** None generated.
---
# Notebook: clustering-and-classification-uni documentation

## 1. Executive Summary
This notebook is dedicated to the exploration and application of various clustering algorithms on preprocessed text data. Utilizing TF-IDF vectorization, it demonstrates the process of preparing text for machine learning. The analysis includes methodologies for determining the optimal number of clusters for K-Means, followed by the implementation of K-Means, DBSCAN, and HDBSCAN. Key outcomes involve evaluating cluster formation and density-based clustering results, providing insights into the inherent groupings within the text dataset.

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
*   **Source:** The analysis is performed on preprocessed text data, referred to as `preprocessed_train_data` and `preprocessed_test_data`. An initial sample from `newsgroups_train.data` suggests the original dataset is likely a text corpus such as the 20 Newsgroups dataset, which has been preprocessed prior to this notebook's execution. The specific loading mechanism for `preprocessed_train_data` and `preprocessed_test_data` is not detailed within the provided notebook cells.

## 3. Methodology & Justification
*   **Step 1: Text Data Vectorization with TF-IDF**
    *   The initial step involves converting the preprocessed text data into numerical features suitable for machine learning algorithms. The `TfidfVectorizer` from `sklearn.feature_extraction.text` is used for this purpose. This method assigns weights to words based on their frequency within a document relative to their frequency across all documents (Inverse Document Frequency), effectively highlighting important terms while downplaying common ones. The vectorizer is fitted on the training data and then used to transform both training and testing datasets.
*   **Step 2: K-Means Clustering - Optimal K Determination**
    *   To identify the most suitable number of clusters (`k`) for the K-Means algorithm, two heuristic methods are employed:
        *   **Elbow Method**: K-Means models are trained for a range of `k` values (1 to 25). The inertia (sum of squared distances of samples to their closest cluster center) is calculated for each `k`. A plot of inertia against `k` helps visualize the "elbow point," which often indicates a reasonable `k`.
        *   **Silhouette Score**: For a refined selection, K-Means models are also run for `k` values from 10 to 25. The silhouette score, a measure of how similar an object is to its own cluster compared to other clusters, is computed. The `k` that yields the highest silhouette score is considered optimal, signifying better-defined and separated clusters.
*   **Step 3: K-Means Clustering Execution**
    *   Following the determination of `optimal_clusters` (explicitly set to 20 based on prior analysis), the K-Means algorithm is applied to the TF-IDF vectorized training data. The `random_state` is fixed at 42 to ensure reproducibility, and `n_init=10` ensures the algorithm runs multiple times with different centroid seeds, selecting the best result.
*   **Step 4: DBSCAN Clustering**
    *   DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is implemented as an alternative clustering approach. Prior to DBSCAN, the cosine similarity between the TF-IDF vectors is computed. These similarity values are then normalized using `MinMaxScaler` and converted into a distance matrix (1 - similarity). DBSCAN is then applied using this precomputed distance matrix, enabling the algorithm to identify clusters of varying shapes based on data point density, inherently handling noise points. The silhouette score is calculated for the resulting clusters, excluding any identified noise points.
*   **Step 5: HDBSCAN Clustering**
    *   HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise), an extension of DBSCAN, is also applied. Similar to DBSCAN, it utilizes a precomputed cosine distance matrix, derived from normalized cosine similarities. HDBSCAN is designed to be more robust to varying densities and automatically identifies the number of clusters. Diagonal values of the distance matrix are explicitly set to zero to ensure correct distance interpretations for the algorithm.
*   **Step 6: Connectivity Analysis**
    *   A `kneighbors_graph` is constructed using the TF-IDF vectorized data with `k=10` nearest neighbors, creating a graph representing the local connectivity of data points. Subsequently, `connected_components` from `scipy.sparse.csgraph` is used to count the number of distinct connected components within this graph. This analysis provides insight into the overall structural connectivity of the dataset, potentially indicating underlying natural groupings or partitions.

## 4. Key Configuration & Hyperparameters
| Parameter | Value | Context |
| :--- | :--- | :--- |
| `random_state` | `42` | Seed used for random number generation in K-Means, ensuring reproducibility. |
| `n_init` | `10` | Number of times the K-Means algorithm is run with different centroid seeds. |
| `cluster_range` | `1` to `25` (Elbow) | Range of `k` values tested during the Elbow method for K-Means. |
| `cluster_range` | `10` to `25` (Silhouette) | Range of `k` values tested during the Silhouette score analysis for K-Means. |
| `optimal_clusters` | `20` | The chosen number of clusters for the final K-Means model. |
| `eps` (DBSCAN) | `0.4` | The maximum distance between two samples for one to be considered as in the neighborhood of the other. |
| `min_samples` (DBSCAN, HDBSCAN) | `5` | The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. |
| `min_cluster_size` (HDBSCAN) | `5` | The minimum number of samples in a cluster. Smaller clusters will be considered noise. |
| `k` (kneighbors_graph) | `10` | Number of nearest neighbors used to construct the connectivity graph. |

## 5. Results & Visualizations
*   **TF-IDF Vectorization Outputs:**
    *   Original Sample: A sample of the raw input text.
    *   Preprocessed Sample: A sample of the text after preprocessing.
    *   TF-IDF Vectorized Shape (Training): `(11314, 130101)` (Example dimensions).
    *   TF-IDF Vectorized Shape (Testing): `(7532, 130101)` (Example dimensions).
*   **K-Means Optimal K Determination:**
    *   An "Elbow Method for Optimal K" plot was generated, visualizing inertia against the number of clusters (k).
    *   A "Silhouette Score for Optimal K" plot was generated, showing silhouette scores against the number of clusters (k).
    *   Optimal number of clusters based on silhouette score: `20`.
*   **K-Means Clustering Execution:**
    *   K-Means clustering performed with `20` clusters.
    *   Cluster labels for the training data (first 10 samples) were printed.
*   **DBSCAN Clustering:**
    *   DBSCAN Clustering Labels: The array of cluster assignments, including noise points (-1).
    *   Number of Clusters: [Identified number of clusters, e.g., 1].
    *   Number of Noise Points: [Count of samples identified as noise, e.g., 2].
    *   Silhouette Score: [Calculated silhouette score, e.g., 0.8569] (if more than 1 cluster).
*   **HDBSCAN Clustering:**
    *   HDBSCAN Clustering Labels: The array of cluster assignments, including noise points (-1).
    *   Number of Clusters: [Identified number of clusters, e.g., 1].
    *   Number of Noise Points: [Count of samples identified as noise, e.g., 2].
*   **Connectivity Analysis:**
    *   Number of connected components: [Calculated number of connected components, e.g., 1].
*   **Observation:** The analysis systematically explored various clustering algorithms, with K-Means demonstrating a defined optimal cluster count. DBSCAN and HDBSCAN provided density-based clustering results, indicating their ability to find clusters of varying shapes and identify noise. The diagonal values of distance matrices were verified to be zero, which is critical for precomputed metric usage in some algorithms.

## 6. Artifacts & Storage
*   **Outputs:** None detected.
*   **Location:** None detected.

---