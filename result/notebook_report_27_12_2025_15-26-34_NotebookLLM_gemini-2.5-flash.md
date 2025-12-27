# Notebook (DSF_Project_clustering_classification.ipynb): clustering-and-classification-uni documentation

## 1. Executive Summary
This notebook presents a comprehensive workflow for clustering and classifying BBC News articles. It encompasses robust text preprocessing, advanced semantic embedding generation using Sentence-BERT, and dimensionality reduction via PCA. The processed data is then utilized for unsupervised learning, specifically Spectral Clustering, which achieved a V-measure of 0.726. Subsequently, supervised classification models (Support Vector Machine and Random Forest) were trained, demonstrating strong performance with average F1-scores of 0.946 and 0.944, respectively, for categorizing news content.

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
*   **External Configuration:**
    *   **Warning:** Hardcoded local file paths (`C:\Users\Debbertin\Downloads\BBC News Train.csv`, `C:\Users\Debbertin\Downloads\BBC News Test.csv`) are used for dataset loading. For production environments, these should be replaced with configurable paths, environment variables, or secure data access methods.
    *   NLTK data (stopwords, wordnet, omw-1.4) is downloaded programmatically.
    *   No environment variables (e.g., `DB_PASSWORD`, `API_KEY`) detected.

### Data Lineage
*   **Source:**
    *   Local CSV files: `C:\Users\Debbertin\Downloads\BBC News Train.csv` (training data)
    *   Local CSV files: `C:\Users\Debbertin\Downloads\BBC News Test.csv` (testing data)

## 3. Methodology & Justification
### Step 1: Environment Setup & Data Loading
*   **Description of logic:** The notebook begins by importing essential libraries for data manipulation, visualization, natural language processing, dimensionality reduction, clustering, and classification. NLTK resources (stopwords and WordNet) are downloaded and initialized. A `preprocess_text` function is defined to clean text by lowercasing, removing punctuation, tokenizing, filtering stopwords, and lemmatizing. The BBC News dataset is loaded from local CSV files into Pandas DataFrames, and the raw text is preprocessed. True category labels are extracted from the training data and converted into numerical codes for subsequent evaluation.
*   **Justification:** This initial step establishes the necessary software environment and prepares the raw text data into a cleaner, more standardized format suitable for numerical encoding and machine learning tasks. Preprocessing ensures consistency and reduces noise, which is critical for effective text analysis.

### Step 2: Text Embedding Generation
*   **Description of logic:** The `SentenceTransformer` model `all-MiniLM-L6-v2` is used to generate dense vector embeddings for both the preprocessed training and testing text data. These embeddings are then normalized to unit length using `sklearn.preprocessing.normalize`.
*   **Justification:** Semantic embeddings capture the contextual meaning of sentences, enabling machine learning models to work with richer representations than traditional bag-of-words approaches. Normalization is a common practice before calculating similarity metrics, ensuring that vector length does not disproportionately influence similarity scores.

### Step 3: Dimensionality Reduction (PCA)
*   **Description of logic:** Principal Component Analysis (PCA) is applied to the normalized embeddings. For the training data, PCA is configured to retain `n_components=200`, which resulted in preserving 95.84% of the total variance. The same `n_components` is used for the test data, retaining 96.88% of its total variance. Cumulative variance plots are generated for visual inspection.
*   **Justification:** Dimensionality reduction helps mitigate the curse of dimensionality, reduce computational cost, and potentially improve model performance by removing noise while retaining most of the essential information in the high-dimensional embeddings. A target of 95% variance retention balances information preservation with dimensionality reduction.

### Step 4: Cosine Similarity Matrix Construction & Normalization
*   **Description of logic:** A cosine similarity matrix is computed from the PCA-reduced training embeddings (`X_pca`) to measure the similarity between all pairs of documents. The matrix is checked for NaN values, symmetry, and non-negativity. The diagonal elements, representing self-similarity, are explicitly set to 1. The entire matrix is then scaled to a range of [0, 1] using `MinMaxScaler` for optimal input to spectral clustering algorithms.
*   **Justification:** Cosine similarity is suitable for measuring the angular similarity between text embeddings, effectively gauging semantic relatedness. Ensuring matrix properties (no NaNs, symmetry) and normalizing the scale are crucial prerequisites for the stability and performance of graph-based clustering algorithms like Spectral Clustering.

