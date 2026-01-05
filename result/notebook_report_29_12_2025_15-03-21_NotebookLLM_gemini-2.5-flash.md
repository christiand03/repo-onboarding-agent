# Notebook (Project_Predicting_Power_Consumption.ipynb): predicting-power-consumption-uni documentation

## 1. Executive Summary
This notebook addresses the challenge of predicting factory power consumption and output for future periods. It evaluates two distinct methodologies: Random Forest Regression and a Neural Network approach. Both models are trained on historical data, which includes time-series information, detailed weather conditions (temperature, humidity, sunshine), and historical factory output and power consumption. The rigorous preprocessing steps ensure data suitability, and both models demonstrate high predictive accuracy, with R2 scores consistently above 0.95. The final comparison of predictions reveals highly similar trends, particularly for power consumption, indicating robust and consistent model performance. The models predict a less volatile future power consumption without the spikes observed in historical data.

## 2. Technical Prerequisites
### Environment
*   **Dependencies:**
    *   pandas
    *   numpy
    *   matplotlib
    *   scikit-learn
    *   tensorflow
*   **External Configuration:** None detected.
### Data Lineage
*   **Source:**
    *   `StudentsData2.tab` (Historical factory data including power consumption and output)
    *   `data_OBS_DEU_PT1H_T2M.csv` (Historical temperature data)
    *   `data_OBS_DEU_PT1H_SD.csv` (Historical sunshine data)
    *   `data_OBS_DEU_PT1H_RF.csv` (Historical humidity data)
    *   `PredictTemp.csv` (Future temperature predictions)
    *   `Predicthumidity.csv` (Future humidity predictions)
    *   `PredictSun.csv` (Future sunshine predictions)

## 3. Methodology & Justification
*   **Step 1: Historical Data Ingestion and Preprocessing**
    *   **Description:** The initial phase involves loading raw historical data from multiple tab and CSV files. These include core factory data (`StudentsData2.tab`) and separate weather datasets for temperature, humidity, and sunshine. Column names were standardized, and irrelevant columns (e.g., product codes) were removed. The 'Zeitstempel' (timestamp) column was uniformly converted to datetime objects and formatted. All weather datasets were then merged sequentially, followed by a merge with the main factory data to form a comprehensive `merged_df`. Missing `SunshineMinutes` values were imputed with zero. To enhance model performance, the `Zeitstempel` column was further decomposed into granular time features (`Day`, `Month`, `Year`, `Hour`, `Minutes`), a transformation noted to improve model accuracy. Finally, redundant original timestamp columns were dropped, and relevant columns were cast to `int64` for numerical processing. This process resulted in two key dataframes: `merged_df` (for factory output prediction) and `merged_df2` (for power consumption prediction).
    *   **Justification:** This extensive preprocessing ensures data consistency, handles missing values, and extracts highly relevant temporal features crucial for time-series regression tasks. The splitting of the timestamp was a critical step in enabling the models to capture underlying patterns that a single timestamp might obscure.

*   **Step 2: Future Prediction Data Ingestion and Preprocessing**
    *   **Description:** Similar to the historical data, future weather prediction data for temperature, humidity, and sunshine was loaded from separate CSV files. The data underwent an identical preprocessing pipeline, including column renaming, product code removal, datetime conversion, and `Zeitstempel` decomposition into granular time features. These future weather features were consolidated into `merged_dfpred`, which serves as the input for generating future predictions.
    *   **Justification:** Applying the same rigorous preprocessing to future data ensures that it aligns structurally and semantically with the historical data the models were trained on, enabling accurate forecasting.

*   **Step 3: Random Forest Regression Model Development**
    *   **Description:** Two Random Forest Regressor models were implemented. The first model predicts `ManufacturingProcesses` (factory output) using time and weather features. The second model predicts `FabPowerConsumption` (power consumption) using time, weather, and the predicted factory output. The historical data was split into 80% training, 10% validation, and 10% test sets. Both models were initialized with `n_estimators=100` and `random_state=42` for reproducibility, then trained on their respective training sets.
    *   **Justification:** Random Forest Regression was selected due to its superior performance compared to an initial linear regression attempt, which yielded "nonsensical" predictions. Its ability to capture complex, non-linear relationships and robustness against overfitting made it a suitable choice for this task. The sequential prediction (output then consumption) reflects the dependency of power consumption on factory output.
    *   **Evaluation:** On the test set, the power consumption model achieved an MSE of 0.00070 and an R2 Score of 0.973. The factory output model achieved an MSE of 3.42e-05 and an R2 Score of 0.999. These metrics indicate very high predictive accuracy.

