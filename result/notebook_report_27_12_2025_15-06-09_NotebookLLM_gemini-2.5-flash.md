# Notebook: predicting-power-consumption-uni documentation

## 1. Executive Summary
This notebook focuses on predicting future power consumption and factory output for the next three days by developing and comparing two regression models: Random Forest Regression and a Neural Network. The core objective is to forecast energy demand and production levels based on historical operational data and various weather conditions. The methodology involves extensive data preprocessing, including merging disparate weather datasets and feature engineering temporal attributes. Both models successfully predict reduced power consumption and less volatility, notably without the historical spikes observed. The Random Forest model achieved impressive R2 scores of 0.973 for power consumption and 0.999 for factory output, while the Neural Network showed strong performance with R2 scores of 0.952 for power consumption and 0.989 for factory output, indicating high accuracy in predicting future trends.

## 2. Technical Prerequisites
### Environment
*   **Dependencies:**
    *   pandas
    *   numpy
    *   matplotlib
    *   scikit-learn
    *   tensorflow (specifically `tensorflow==2.12.0` was installed)
    *   torch (imported but not explicitly used for model training)
*   **External Configuration:** None detected.
### Data Lineage
*   **Source:**
    *   **Historical Data:**
        *   `StudentsData2.tab` (Main operational data, including factory output and power consumption)
        *   `data_OBS_DEU_PT1H_T2M.csv` (Historical temperature data)
        *   `data_OBS_DEU_PT1H_SD.csv` (Historical sunshine duration data)
        *   `data_OBS_DEU_PT1H_RF.csv` (Historical relative humidity data)
    *   **Future Prediction Data:**
        *   `PredictTemp.csv` (Future temperature data)
        *   `Predicthumidity.csv` (Future humidity data)
        *   `PredictSun.csv` (Future sunshine duration data)

## 3. Methodology & Justification

*   **Step 1: Historical Data Acquisition and Preprocessing**
    *   **Objective:** To prepare comprehensive historical datasets suitable for model training, incorporating factory output, power consumption, and environmental factors.
    *   **Logic:** The process began by importing `pandas` for data manipulation. Several `.csv` and `.tab` files containing historical operational data and weather information (temperature, sunshine, humidity) were loaded. Columns were consistently renamed for clarity (e.g., "Wert" to "Temperature", "SunshineMinutes", "RelativeHumidity"). Extraneous identifier columns were removed. `Zeitstempel` (timestamp) columns across all dataframes were converted to a datetime format and then standardized to `'%d-%b-%y %H:%M'`. These individual dataframes were subsequently merged using left and inner joins based on the `Zeitstempel` column to form a unified dataset (`merged_df`). Missing values in the `SunshineMinutes` column, which arose during merging, were imputed with `0`. The `Zeitstempel` column was further engineered by splitting it into `Day`, `Month`, `Year`, `Hour`, and `Minutes` components. This decomposition of the timestamp was observed to significantly improve model accuracy. Finally, columns were reordered, and redundant time-related columns (`Zeitstempel`, `Time`, `Minutes`) were dropped to create `merged_df` (for factory output features) and `merged_df2` (for power consumption features, including `ManufacturingProcesses` and `FabPowerConsumption`). Numerical columns (`Day`, `Month`, `Year`, `Hour`) were explicitly converted to `int64` for compatibility with subsequent modeling steps.

*   **Step 2: Future Prediction Data Acquisition and Preprocessing**
    *   **Objective:** To prepare future weather data to serve as input for generating forecasts of factory output and power consumption.
    *   **Logic:** Similar to the historical data, separate `.csv` files containing future temperature, humidity, and sunshine data were loaded. The same preprocessing steps—column renaming, dropping irrelevant columns, converting `Zeitstempel` to a standardized datetime string format, and merging—were applied to these future datasets. Missing `SunshineMinutes` values were filled with `0`. The `Zeitstempel` column was then split into `Day`, `Month`, `Year`, `Hour`, and `Minutes`. After column reordering and dropping the original `Zeitstempel`, `Time`, and `Minutes` columns, the resulting `merged_dfpred` dataframe was established as the primary input for future predictions.