### Step 5: Spectral Clustering
*   **Description of logic:** Spectral Clustering is performed on the normalized cosine similarity matrix. The model is initialized with `n_clusters=5`, `affinity='precomputed'` (as a similarity matrix is provided), and `random_state=42` for reproducibility. The resulting `cluster_labels` are then evaluated against the `true_labels` using the V-measure score.
*   **Justification:** Spectral Clustering is well-suited for discovering arbitrarily shaped clusters and leveraging the underlying graph structure defined by the similarity matrix. Choosing 5 clusters aligns with the common understanding of BBC News categories. The V-measure provides a balanced assessment of clustering quality, considering both homogeneity and completeness.

### Step 6: Dimensionality Reduction for Visualization (t-SNE & UMAP)
*   **Description of logic:** t-SNE (t-Distributed Stochastic Neighbor Embedding) is applied to the PCA-reduced embeddings (`X_pca`) with `n_components=2`, `perplexity=70`, and `max_iter=1000` to create a 2D projection suitable for visualization. Similarly, UMAP (Uniform Manifold Approximation and Projection) is applied with `n_neighbors=40`, `min_dist=0.1`, `metric="euclidean"`, and `n_components=2` to provide an alternative 2D visualization.
*   **Justification:** t-SNE and UMAP are powerful non-linear dimensionality reduction techniques that are particularly effective at preserving local and global data structures, respectively, in a low-dimensional space. These projections allow for visual inspection of the clusters identified by Spectral Clustering, helping to understand their separability and density.

### Step 7: Supervised Classification (SVM & Random Forest)
*   **Description of logic:**
    *   A Support Vector Machine (SVC) model, configured with an RBF kernel (`C=1.0`, `gamma='scale'`) and `random_state=42`, is trained on the PCA-reduced training data (`X_pca`) and `true_labels`. The model's performance is then evaluated using 5-fold cross-validation on the training set, calculating the weighted F1-score.
    *   A RandomForestClassifier is initialized with `n_estimators=100`, `random_state=42`, and `n_jobs=-1` (to utilize all available CPU cores). This model is also trained on `X_pca` and `true_labels`, and its performance is assessed via 5-fold cross-validation with a weighted F1-score. Predictions are also made on the PCA-reduced test data for both models.
*   **Justification:** After exploring unsupervised clustering, supervised classification models are employed to build a predictive system for categorizing news articles. SVMs are effective for high-dimensional data and can find optimal hyperplanes for separation. Random Forests, as ensemble methods, are robust against overfitting and provide good generalization performance. Cross-validation ensures a reliable estimate of model performance on unseen data.

## 4. Key Configuration & Hyperparameters (only if applicable)
| Parameter | Value | Context |
| :--- | :--- | :--- |
| `model` (SentenceTransformer) | `all-MiniLM-L6-v2` | Pre-trained model selected for generating text embeddings, chosen for its balance of performance and efficiency. |
| `n_components` (PCA) | 200 | Number of principal components retained, chosen to capture approximately 95% of the variance. |
| `n_clusters` (SpectralClustering) | 5 | The target number of clusters, corresponding to the expected number of distinct news categories. |
| `random_state` | 42 | A fixed seed used across multiple algorithms (Spectral Clustering, t-SNE, UMAP, SVM, RandomForest) to ensure reproducibility of results. |
| `perplexity` (t-SNE) | 70 | Parameter for t-SNE, influencing the balance between preserving local and global data structures in the embedding. |
| `max_iter` (t-SNE) | 1000 | Maximum iterations for the t-SNE optimization process, ensuring convergence. |
| `n_neighbors` (UMAP) | 40 | Parameter for UMAP, controlling the size of the local neighborhood used for manifold approximation. |
| `min_dist` (UMAP) | 0.1 | Parameter for UMAP, governing how tightly packed points are allowed to be in the low-dimensional representation. |
| `metric` (UMAP) | `euclidean` | Distance metric used in UMAP for computing distances in the input space. |
| `kernel` (SVC) | `rbf` | The type of kernel function used in the Support Vector Machine, allowing for non-linear decision boundaries. |
| `C` (SVC) | 1.0 | Regularization parameter in the SVM, balancing misclassification with margin maximization. |
| `gamma` (SVC) | `scale` | Kernel coefficient for the RBF kernel, implicitly scaled by the number of features. |
| `n_estimators` (RandomForestClassifier) | 100 | The number of decision trees in the Random Forest ensemble. |
| `n_jobs` (RandomForestClassifier) | -1 | Configures the Random Forest to use all available processor cores for parallel execution, speeding up training. |