*   **Step 4: Neural Network Model Development**
    *   **Description:** Two Sequential Neural Networks were developed using TensorFlow/Keras. The first network predicts factory output, and the second predicts power consumption. Features for the factory output model were scaled using `MinMaxScaler`. Both networks utilize `relu` activation functions in hidden layers and `sigmoid` for the output layer, optimized with Nadam (`learning_rate=0.002` for factory output, `0.001` for power consumption) and `mean_squared_error` loss. The factory output model has `Dense` layers with 256 and 128 neurons, while the power consumption model uses 128 and 64 neurons. Both were trained for 100 epochs with a batch size of 16.
    *   **Justification:** Neural networks offer a flexible framework for modeling non-linear relationships. The specific architectures, activation functions, and optimizers were chosen based on "thorough testing a large number of different combinations outside of the grid search." The factory output predictions from the first NN are then used as an input feature for the power consumption NN.
    *   **Evaluation:** On the test set, the factory output NN achieved an MSE of 0.00038, RMSE of 0.0196, and an R2 Score of 0.989. The power consumption NN achieved an MSE of 0.00125, RMSE of 0.0354, and an R2 Score of 0.952. These results confirm the neural networks' strong performance in capturing data variance.

*   **Step 5: Grid Search for Neural Network Hyperparameters (Factory Output)**
    *   **Description:** A `GridSearchCV` was performed to optimize hyperparameters for the Factory Output Neural Network. The parameters tuned were `hidden_units_layer1` ([64, 128, 256]), `hidden_units_layer2` ([32, 64, 128]), `learning_rate` ([0.001, 0.01, 0.002]), and `batch_size` ([16, 32, 64]). The search was conducted using a `KerasRegressor` wrapper with `epochs=50` and `cv=2`.
    *   **Justification:** This systematic search aimed to identify the optimal hyperparameter combination to further enhance the factory output prediction model. The best parameters identified were `batch_size: 16`, `hidden_units_layer1: 256`, `hidden_units_layer2: 128`, and `learning_rate: 0.002`, yielding a best MSE of 0.000796. A grid search for the power consumption model was deemed unnecessary due to its computational intensity and the marginal improvements expected based on previous manual testing.

## 4. Key Configuration & Hyperparameters
| Parameter                          | Value  | Context                                                                       |
| :--------------------------------- | :----- | :---------------------------------------------------------------------------- |
| `RandomForestRegressor.n_estimators` | 100    | Number of decision trees in the ensemble for both models.                     |
| `RandomForestRegressor.random_state` | 42     | Seed for random number generation to ensure reproducibility.                  |
| `NN.FactoryOutput.epochs`            | 100    | Number of full passes through the training dataset.                           |
| `NN.FactoryOutput.batch_size`        | 16     | Number of samples processed before updating model weights.                    |
| `NN.FactoryOutput.hidden_units_layer1` | 256    | Number of neurons in the first hidden layer of the factory output NN.         |
| `NN.FactoryOutput.hidden_units_layer2` | 128    | Number of neurons in the second hidden layer of the factory output NN.        |
| `NN.FactoryOutput.learning_rate`     | 0.002  | Step size for the Nadam optimizer during weight updates.                      |
| `NN.PowerConsumption.epochs`         | 100    | Number of full passes through the training dataset.                           |
| `NN.PowerConsumption.batch_size`     | 16     | Number of samples processed before updating model weights.                    |
| `NN.PowerConsumption.hidden_units_layer1` | 128    | Number of neurons in the first hidden layer of the power consumption NN.      |
| `NN.PowerConsumption.hidden_units_layer2` | 64     | Number of neurons in the second hidden layer of the power consumption NN.     |
| `NN.PowerConsumption.learning_rate`  | 0.001  | Step size for the Nadam optimizer during weight updates.                      |
| `MinMaxScaler`                     | N/A    | Feature scaling applied to neural network inputs.                             |
| `train_test_split.test_size`       | 0.2    | Proportion of data allocated for testing the models (initial split).          |
| `NN.validation_split`              | 0.2    | Proportion of training data used for validation during NN training.           |
| `GridSearchCV.scoring`             | `neg_mean_squared_error` | Evaluation metric used to find the best hyperparameters.                  |
| `GridSearchCV.cv`                  | 2      | Number of cross-validation folds for grid search.                             |

## 5. Results & Visualizations
*   **Random Forest Regression Metrics:**
    *   Mean Squared Error for Power Consumption on Test Set: `0.0007007`
    *   Mean Squared Error for Factory Output on Test Set: `3.428781658402992e-05`
    *   R2 Score for Power Consumption on Test Set: `0.9732105105134488`
    *   R2 Score for Factory Output on Test Set: `0.9989989335833827`