*   **Step 3: Random Forest Regression Model Development and Evaluation**
    *   **Objective:** To develop and evaluate a Random Forest Regressor for predicting both factory output and power consumption.
    *   **Logic:** The historical features and target variables for both factory output and power consumption were extracted from `merged_df` and `merged_df2`. Each dataset was then split into 80% training, 10% validation, and 10% testing sets using `train_test_split` with `random_state=42` for reproducibility. Two `RandomForestRegressor` models were initialized, both configured with `n_estimators=100` and `random_state=42`. These models were independently trained: one for factory output (`rf_factory_output`) and one for power consumption (`rf_power_consumption`). Future factory output was predicted first using `rf_factory_output` on `merged_dfpred`. These predictions were then concatenated with the future weather features (`merged_dfpred`) to form the complete input for predicting future power consumption using `rf_power_consumption`. Finally, the performance of both Random Forest models was evaluated on their respective test sets using `mean_squared_error` and `r2_score`.
    *   **Justification:** Initial exploration with a Linear Regression model proved unsuitable due to "nonsensical" predictions and a failure to capture non-linear relationships. Random Forest Regression was chosen as a more robust alternative, offering high predictive accuracy, the ability to handle complex non-linear data patterns, and inherent robustness against overfitting, thus addressing the limitations of the linear approach.

*   **Step 4: Neural Network Model Development and Evaluation**
    *   **Objective:** To implement and evaluate a Neural Network architecture for predicting factory output and power consumption, providing an alternative perspective to the Random Forest model.
    *   **Logic:** Features and target variables for factory output and power consumption were extracted from `merged_df2` and split into training and testing sets. `MinMaxScaler` was applied to scale the features for the factory output model, which is a common practice for Neural Networks to improve training stability and performance. Two separate `tensorflow.keras.models.Sequential` Neural Networks were constructed:
        *   **Factory Output Model:** Consisted of three `Dense` layers (256, 128, and 1 neuron) with `relu` activation for hidden layers and `sigmoid` for the output layer. It was compiled with the `Nadam` optimizer (`learning_rate=0.002`) and `mean_squared_error` loss. The model was trained for `100 epochs` with a `batch_size` of `16` and `validation_split` of `0.2`.
        *   **Power Consumption Model:** Featured three `Dense` layers (128, 64, and 1 neuron) with `relu` activation for hidden layers and `sigmoid` for the output. This model was compiled with `Nadam` (`learning_rate=0.001`) and `mean_squared_error` loss, and trained for `100 epochs` with `batch_size=16` and `validation_split=0.2`.
    *   Predictions for future factory output were made using the scaled future features from `merged_dfpred`. These predictions were then combined with the original `merged_dfpred` (converted to a TensorFlow constant tensor) to serve as input for the power consumption Neural Network. The models' performance on the test sets was assessed using `mean_squared_error`, `mean_absolute_error`, and `r2_score`.
    *   **Justification:** The Neural Network approach was adopted to explore its capability in capturing potentially more intricate non-linear dynamics within the data. Hyperparameters such as neuron counts and learning rates were carefully determined through a combination of thorough experimentation and a subsequent grid search. The choice of `relu` and `sigmoid` activations and the `Nadam` optimizer stemmed from extensive empirical testing. During development, a specific older version of TensorFlow (`tensorflow==2.12.0`) was installed, implying compatibility or stability reasons for this choice.

*   **Step 5: Hyperparameter Tuning for Neural Network (Factory Output)**
    *   **Objective:** To optimize the hyperparameters of the factory output Neural Network model using a systematic search.
    *   **Logic:** A `create_model` function was defined to generate a `Sequential` Keras model with configurable hidden layer units and learning rates. A hyperparameter grid was specified, exploring various combinations of `hidden_units_layer1` (64, 128, 256), `hidden_units_layer2` (32, 64, 128), `learning_rate` (0.001, 0.01, 0.002), and `batch_size` (16, 32, 64). `GridSearchCV` from `scikit-learn` was employed with `KerasRegressor` (epochs=50, cv=2, scoring='neg_mean_squared_error') to identify the optimal set of hyperparameters for the factory output model.
    *   **Justification:** Grid search was performed to systematically refine the Neural Network's architecture and training parameters, ensuring optimal performance. A grid search for the power consumption model was forgone due to its high computational cost and observations that further improvements beyond initial testing were marginal.