## 5. Results & Visualizations
*   **V-Measure (Spectral Clustering):** 0.72581
    *   **Observation:** A V-measure of approximately 0.726 indicates a reasonably good clustering performance, demonstrating a balance between the homogeneity and completeness of the clusters relative to the true category labels.
*   **Average F1 Score (Support Vector Machine):** 0.946
    *   **Observation:** The SVM model achieved a high average F1 score of 0.946 during cross-validation, suggesting strong performance in classifying news articles across categories.
*   **Average F1 Score (Random Forest Classifier):** 0.944
    *   **Observation:** The Random Forest model also performed very well, with an average F1 score of 0.944 from cross-validation, confirming its effectiveness in this classification task.
*   **t-SNE Visualization of Clusters:** A scatter plot generated from t-SNE reduced features, colored by the Spectral Clustering labels. This visualization aims to show the spatial separation and grouping of the identified clusters in a 2D space.
*   **UMAP Visualization of Clusters:** A scatter plot generated from UMAP reduced features, colored by the Spectral Clustering labels. This offers an alternative 2D projection to visualize cluster structures, often providing a more cohesive representation than t-SNE for global structures.

## 6. Artifacts & Storage
*   **Outputs:** None detected.
*   **Location:** None detected.

---


# Notebook (DSF_Project_legacy_code.ipynb): clustering-and-classification-uni documentation

## 1. Executive Summary
This notebook focuses on exploring various unsupervised learning techniques, primarily clustering algorithms, for text data. It commences with the vectorization of preprocessed text using TF-IDF. Subsequently, it applies and evaluates K-Means, DBSCAN, and HDBSCAN clustering methods. Evaluation metrics such as the Elbow method, Silhouette score, and graph connectivity analysis are employed to determine optimal parameters and assess the quality of the resulting clusters. The overarching objective is to identify inherent groupings and structural patterns within the text dataset.

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
*   **Source:** The notebook processes `preprocessed_train_data` and `preprocessed_test_data`. An example print statement mentions `newsgroups_train.data`, indicating the raw data is likely derived from a newsgroup dataset.

## 3. Methodology & Justification
*   **Step 1: Text Data Vectorization with TF-IDF**
    *   **Description:** The initial step involves converting raw text data into a numerical format suitable for machine learning algorithms. This is achieved using `TfidfVectorizer` from `sklearn.feature_extraction.text`. This process transforms the `preprocessed_train_data` and `preprocessed_test_data` into TF-IDF (Term Frequency-Inverse Document Frequency) feature vectors, which quantify the importance of words in a document relative to the entire corpus.
    *   **Justification:** TF-IDF is a widely adopted technique for text representation due to its effectiveness in capturing semantic importance and normalizing for document length, enabling robust analysis by clustering algorithms.
*   **Step 2: K-Means Clustering - Optimal `k` Determination**
    *   **Description:** To identify the most suitable number of clusters (`k`) for K-Means, two common heuristics are employed: the Elbow Method and the Silhouette Score.
        *   The **Elbow Method** iterates K-Means for a range of `k` values (1 to 25) and plots the inertia (sum of squared distances of samples to their closest cluster center). The "elbow" point in the plot typically indicates a good balance between the number of clusters and the explained variance.
        *   The **Silhouette Score** is computed for a range of `k` values (10 to 25). This metric measures the similarity of an object to its own cluster compared to other clusters, with higher values indicating better-defined clusters. The `k` that maximizes this score is selected as optimal.
    *   **Justification:** These methods provide quantitative insights into the inherent clustering structure of the data, guiding the selection of a robust `k` and avoiding arbitrary parameter choices for K-Means.
*   **Step 3: K-Means Clustering - Application**
    *   **Description:** Following the determination of an optimal number of clusters, K-Means clustering is performed on the TF-IDF vectorized training data. The `optimal_clusters` value, hardcoded to 20 based on previous analysis, is used. The algorithm partitions data points into `k` clusters, where each data point belongs to the cluster with the nearest mean (centroid).
    *   **Justification:** K-Means is a computationally efficient and widely used partitioning algorithm, suitable for datasets where clusters are expected to be somewhat spherical and equally sized.