*   **Neural Network Metrics:**
    *   MSE for Factory Output: `0.00038482187361803304`
    *   RMSE for Factory Output: `0.0196168772646931`
    *   R2 Score for Factory Output: `0.9888939769435837`
    *   MSE for Power Consumption: `0.0012548980485401766`
    *   RMSE for Power Consumption: `0.035424540202240826`
    *   R2 Score for Power Consumption: `0.9523366263808888`

Figure 1: Predictions: Regression vs Neural Network
*   **Visual Analysis:** This line plot compares the predicted Power Consumption and Factory Output from both the Random Forest Regression and Neural Network models for the future prediction period (72 points). The power consumption predictions (red for Regression, orange for NN) show a high degree of similarity, tracking the same general pattern and magnitude (0.3 to 0.45). For factory output predictions (blue for Regression, green for NN), both models predict values consistently around 0.9. However, the Neural Network's factory output shows slightly more volatility and, notably, an inverse trend compared to the Regression model's factory output towards the end of the prediction window (index ~50-70).
*   **Context:** The visual congruence in power consumption predictions from two different model types lends significant confidence to their accuracy. The minor discrepancies in factory output, particularly the differing trends on the third day, suggest potential areas for further model refinement or ensemble approaches, but the overall alignment confirms a consistent interpretation of underlying data.

Figure 2: Last 72 Datapoints before Prediction
*   **Visual Analysis:** This line plot illustrates the actual 'ManufacturingProcesses' (Factory Output, blue line) and 'FabPowerConsumption' (Power Consumption, orange line) for the 72 hours immediately preceding the prediction period. Factory output remains consistently high, near 1.0, while power consumption displays considerable fluctuation, including a prominent spike around index 27660 (reaching ~0.5) and another peak near 27710.
*   **Context:** This plot serves as a crucial reference, demonstrating the historical volatility and general levels of power consumption and factory output. It provides context for the models' predictions, which notably show a significant reduction in power consumption volatility for the next three days, and a predicted initial 10% drop in factory output that both models agree upon.

Figure 3: Comparing Temperature, Humidity and Sunshine
*   **Visual Analysis:** This plot visualizes the predicted Temperature (blue), Relative Humidity (red), and Sunshine Minutes (green) for the future prediction period. Relative Humidity shows a high baseline with two distinct dips, while Temperature gradually decreases from approximately 10 degrees to near 0, then slightly recovers. Sunshine Minutes are mostly zero, with two sharp, short-duration spikes indicating brief periods of sunshine.
*   **Context:** These are the key environmental inputs for the prediction models. The patterns shown here, particularly the temperature trend, are expected to directly influence the predicted power consumption and factory output, aligning with the observed strong correlation between historical temperature and power consumption.

Figure 4: Comparing Factory Output and Power Consumption
*   **Visual Analysis:** This plot presents the entire historical series of 'ManufacturingProcesses' (Factory Output, red) and 'FabPowerConsumption' (Power Consumption, blue) over roughly 27,000 data points. Both series exhibit high variability, with factory output generally staying above 0.2 and power consumption fluctuating widely, sometimes dipping close to zero. There are periods of strong correlation where peaks and troughs align, but also significant divergences, demonstrating a complex relationship.
*   **Context:** This visualization provides a macroscopic view of the historical data's complexity, justifying the choice of non-linear models (Random Forest, Neural Network). It reinforces the observation that power consumption and factory output do not always move in lockstep, and significant differences between them are normal.

Figure 5: Last 72 Datapoints Weather
*   **Visual Analysis:** This plot displays the historical Temperature (blue), Relative Humidity (red), and Sunshine Minutes (green) for the 72 hours preceding the prediction. Relative Humidity fluctuates significantly, often above 50. Temperature generally rises and then falls, ranging from ~10 to ~22. Sunshine Minutes show intermittent, short bursts of activity, reaching values up to 60.
*   **Context:** This detailed view of recent weather conditions provides direct context for the models' predictions. The observed patterns, especially the dynamic temperature shifts, are critical inputs that drive the predicted changes in factory output and power consumption. The strong correlation between historical temperature and power consumption supports the reliability of using these weather inputs.

## 6. Artifacts & Storage
*   **Outputs:** The notebook generates dataframes containing the following predicted values:
    *   `predictions_next_three_days`: DataFrame with 'Factory Output Predictions' and 'Power Consumption Predictions' from the Random Forest model.
    *   `predictions_df_nn`: DataFrame with 'Power Consumption Predictions' and 'Factory Output Predictions' from the Neural Network model.
*   **Location:** These prediction dataframes are displayed as direct output within the notebook. No files are saved to persistent storage by the provided code.

---