*   **Step 6: Model Comparison and Causal Analysis**
    *   **Objective:** To visually compare the predictions from both models and analyze underlying data relationships that influence power consumption.
    *   **Logic:**
        *   The predicted factory output and power consumption for the next three days from both the Random Forest and Neural Network models were plotted on a single graph to visually compare their trends.
        *   Historical factory output and power consumption for the last 72 hours preceding the prediction period were plotted to provide context for the models' immediate forecasts.
        *   Future and historical plots of temperature, humidity, and sunshine were generated to analyze environmental factor trends.
        *   A plot comparing historical factory output and power consumption was created.
    *   **Analysis & Justification:**
        *   The plots revealed a "striking similarity" between the power consumption predictions of both models, indicating a consistent interpretation of the underlying data. While factory output predictions were generally similar, the Neural Network showed slightly more volatility and an interesting "mirroring effect" in the trend on the third day compared to the Random Forest model.
        *   Both models predicted an approximate 10% drop in factory output immediately after the last historical data point, which was deemed plausible given the lack of real-world context for these values.
        *   A significant observation was the strong correlation between Power Consumption and Temperature, which was visually evident in both historical and predicted data plots. This correlation provided increased confidence in the accuracy of the predictions.
        *   The models consistently predicted lower power consumption and reduced volatility, with no spikes, for the upcoming three days, a departure from some historical patterns. The notebook also noted that large differences between historical factory output and power consumption are common.

## 4. Key Configuration & Hyperparameters (only if applicable)
| Parameter                     | Value                                                                        | Context                                                                                                       |
| :---------------------------- | :--------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| `RandomForestRegressor`       | `n_estimators=100`, `random_state=42`                                        | Number of trees in the forest and seed for reproducibility across all Random Forest models.                     |
| `NN Factory Output Model`     | `Dense(256, activation='relu')`, `Dense(128, activation='relu')`             | Number of neurons and activation function for the first two hidden layers, as determined by Grid Search.      |
| `NN Factory Output Model`     | `Dense(1, activation='sigmoid')`                                             | Number of neurons and activation function for the output layer.                                               |
| `NN Factory Output Model`     | `learning_rate=0.002`                                                        | Learning rate for the Nadam optimizer (optimized via Grid Search).                                            |
| `NN Factory Output Model`     | `epochs=100`, `batch_size=16`, `validation_split=0.2`                        | Number of training iterations, samples per gradient update, and percentage of training data used for validation. |
| `NN Power Consumption Model`  | `Dense(128, activation='relu')`, `Dense(64, activation='relu')`             | Number of neurons and activation function for the first two hidden layers.                                    |
| `NN Power Consumption Model`  | `Dense(1, activation='sigmoid')`                                             | Number of neurons and activation function for the output layer.                                               |
| `NN Power Consumption Model`  | `learning_rate=0.001`                                                        | Learning rate for the Nadam optimizer.                                                                        |
| `NN Power Consumption Model`  | `epochs=100`, `batch_size=16`, `validation_split=0.2`                        | Number of training iterations, samples per gradient update, and percentage of training data used for validation. |
| `Grid Search Best Parameters` | `{'batch_size': 16, 'hidden_units_layer1': 256, 'hidden_units_layer2': 128, 'learning_rate': 0.002}` | Optimal hyperparameters for the factory output Neural Network, identified through GridSearchCV.               |

## 5. Results & Visualizations
This section is not implemented yet.

## 6. Artifacts & Storage
*   **Outputs:** No explicit model artifacts (e.g., `.pkl`, `.h5` files for trained models) or processed output dataframes (e.g., `.csv`, `.json` files for predictions) were saved to disk in this notebook.
*   **Location:** Not applicable.

---