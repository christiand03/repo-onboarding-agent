# Notebook Documentation: predicting-power-consumption-uni documentation

## 1. Executive Summary
This notebook focuses on predicting future power consumption and factory output. It addresses the challenge of forecasting these metrics using both Random Forest Regression and Neural Network models, aiming to provide insights into future operational demands. The methodology involves comprehensive data preparation, including feature engineering from timestamps and merging various environmental datasets. Both models demonstrate high predictive accuracy, consistently achieving R2 scores above 95%, indicating reliable forecasts for the next three days with predictions of less power consumption and volatility compared to historical trends.

## 2. Technical Prerequisites
### Environment
*   **Dependencies:**
    *   pandas
    *   numpy
    *   matplotlib
    *   scikit-learn
    *   tensorflow
    *   torch
*   **External Configuration:** None detected.
### Data Lineage
*   **Source:**
    *   `StudentsData2.tab` (Historical operational data)
    *   `data_OBS_DEU_PT1H_T2M.csv` (Historical temperature data)
    *   `data_OBS_DEU_PT1H_SD.csv` (Historical sunshine data)
    *   `data_OBS_DEU_PT1H_RF.csv` (Historical humidity data)
    *   `PredictTemp.csv` (Future temperature prediction data)
    *   `Predicthumidity.csv` (Future humidity prediction data)
    *   `PredictSun.csv` (Future sunshine prediction data)

## 3. Methodology & Justification
*   **Step 1: Historical Data Preparation**
    *   **Data Ingestion and Initial Cleaning:** The process began by loading historical operational data from `StudentsData2.tab` alongside weather data (temperature, sunshine, humidity) from three separate CSV files. Key columns were consistently renamed (e.g., "Wert" to "Temperature") for unified processing.
    *   **Feature Engineering from Timestamps:** The `Zeitstempel` column in all datasets was converted to a datetime format. This timestamp was then extensively engineered by splitting it into `Day`, `Month`, `Year`, `Hour`, and `Minutes` components. This decomposition was explicitly noted by the original author to enhance model accuracy by better capturing temporal patterns.
    *   **Data Merging and Structuring:** The weather datasets were merged first, followed by a merge with the main operational data, using `Zeitstempel` as the key. Missing values in `SunshineMinutes` were imputed with 0. This resulted in two primary dataframes: `merged_df` (containing features for factory output prediction, excluding power consumption) and `merged_df2` (the main dataframe, including both factory output and power consumption). Irrelevant original timestamp columns were subsequently dropped.
    *   **Type Conversion:** Critical temporal features (`Day`, `Month`, `Year`, `Hour`) were converted to `int64` to ensure proper numerical handling by the machine learning models.

*   **Step 2: Future Prediction Data Preparation**
    *   **Future Data Ingestion:** Separate datasets containing future weather predictions were loaded (`PredictTemp.csv`, `Predicthumidity.csv`, `PredictSun.csv`).
    *   **Consistent Preprocessing:** These future prediction datasets underwent the exact same preprocessing steps as the historical data, including column renaming, dropping of initial columns, datetime conversion, formatting, and splitting of the `Zeitstempel` into granular time features.
    *   **Merged Future Dataframe Creation:** The processed future weather dataframes were merged to create `merged_dfpred`, which serves as the input for generating future factory output and power consumption predictions.

*   **Step 3: Random Forest Regression Model Development**
    *   **Data Splitting:** Historical features and target variables (Factory Output and Power Consumption) were extracted. The datasets were then partitioned into training, validation, and testing sets using a 80/10/10 split with `random_state=42` for reproducibility.
    *   **Model Definition and Training:** Two `RandomForestRegressor` models, each configured with `n_estimators=100` and `random_state=42`, were initialized and trained. One model predicted factory output based on temporal and weather features, while the other predicted power consumption using temporal, weather, and historical manufacturing process data.
    *   **Prediction Workflow:** To predict future power consumption, the trained factory output model (`rf_factory_output`) first generated predictions for future factory output using `future_features`. These predicted factory output values were then concatenated with the `future_features` to serve as input for the power consumption model (`rf_power_consumption`), which then produced the final power consumption forecasts.
    *   **Justification and Evaluation:** Random Forest Regression was selected for its high predictive accuracy, ability to model complex non-linear relationships, and robustness to overfitting, particularly after a preliminary linear regression model proved unsuitable for the task. The models were evaluated using Mean Squared Error (MSE) and R2 Score on their respective test sets. The results demonstrated strong performance, with an R2 Score of 0.973 for Power Consumption and 0.999 for Factory Output, indicating excellent fit to the data.

*   **Step 4: Neural Network Model Development**
    *   **Data Splitting and Scaling:** Features for both factory output and power consumption prediction were extracted from `merged_df2`. The data was split into training and testing sets (80/20 split). `MinMaxScaler` was applied to the factory output features to normalize the input data, which is crucial for neural network performance.
    *   **Factory Output Neural Network:** A sequential Keras model was constructed. It comprised an input layer, two dense hidden layers (256 and 128 neurons respectively) using 'relu' activation, and an output layer with 'sigmoid' activation. The model was compiled using the Nadam optimizer with a learning rate of 0.002 and trained for 100 epochs with a batch size of 16. The specific architecture and hyperparameters were informed by a grid search (see Step 5).
    *   **Power Consumption Neural Network:** A second sequential Keras model was developed for power consumption prediction. This network used dense layers with 128 and 64 neurons, 'relu' activation, and a final 'sigmoid' output layer. It was compiled with the Nadam optimizer and a learning rate of 0.001, trained for 100 epochs with a batch size of 16. The author noted that grid search results were not used for this model due to suboptimal predictions during initial testing.
    *   **Future Predictions with NN:** The `merged_dfpred` (future features) was scaled using the factory output `MinMaxScaler`. The factory output NN then predicted future factory output. These predictions were combined with the original future features to form the input for the power consumption NN, which then generated the final power consumption forecasts.
    *   **Evaluation:** The Neural Network models were evaluated using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R2 Score. The R2 scores were 0.989 for Factory Output and 0.952 for Power Consumption, indicating a strong ability to explain the variance in the test set.

