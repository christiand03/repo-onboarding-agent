```python
import numpy as np
import pandas as matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.exceptions import ConvergenceWarning
import warnings

# Suppress ConvergenceWarning for MLPRegressor
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# --- 1. Data Generation (Simulated) ---
def generate_simulated_data(num_samples=1000):
    np.random.seed(42)
    data = {
        'Age': np.random.randint(20, 60, num_samples),
        'Experience': np.random.randint(0, 30, num_samples),
        'Education_Level': np.random.choice(['High School', 'Bachelors', 'Masters', 'PhD'], num_samples),
        'City': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], num_samples),
        'Project_Count': np.random.randint(1, 20, num_samples),
        'Client_Satisfaction_Score': np.random.uniform(3.0, 5.0, num_samples),
        'Hours_Worked_Per_Week': np.random.randint(30, 60, num_samples),
        'Performance_Score': np.random.uniform(60, 100, num_samples)
    }
    df = pd.DataFrame(data)

    # Introduce some missing values
    for col in ['Experience', 'Project_Count', 'Client_Satisfaction_Score']:
        missing_indices = np.random.choice(df.index, int(num_samples * 0.05), replace=False)
        df.loc[missing_indices, col] = np.nan

    # Simulate 'Salary' based on other features with some noise
    df['Salary'] = (
        1000 * df['Age'] +
        500 * df['Experience'].fillna(df['Experience'].mean()) +
        (df['Education_Level'].map({'High School': 0, 'Bachelors': 10000, 'Masters': 20000, 'PhD': 30000})) +
        (df['City'].map({'New York': 15000, 'Los Angeles': 10000, 'Chicago': 5000, 'Houston': 0, 'Phoenix': -5000})) +
        700 * df['Project_Count'].fillna(df['Project_Count'].mean()) +
        2000 * df['Client_Satisfaction_Score'].fillna(df['Client_Satisfaction_Score'].mean()) +
        100 * df['Hours_Worked_Per_Week'] +
        150 * df['Performance_Score'] +
        np.random.normal(0, 10000, num_samples) # Noise
    )
    return df

df = generate_simulated_data()
print("Simulated Data Head:")
print(df.head())
print("\nData Info:")
df.info()

# --- 2. Exploratory Data Analysis (EDA) ---
print("\n--- Exploratory Data Analysis ---")

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe(include='all'))

# Distribution of Salary
plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], kde=True)
plt.title('Distribution of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Correlation Matrix for numerical features
plt.figure(figsize=(12, 8))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# Pairplot for selected numerical features (can be slow for many features/samples)
# sns.pairplot(df[['Age', 'Experience', 'Project_Count', 'Salary']])
# plt.suptitle('Pairplot of Selected Numerical Features', y=1.02)
# plt.show()

# Box plots for categorical features vs. Salary
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x='Education_Level', y='Salary', data=df, order=['High School', 'Bachelors', 'Masters', 'PhD'])
plt.title('Salary by Education Level')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
sns.boxplot(x='City', y='Salary', data=df)
plt.title('Salary by City')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 3. Feature Engineering & Preprocessing ---
print("\n--- Feature Engineering & Preprocessing ---")

# Define features (X) and target (y)
X = df.drop('Salary', axis=1)
y = df['Salary']

# Identify categorical and numerical features
categorical_features = X.select_dtypes(include='object').columns
numerical_features = X.select_dtypes(include=np.number).columns

# Create preprocessing pipelines for numerical and categorical features
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')), # Impute missing numerical values with the mean
    ('scaler', StandardScaler()) # Scale numerical features
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')), # Impute missing categorical values with the most frequent
    ('onehot', OneHotEncoder(handle_unknown='ignore')) # One-hot encode categorical features
])

# Create a column transformer to apply different transformations to different columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# --- 4. Model Training and Evaluation ---
print("\n--- Model Training and Evaluation ---")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a dictionary of models to evaluate
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree Regressor': DecisionTreeRegressor(random_state=42),
    'Random Forest Regressor': RandomForestRegressor(random_state=42, n_estimators=100),
    'Gradient Boosting Regressor': GradientBoostingRegressor(random_state=42, n_estimators=100),
    'Support Vector Regressor': SVR(), # SVR can be very slow on larger datasets
    'K-Neighbors Regressor': KNeighborsRegressor(),
    'MLP Regressor': MLPRegressor(random_state=42, max_iter=500) # Increased max_iter
}

results = {}

for name, model in models.items():
    print(f"\nTraining {name}...")
    # Create a pipeline that first preprocesses the data and then trains the model
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('regressor', model)])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Make predictions
    y_pred = pipeline.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    results[name] = {'MSE': mse, 'RMSE': rmse, 'R2': r2}

    print(f"{name} - Mean Squared Error: {mse:.2f}")
    print(f"{name} - Root Mean Squared Error: {rmse:.2f}")
    print(f"{name} - R-squared: {r2:.2f}")

# --- 5. Results Visualization ---
print("\n--- Results Visualization ---")

results_df = pd.DataFrame(results).T
print("\nModel Performance Comparison:")
print(results_df)

# Plotting R-squared scores
plt.figure(figsize=(12, 7))
sns.barplot(x=results_df.index, y=results_df['R2'], palette='viridis')
plt.title('R-squared Score Comparison Across Models')
plt.xlabel('Model')
plt.ylabel('R-squared Score')
plt.ylim(0, 1)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plotting RMSE scores
plt.figure(figsize=(12, 7))
sns.barplot(x=results_df.index, y=results_df['RMSE'], palette='magma')
plt.title('RMSE Score Comparison Across Models')
plt.xlabel('Model')
plt.ylabel('RMSE Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- 6. Model Deployment (Example with the best model) ---
print("\n--- Model Deployment Example ---")

# Identify the best model based on R-squared
best_model_name = results_df['R2'].idxmax()
print(f"\nBest performing model based on R-squared: {best_model_name}")

# Retrain the best model on the full dataset (optional, but good practice for deployment)
# For simplicity, we'll just use the pipeline from the evaluation loop
best_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                 ('regressor', models[best_model_name])])
best_pipeline.fit(X, y) # Train on full data

# Example of making a prediction for a new, unseen data point
print("\nMaking a prediction for a new employee:")
new_employee_data = pd.DataFrame([{
    'Age': 35,
    'Experience': 10,
    'Education_Level': 'Bachelors',
    'City': 'New York',
    'Project_Count': 8,
    'Client_Satisfaction_Score': 4.2,
    'Hours_Worked_Per_Week': 45,
    'Performance_Score': 88
}])

# Ensure the new data has the same columns as the training data
# and handle potential missing values if they were present in the original X
# (though in this specific example, new_employee_data is complete)
predicted_salary = best_pipeline.predict(new_employee_data)
print(f"Predicted Salary for new employee: ${predicted_salary[0]:,.2f}")

# Example with missing values in new data
new_employee_data_missing = pd.DataFrame([{
    'Age': 40,