*   **Step 4: DBSCAN Clustering**
    *   **Description:** DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is applied to the data. Prior to DBSCAN, the cosine similarity between the TF-IDF vectors is computed, normalized using `MinMaxScaler`, and then converted into a cosine distance matrix (1 - similarity). DBSCAN is then executed with `metric='precomputed'`, `eps=0.4`, and `min_samples=5`. The algorithm identifies dense regions as clusters and marks points in sparse regions as noise. A silhouette score is calculated for the resulting clusters, explicitly excluding noise points.
    *   **Justification:** DBSCAN is valuable for discovering arbitrarily shaped clusters and robustly identifying outliers in datasets where clusters may not be spherical. Using cosine distance is particularly appropriate for high-dimensional textual data.
*   **Step 5: HDBSCAN Clustering**
    *   **Description:** HDBSCAN (Hierarchical DBSCAN), an advanced density-based clustering algorithm, is applied using the same precomputed cosine distance matrix. It constructs a hierarchical representation of clusters and then extracts a flat partitioning based on cluster stability. Parameters `min_cluster_size=5` and `min_samples=5` are specified. Diagonal values of the distance matrix are explicitly set to zero to ensure proper metric interpretation.
    *   **Justification:** HDBSCAN improves upon DBSCAN by automatically detecting the number of clusters and handling varying cluster densities more effectively, making it a powerful tool for complex, real-world datasets and less sensitive to parameter tuning.
*   **Step 6: Connectivity Analysis**
    *   **Description:** A k-nearest neighbors graph is constructed from the TF-IDF vectorized training data using `kneighbors_graph` with `n_neighbors=10` and `mode='connectivity'`. This creates an adjacency matrix where edges exist between nearest neighbors. Subsequently, the number of connected components within this graph is calculated using `scipy.sparse.csgraph.connected_components`.
    *   **Justification:** Analyzing connected components provides insights into the global connectivity and inherent structure of the data, which can be indicative of natural groupings or the presence of isolated data points.

## 4. Key Configuration & Hyperparameters
| Parameter          | Value           | Context                                                                    |
| :----------------- | :-------------- | :------------------------------------------------------------------------- |
| `TfidfVectorizer`  | Default         | Default parameters used for text vectorization.                            |
| `cluster_range` (K-Means) | 1-25 (Elbow), 10-25 (Silhouette) | Range of cluster numbers explored for optimal `k`.                         |
| `random_state`     | 42              | Seed for K-Means initialization, ensuring reproducibility of centroids.    |
| `n_init`           | 10              | Number of times K-Means is run with different centroid seeds.              |
| `optimal_clusters` | 20              | The chosen number of clusters for the final K-Means model.                 |
| `DBSCAN.eps`       | 0.4             | Maximum distance between two samples for one to be considered as in the neighborhood of the other. |
| `DBSCAN.min_samples` | 5             | Number of samples (or total weight) in a neighborhood for a point to be considered as a core point. |
| `HDBSCAN.min_cluster_size` | 5       | The minimum number of samples in a cluster.                                |
| `HDBSCAN.min_samples` | 5            | The number of samples in a neighborhood for a point to be considered a core point, influencing cluster density. |
| `kneighbors_graph.n_neighbors` | 10  | Number of nearest neighbors to consider when building the connectivity graph. |

## 5. Results & Visualizations
*   **K-Means Optimal Clusters:** The analysis indicated an optimal number of clusters for K-Means based on the silhouette score.
    *   **Observation:** The notebook shows that the optimal number of clusters based on the silhouette score calculation was identified. While the exact value isn't explicitly printed in the final cell, the subsequent K-Means execution uses `optimal_clusters = 20`.
*   **DBSCAN Clustering Output:**
    *   **Observation:** DBSCAN identified multiple clusters and a significant number of noise points. For example, a run might produce `Number of Clusters: 20` and `Number of Noise Points: 110`. The calculated Silhouette Score for the DBSCAN clusters (excluding noise) provides a measure of cluster cohesion and separation.
*   **HDBSCAN Clustering Output:**
    *   **Observation:** HDBSCAN also identified multiple clusters and noise points, similar to DBSCAN but potentially with different cluster structures due to its hierarchical approach. For example, a run might produce `Number of Clusters: 20` and `Number of Noise Points: 20`.
*   **Connectivity Analysis:**
    *   **Observation:** The k-nearest neighbors graph analysis revealed `n_connected_components` which gives insight into the overall connectivity of the dataset.

## 6. Artifacts & Storage
*   **Outputs:** No explicit file outputs (e.g., `.csv`, `.pkl`, `.json`, `.model`) are generated or saved within the provided notebook cells.
*   **Location:** None.

---