*   **Step 5: Hyperparameter Tuning (Grid Search)**
    *   A `GridSearchCV` was implemented to find optimal hyperparameters for the factory output Neural Network. The search space included `hidden_units_layer1` (64, 128, 256), `hidden_units_layer2` (32, 64, 128), `learning_rate` (0.001, 0.01, 0.002), and `batch_size` (16, 32, 64). The best parameters identified were a `batch_size` of 16, 256 neurons for the first hidden layer, 128 neurons for the second hidden layer, and a `learning_rate` of 0.002, resulting in a best MSE of 0.000796. A grid search was intentionally omitted for the power consumption model due to its computational intensity and the marginal improvements observed during manual testing.

*   **Step 6: Comparative Analysis and Insights**
    *   **Model Prediction Comparison:** A direct comparison of predictions from both the Random Forest and Neural Network models revealed significant similarities in power consumption trends. While the Neural Network showed slightly more volatility in factory output predictions, the overall patterns were alike. An interesting "mirroring effect" in factory output trends on the third day was observed between the two models, for which the cause was not definitively determined.
    *   **Historical Contextualization:** Analysis of the last 72 hours of historical factory output and power consumption data provided context for the immediate future predictions. Both models consistently predicted an approximate 10% drop in factory output immediately following the historical data, which was deemed reasonable given the unknown real-world scale of the values.
    *   **Causation Identification:** Exploratory plots indicated a strong correlation between historical power consumption and temperature, reinforcing confidence in the temperature-driven aspects of the predictions. Additional plots comparing factory output and power consumption confirmed that large historical differences between these two metrics were not uncommon.

## 4. Key Configuration & Hyperparameters
| Parameter                   | Value                                                               | Context                                                                                                                                                                                                                                    |
| :-------------------------- | :------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RandomForestRegressor`     | `n_estimators=100`                                                  | Number of trees in the forest for both factory output and power consumption models.                                                                                                                                                          |
| `RandomForestRegressor`     | `random_state=42`                                                   | Seed for random number generation to ensure reproducibility in Random Forest models.                                                                                                                                                         |
| `NN_FactoryOutput_Layer1`   | `256` neurons, `relu` activation                                    | First hidden layer in the factory output Neural Network.                                                                                                                                                                                   |
| `NN_FactoryOutput_Layer2`   | `128` neurons, `relu` activation                                    | Second hidden layer in the factory output Neural Network.                                                                                                                                                                                  |
| `NN_FactoryOutput_Output`   | `1` neuron, `sigmoid` activation                                    | Output layer for the factory output prediction Neural Network.                                                                                                                                                                             |
| `NN_FactoryOutput_LR`       | `0.002`                                                             | Learning rate used by the Nadam optimizer for the factory output Neural Network.                                                                                                                                                           |
| `NN_FactoryOutput_Epochs`   | `100`                                                               | Number of training epochs for the factory output Neural Network.                                                                                                                                                                           |
| `NN_FactoryOutput_BatchSize`| `16`                                                                | Batch size used during the training of the factory output Neural Network.                                                                                                                                                                  |
| `NN_PowerConsumption_Layer1`| `128` neurons, `relu` activation                                    | First hidden layer in the power consumption Neural Network.                                                                                                                                                                                |
| `NN_PowerConsumption_Layer2`| `64` neurons, `relu` activation                                     | Second hidden layer in the power consumption Neural Network.                                                                                                                                                                               |
| `NN_PowerConsumption_Output`| `1` neuron, `sigmoid` activation                                    | Output layer for the power consumption prediction Neural Network.                                                                                                                                                                          |
| `NN_PowerConsumption_LR`    | `0.001`                                                             | Learning rate used by the Nadam optimizer for the power consumption Neural Network.                                                                                                                                                        |
| `NN_PowerConsumption_Epochs`| `100`                                                               | Number of training epochs for the power consumption Neural Network.                                                                                                                                                                        |
| `NN_PowerConsumption_BatchSize`| `16`                                                                | Batch size used during the training of the power consumption Neural Network.                                                                                                                                                               |
| `GridSearch_Param_Range`    | `hidden_units_layer1: [64, 128, 256]`, `hidden_units_layer2: [32, 64, 128]`, `learning_rate: [0.001, 0.01, 0.002]`, `batch_size: [16, 32, 64]` | The range of hyperparameters explored during the Grid Search for optimizing the factory output Neural Network.                                                                                                                             |
| `GridSearch_Best_Params`    | `{'batch_size': 16, 'hidden_units_layer1': 256, 'hidden_units_layer2': 128, 'learning_rate': 0.002}` | The optimal combination of hyperparameters identified by the Grid Search for the factory output Neural Network, resulting in the lowest mean squared error. |

## 5. Results & Visualizations
[This section is not implemented yet]

## 6. Artifacts & Storage
*   **Outputs:** No explicit artifacts (e.g., trained models saved as `.pkl` or `.h5`, final prediction dataframes saved as `.csv`) were saved to disk within the provided notebook.
*   **Location:** Not applicable.

---