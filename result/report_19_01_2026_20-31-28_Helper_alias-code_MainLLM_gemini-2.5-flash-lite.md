# Project Documentation: analytics-application-development-uni

## 1. Project Overview [Can be accessed under 'basic_info'.]
    - **Description:** Information not found
    - **Key Features:** 
      - Information not found
    - **Tech Stack:** Information not found
*   **Repository Structure:**
    ```mermaid
    graph LR
        root --> streamlit_config[config.toml]
        root --> notebook[Notebook.ipynb]
        root --> notes_dir(Notizen)
        notes_dir --> note1[Analytics Application Development.md]
        notes_dir --> note2[Dokumentation AAD.md]
        notes_dir --> note3[Meeting_17-11-25.md]
        root --> app_pages_dir(app_pages)
        app_pages_dir --> app_pages_init[__init__.py]
        app_pages_dir --> page1[page1.py]
        app_pages_dir --> page2[page2.py]
        app_pages_dir --> page3[page3.py]
        app_pages_dir --> page4[page4.py]
        app_pages_dir --> page5[page5.py]
        root --> assets_dir(assets)
        assets_dir --> logo[logo.png]
        root --> build_db[build_db.py]
        root --> dashboard[dashboard.py]
        root --> data_cleaning[data_cleaning.py]
        root --> data_drift[data_drift.py]
        root --> data_drift_metrics[data_drift_metrics.py]
        root --> data_exploration[data_exploration.py]
        root --> data_exploration2[data_exploration2.py]
        root --> db_dashboard[db_dashboard.py]
        root --> metrics[metrics.py]
        root --> requirements[requirements.txt]
    ```

    ## 2. Installation (can be accessed under 'basic_info')
    ### Dependencies
    - altair==5.5.0
    - attrs==25.4.0
    - blinker==1.9.0
    - cachetools==6.2.2
    - certifi==2025.11.12
    - charset-normalizer==3.4.4
    - click==8.3.1
    - colorama==0.4.6
    - gitdb==4.0.12
    - GitPython==3.1.45
    - idna==3.11
    - Jinja2==3.1.6
    - jsonschema==4.25.1
    - jsonschema-specifications==2025.9.1
    - MarkupSafe==3.0.3
    - narwhals==2.12.0
    - numpy==2.3.5
    - packaging==25.0
    - pandas==2.3.3
    - pillow==12.0.0
    - protobuf==6.33.1
    - pyarrow==21.0.0
    - pydeck==0.9.1
    - python-dateutil==2.9.0.post0
    - pytz==2025.2
    - referencing==0.37.0
    - requests==2.32.5
    - rpds-py==0.29.0
    - scipy==1.16.3
    - six==1.17.0
    - smmap==5.0.2
    - streamlit==1.51.0
    - streamlit-option-menu==0.4.0
    - tenacity==9.1.2
    - toml==0.10.2
    - tornado==6.5.2
    - typing_extensions==4.15.0
    - tzdata==2025.2
    - urllib3==2.5.0
    - watchdog==6.0.0
    - sentence-transformers
    - torch torchvision --index-url https://download.pytorch.org/whl/cu126
    - duckdb
    **Note:** pip install -r requirements.txt
### Setup Guide
Information not found
### Quick Startup
Information not found

## 3. Use Cases & Commands
This application appears to be a data analysis and visualization dashboard, likely built with Streamlit. It focuses on processing and presenting metrics derived from order and position data. Key use cases include:

*   **Data Quality Assessment:** Evaluating the cleanliness and integrity of order and position datasets through various metrics like null value ratios, uniqueness checks, and plausibility checks.
*   **Performance Monitoring:** Tracking key performance indicators (KPIs) related to orders and positions, such as row counts, error frequencies, and specific business-related metrics (e.g., proforma receipts, orders over €50k).
*   **Data Drift Analysis:** (Potentially, based on `data_drift.py` and `data_drift_metrics.py`) Analyzing changes and drift in data characteristics over time.
*   **Business Logic Validation:** Checking for discrepancies between aggregated position data and order-level data, and validating specific business rules (e.g., discount checks, time value consistency).

Primary commands would involve running the Streamlit application:
*   `streamlit run dashboard.py`
*   `streamlit run db_dashboard.py`
*   `streamlit run data_drift.py`

## 4. Architecture
```mermaid
graph TD
```

## 5. Code Analysis
### File: `app_pages/page1.py`

#### Function: `show_page`
*   **Signature:** `def show_page(df, df2, metrics_df1, metrics_df2, metrics_combined)`
*   **Description:** The function 'show_page' displays key performance indicators (KPIs) and visualizes data quality metrics using Streamlit components. It calculates and presents various statistics such as row counts, null value ratios, and unique ID checks for two datasets. Additionally, it generates two charts: one showing the top columns with the highest null value ratios and another displaying error frequency by weekday and hour. The function relies on precomputed metrics provided via input DataFrames.
*   **Parameters:**
    *   **df** (`DataFrame`): The first dataset containing order data.
    *   **df2** (`DataFrame`): The second dataset containing position data.
    *   **metrics_df1** (`dict`): A dictionary containing metrics computed for the first dataset.
    *   **metrics_df2** (`dict`): A dictionary containing metrics computed for the second dataset.
    *   **metrics_combined** (`dict`): A dictionary containing combined metrics for both datasets.
*   **Returns:**
*   **Usage:**
    *   Calls: `metrics.ratio_null_values_rows`
    *   Called by: No other functions.

### File: `app_pages/page2.py`

#### Function: `show_page`
*   **Signature:** `def show_page(df, df2, metrics_df1, metrics_df2, metrics_combined)`
*   **Description:** The function 'show_page' displays data visualization and metrics related to time value errors and orders exceeding 50,000 EUR. It retrieves specific data series and counts from provided DataFrames and uses Streamlit components to render KPIs, tables, and charts. The function dynamically calculates or fetches error counts and data frames based on optional keys in the metrics DataFrames.
*   **Parameters:**
    *   **df** (`DataFrame`): Primary DataFrame containing general data.
    *   **df2** (`DataFrame`): Secondary DataFrame, likely used for additional data processing or comparison.
    *   **metrics_df1** (`DataFrame`): DataFrame containing metrics related to time value errors and other data points.
    *   **metrics_df2** (`DataFrame`): Secondary metrics DataFrame, possibly used for additional metric calculations.
    *   **metrics_combined** (`DataFrame`): Combined metrics DataFrame, used to retrieve data such as order agreement information.
*   **Returns:**
*   **Usage:**
    *   Calls: `metrics.above_50k`, `metrics.check_zeitwert`
    *   Called by: No other functions.

### File: `app_pages/page3.py`

#### Function: `show_page`
*   **Signature:** `def show_page(df, df2, metrics_df1, metrics_df2, metrics_combined)`
*   **Description:** The function 'show_page' displays data related to handwerker (craftspeople) and gewerke (trades) using Streamlit components. It retrieves specific metrics from 'metrics_df1' and presents them as KPIs and dataframes in a Streamlit layout. The function uses Streamlit's column and metric components to organize and display information.
*   **Parameters:**
    *   **df** (`Any`): A dataframe parameter, likely containing general data, though not directly used in the function.
    *   **df2** (`Any`): A second dataframe parameter, possibly for additional data, but not used in the function.
    *   **metrics_df1** (`Dict[str, Any]`): A dictionary containing metrics data, specifically used to retrieve outlier and test entry counts.
    *   **metrics_df2** (`Any`): A second metrics dataframe, possibly for additional metrics, but not used in the function.
    *   **metrics_combined** (`Any`): A combined metrics dataframe, possibly for aggregated data, but not used in the function.
*   **Returns:**
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

### File: `app_pages/page4.py`

#### Function: `show_page`
*   **Signature:** `def show_page(df, df2, metrics_df1, metrics_df2, metrics_combined)`
*   **Description:** The function 'show_page' displays a set of key performance indicators (KPIs) derived from two datasets and their associated metrics. It retrieves specific metric values from provided dataframes and presents them using Streamlit components such as 'st.metric' and 'st.columns'. The function also handles default fallbacks for missing keys in the metrics dataframes by calling helper functions from the 'metrics' module. This function is designed to visualize data quality checks and discrepancies between order and position data.
*   **Parameters:**
    *   **df** (`Any`): The first dataframe containing order-related data.
    *   **df2** (`Any`): The second dataframe containing position-related data.
    *   **metrics_df1** (`Dict[str, Any]`): A dictionary containing metrics related to order data.
    *   **metrics_df2** (`Dict[str, Any]`): A dictionary containing metrics related to position data.
    *   **metrics_combined** (`Any`): A combined metrics object, although not directly used in the function body.
*   **Returns:**
*   **Usage:**
    *   Calls: `metrics.discount_check`, `metrics.false_negative_df`, `metrics.false_negative_df2`
    *   Called by: No other functions.

### File: `app_pages/page5.py`

#### Function: `show_page`
*   **Signature:** `def show_page()`
*   **Description:** This function displays the content for Page 5 of a Streamlit application. It sets the title of the page to 'Page 5' using the Streamlit library. The function performs no complex logic or data processing; it simply renders a static title on the page.
*   **Parameters:**
*   **Returns:**
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

### File: `build_db.py`
*Analysis data not available for this component.*
### File: `dashboard.py`

#### Function: `load`
   **Sequence diagram for load**
```mermaid
sequenceDiagram
    participant db_dashboard_load
    participant db_dashboard_get_db_connection
    db_dashboard_load ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_load: return
```
*   **Signature:** `def load()`
*   **Description:** This function loads two dataframes from parquet files located at 'resources/Auftragsdaten_konvertiert' and 'resources/Positionsdaten_konvertiert'. It uses pandas to read these files and returns both dataframes as a tuple. The function serves as a data loading utility for a dashboard application.
*   **Parameters:**
*   **Returns:**
    *   **df** (`DataFrame`): The first dataframe loaded from the 'Auftragsdaten_konvertiert' parquet file.
    *   **df2** (`DataFrame`): The second dataframe loaded from the 'Positionsdaten_konvertiert' parquet file.
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `compute_metrics_df1`
   **Sequence diagram for compute_metrics_df1**
```mermaid
sequenceDiagram
    participant dashboard_compute_metrics_df1
    participant dashboard_load
    participant db_dashboard_compute_metrics_df1
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_df1
    participant db_dashboard_get_scalar_metrics
    dashboard_compute_metrics_df1 ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_metrics_df1: return
    db_dashboard_compute_metrics_df1 ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_df1: return
    db_dashboard_compute_metrics_df1 ->> db_dashboard_get_scalar_metrics: []
```
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** "This function computes a comprehensive set of metrics for a DataFrame named 'df1' (Auftragsdaten). It performs various data validation checks, calculates statistical measures, and extracts specific data patterns such as error frequencies and outlier information. The function orchestrates multiple utility functions from the 'metrics' module to gather these insights and returns them in a dictionary format."
*   **Parameters:**
*   **Returns:**
    *   **metrics_df1** (`dict`): "A dictionary containing computed metrics for df1, including row counts, null value ratios, plausibility checks, data cleanliness ratios, proforma documents, error frequency, and outlier information."
*   **Usage:**
    *   Calls: `dashboard.load`, `metrics.Kundengruppe_containing_test`, `metrics.above_50k`, `metrics.allgemeine_statistiken_num`, `metrics.check_keywords_vectorized`, `metrics.check_zeitwert`, `metrics.count_rows`, `metrics.data_cleanliness`, `metrics.error_frequency_by_weekday_hour`, `metrics.false_negative_df`, `metrics.handwerker_gewerke_outlier`, `metrics.plausibilitaetscheck_forderung_einigung`, `metrics.proformabelege`, `metrics.ratio_null_values_column`, `metrics.ratio_null_values_rows`
    *   Called by: No other functions.

#### Function: `compute_metrics_df2`
   **Sequence diagram for compute_metrics_df2**
```mermaid
sequenceDiagram
    participant dashboard_compute_metrics_df2
    participant dashboard_load
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_get_scalar_metrics
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_load
    dashboard_compute_metrics_df2 ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_metrics_df2: return
    db_dashboard_compute_metrics_df2 ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_df2: return
    db_dashboard_compute_metrics_df2 ->> db_dashboard_get_scalar_metrics: []
    db_dashboard_compute_metrics_df2 ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_df2: return
    db_dashboard_compute_metrics_df2 ->> db_dashboard_load: []
```
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** "This function computes a set of descriptive statistics and validation metrics for a DataFrame named 'df2', which contains position data. It loads the DataFrame using an external load function, performs several checks and calculations on the data, and returns a dictionary containing various metric values. The function includes timing information to track execution duration."
*   **Parameters:**
*   **Returns:**
    *   **metrics_df2** (`dict`): "A dictionary containing various computed metrics for df2, including row count, null value ratios, statistical summaries, plausibility checks, and false negative counts."
*   **Usage:**
    *   Calls: `dashboard.load`, `metrics.allgemeine_statistiken_num`, `metrics.count_rows`, `metrics.discount_check`, `metrics.false_negative_df2`, `metrics.plausibilitaetscheck_forderung_einigung`, `metrics.position_count`, `metrics.ratio_null_values_column`, `metrics.ratio_null_values_rows`
    *   Called by: No other functions.

#### Function: `compute_metrics_combined`
   **Sequence diagram for compute_metrics_combined**
```mermaid
sequenceDiagram
    participant dashboard_compute_metrics_combined
    participant dashboard_load
    participant db_dashboard_compute_metrics_combined
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_combined
    participant db_dashboard_get_scalar_metrics
    dashboard_compute_metrics_combined ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_metrics_combined: return
    db_dashboard_compute_metrics_combined ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_combined: return
    db_dashboard_compute_metrics_combined ->> db_dashboard_get_scalar_metrics: []
```
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** "This function computes combined metrics that require data from two DataFrames. It loads the required data, performs uniqueness checks and order alignment calculations, and returns a dictionary containing the computed metrics. The function includes timing information to measure execution duration."
*   **Parameters:**
*   **Returns:**
    *   **metrics_combined** (`dict`): "A dictionary containing three keys: 'kvarechnung_id_is_unique', 'position_id_is_unique', and 'auftraege_abgleich', each mapping to their respective computed metric values."
*   **Usage:**
    *   Calls: `dashboard.load`, `metrics.abgleich_auftraege`, `metrics.uniqueness_check`
    *   Called by: No other functions.

#### Function: `compute_positions_over_time`
   **Sequence diagram for compute_positions_over_time**
```mermaid
sequenceDiagram
    participant dashboard_compute_positions_over_time
    participant dashboard_load
    participant db_dashboard_compute_positions_over_time
    participant db_dashboard_get_db_connection
    dashboard_compute_positions_over_time ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_positions_over_time: return
    db_dashboard_compute_positions_over_time ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_positions_over_time: return
```
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** "This function calculates the number of positions per order over time and returns the result as a DataFrame. It loads two datasets using a helper function, performs a computation on these datasets to derive the positions over time, and prints timing information during execution. The function is designed to be cached, although caching behavior is not explicitly shown in the code."
*   **Parameters:**
*   **Returns:**
    *   **positions_over_time_df** (`DataFrame`): A DataFrame containing the calculated positions per order over time.
*   **Usage:**
    *   Calls: `dashboard.load`, `metrics.positions_per_order_over_time`
    *   Called by: No other functions.

### File: `data_cleaning.py`
*Analysis data not available for this component.*
### File: `data_drift.py`

#### Function: `load_data`
   **Sequence diagram for load**
```mermaid
sequenceDiagram
    participant db_dashboard_load
    participant db_dashboard_get_db_connection
    db_dashboard_load ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_load: return
```
*   **Signature:** `def load_data()`
*   **Description:** "This function generates a synthetic dataset representing daily sales data over a period of one year, from January 1, 2022, to December 31, 2023. It creates a DataFrame with three columns: 'datum' for dates, 'umsatz' for sales figures that exhibit a gradual increase with random noise, and 'kunden' for customer counts. The function uses pandas for date range creation and DataFrame construction, and numpy for generating linearly increasing sales data with normally distributed random variation."
*   **Parameters:**
*   **Returns:**
    *   **df** (`DataFrame`): "A pandas DataFrame containing synthetic daily sales data with columns 'datum', 'umsatz', and 'kunden'."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `filterby_timeframe`
*   **Signature:** `def filterby_timeframe(input_df, start_date, end_date)`
*   **Description:** The function filters a pandas DataFrame based on a specified date range. It converts the provided start and end dates into datetime objects and applies a boolean mask to select rows where the 'datum' column falls within the given timeframe. The result is a filtered DataFrame containing only the rows that meet the date criteria.
*   **Parameters:**
    *   **input_df** (`DataFrame`): The input pandas DataFrame that contains the data to be filtered.
    *   **start_date** (`str or datetime-like`): "The starting date of the desired time range, which will be converted to a datetime object."
    *   **end_date** (`str or datetime-like`): "The ending date of the desired time range, which will be converted to a datetime object."
*   **Returns:**
    *   **filtered_df** (`DataFrame`): "A pandas DataFrame containing only the rows from input_df where the 'datum' column is between start_date and end_date inclusive."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `get_drift_stats`
*   **Signature:** `def get_drift_stats(input_df, frequency)`
*   **Description:** "The function computes statistical measures (mean, median, standard deviation, minimum, and maximum) for two columns ('umsatz' and 'kunden') grouped by a time frequency. It takes an input DataFrame and a frequency parameter to group the data by time periods. The resulting statistics are organized into a flattened DataFrame with column names indicating the metric and variable. This function is intended for use in generating charts based on time-series data."
*   **Parameters:**
    *   **input_df** (`DataFrame`): "The input DataFrame containing at least the columns 'datum', 'umsatz', and 'kunden'."
    *   **frequency** (`str`): "A frequency string used to group the data by time periods (e.g., 'D' for daily, 'M' for monthly)."
*   **Returns:**
    *   **stats_df** (`DataFrame`): "A DataFrame containing aggregated statistics for 'umsatz' and 'kunden' grouped by the specified frequency."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `slicing`
*   **Signature:** `def slicing(input_df, frequency)`
*   **Description:** "The function 'slicing' creates individual slices from an input DataFrame based on a specified frequency grouping. It groups the data by date using pandas' Grouper and iterates through the groups to build a dictionary of slices, keyed by formatted date labels. Each slice corresponds to a time period defined by the frequency parameter. In case of an exception during processing, it displays an error message using Streamlit and returns an empty dictionary."
*   **Parameters:**
    *   **input_df** (`DataFrame`): The input DataFrame containing the data to be sliced.
    *   **frequency** (`str`): "The frequency string used to group the data by date, such as 'D' for daily or 'M' for monthly."
*   **Returns:**
    *   **slices** (`dict`): "A dictionary where keys are formatted date strings and values are the corresponding grouped DataFrames."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

### File: `data_drift_metrics.py`

#### Function: `load`
   **Sequence diagram for load**
```mermaid
sequenceDiagram
    participant db_dashboard_load
    participant db_dashboard_get_db_connection
    db_dashboard_load ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_load: return
```
*   **Signature:** `def load()`
*   **Description:** "This function loads two datasets from Parquet files, sorts them by a timestamp column, and merges them based on a shared identifier. It returns both the sorted original dataset and the merged dataset. The function primarily handles data ingestion and preprocessing for further analysis."
*   **Parameters:**
*   **Returns:**
    *   **df** (`DataFrame`): "The first loaded DataFrame sorted by CRMEingangszeit."
    *   **df2** (`DataFrame`): "The second loaded DataFrame merged with selected columns from the first DataFrame, also sorted by CRMEingangszeit."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `check_start_end_date`
*   **Signature:** `def check_start_end_date(start, end)`
*   **Description:** "This function serves as a helper to ensure chronological ordering of two datetime objects. It takes two datetime inputs, compares them, and returns them in chronological order by swapping their positions if necessary. The function is designed to handle cases where the 'end' date might precede the 'start' date, correcting the order automatically."
*   **Parameters:**
    *   **start** (`datetime`): "The assumed beginning of the interval."
    *   **end** (`datetime`): "The assumed end of the interval."
*   **Returns:**
    *   **start** (`datetime`): "The earlier datetime value in the pair."
    *   **end** (`datetime`): "The later datetime value in the pair."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `datetime_slice_mask`
*   **Signature:** `def datetime_slice_mask(df, start_date, end_date)`
*   **Description:** "This function filters a pandas DataFrame based on a specified date range and converts the resulting subset into an Evidently Dataset. It checks for specific column names to determine the appropriate data definition schema to use during conversion. The function is designed to work with two types of DataFrames: one with a 'Kundengruppe' column (likely representing order data) and another with a 'Menge' column (likely representing position data)."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "The input DataFrame to be filtered by date."
    *   **start_date** (`datetime`): "The beginning of the date range (inclusive)."
    *   **end_date** (`datetime`): "The end of the date range (exclusive)."
*   **Returns:**
    *   **sliced_ds** (`evidently.Dataset`): "A sliced DataFrame converted to an Evidently Dataset based on the provided date range and column presence."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `data_drift_evaluation`
   **Sequence diagram for data_drift_evaluation**
```mermaid
sequenceDiagram
    participant data_drift_metrics_data_drift_evaluation
    participant data_drift_metrics_check_start_end_date
    participant data_drift_metrics_data_drift_evaluation
    participant data_drift_metrics_check_start_end_date
    participant data_drift_metrics_data_drift_evaluation
    participant data_drift_metrics_datetime_slice_mask
    participant data_drift_metrics_data_drift_evaluation
    participant data_drift_metrics_datetime_slice_mask
    data_drift_metrics_data_drift_evaluation ->> data_drift_metrics_check_start_end_date: ['start', 'end']
    data_drift_metrics_check_start_end_date ->> data_drift_metrics_data_drift_evaluation: return
    data_drift_metrics_data_drift_evaluation ->> data_drift_metrics_check_start_end_date: ['start', 'end']
    data_drift_metrics_check_start_end_date ->> data_drift_metrics_data_drift_evaluation: return
    data_drift_metrics_data_drift_evaluation ->> data_drift_metrics_datetime_slice_mask: ['df', 'start_date', 'end_date']
    data_drift_metrics_datetime_slice_mask ->> data_drift_metrics_data_drift_evaluation: return
    data_drift_metrics_data_drift_evaluation ->> data_drift_metrics_datetime_slice_mask: ['df', 'start_date', 'end_date']
    data_drift_metrics_datetime_slice_mask ->> data_drift_metrics_data_drift_evaluation: return
```
*   **Signature:** `def data_drift_evaluation(df, start_date_reference, end_date_reference, start_date_eval, end_date_eval)`
*   **Description:** "This function evaluates data drift between two time-sliced datasets using the EvidentlyAI framework. It takes a DataFrame and four datetime parameters to define reference and evaluation periods. The function ensures chronological order of date ranges, slices the data accordingly, and generates a data drift report tailored to either an 'Auftragsdaten' or 'Positionsdaten' dataset based on column presence. The resulting HTML report is saved to disk for visualization."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "DataFrame to sample from"
    *   **start_date_reference** (`datetime`): "starting datetime of the reference, baseline dataset"
    *   **end_date_reference** (`datetime`): "ending datetime of the reference, baseline dataset"
    *   **start_date_eval** (`datetime`): "starting datetime of the evaluated dataset"
    *   **end_date_eval** (`datetime`): "starting datetime of the evaluated dataset"
*   **Returns:**
*   **Usage:**
    *   Calls: `data_drift_metrics.check_start_end_date`, `data_drift_metrics.datetime_slice_mask`
    *   Called by: No other functions.

### File: `data_exploration.py`

#### Function: `load`
   **Sequence diagram for load**
```mermaid
sequenceDiagram
    participant db_dashboard_load
    participant db_dashboard_get_db_connection
    db_dashboard_load ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_load: return
```
*   **Signature:** `def load()`
*   **Description:** This function loads two datasets from parquet files located at 'resources/Auftragsdaten_konvertiert' and 'resources/Positionsdaten_konvertiert'. It reads these files into pandas DataFrames and returns them as a tuple. The function serves as a data loading utility for subsequent data processing steps.
*   **Parameters:**
*   **Returns:**
    *   **df** (`DataFrame`): "A pandas DataFrame containing the data from the 'Auftragsdaten_konvertiert' parquet file."
    *   **df2** (`DataFrame`): "A pandas DataFrame containing the data from the 'Positionsdaten_konvertiert' parquet file."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

### File: `data_exploration2.py`
*Analysis data not available for this component.*
### File: `db_dashboard.py`

#### Function: `get_db_connection`
*   **Signature:** `def get_db_connection()`
*   **Description:** "This function establishes a read-only connection to a DuckDB database using a predefined database path. It is designed to provide a simple interface for accessing the database in a read-only mode, ensuring data integrity by preventing modifications. The function does not take any parameters and directly returns the database connection object."
*   **Parameters:**
*   **Returns:**
    *   **connection** (`duckdb.Connection`): "A read-only connection object to the DuckDB database."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `load`
   **Sequence diagram for load**
```mermaid
sequenceDiagram
    participant db_dashboard_load
    participant db_dashboard_get_db_connection
    db_dashboard_load ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_load: return
```
*   **Signature:** `def load()`
*   **Description:** "This function retrieves two dataframes from a DuckDB database by executing SQL queries on the 'auftragsdaten' and 'positionsdaten' tables. It establishes a database connection, performs the queries, and returns the resulting dataframes. The function ensures proper resource management by closing the connection in a finally block."
*   **Parameters:**
*   **Returns:**
    *   **df** (`pandas.DataFrame`): "The dataframe containing data from the 'auftragsdaten' table."
    *   **df2** (`pandas.DataFrame`): "The dataframe containing data from the 'positionsdaten' table."
*   **Usage:**
    *   Calls: `db_dashboard.get_db_connection`
    *   Called by: No other functions.

#### Function: `get_scalar_metrics`
   **Sequence diagram for get_scalar_metrics**
```mermaid
sequenceDiagram
    participant db_dashboard_get_scalar_metrics
    participant db_dashboard_get_db_connection
    db_dashboard_get_scalar_metrics ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_get_scalar_metrics: return
```
*   **Signature:** `def get_scalar_metrics()`
*   **Description:** "This function serves as a helper to retrieve a single row of scalar metrics from a database table named 'scalar_metrics'. It establishes a database connection, executes a query to fetch all columns from the table, converts the result into a pandas DataFrame, and returns the first row of that DataFrame. The function ensures proper resource management by closing the database connection in a finally block."
*   **Parameters:**
*   **Returns:**
    *   **result** (`pandas.core.series.Series`): "A pandas Series representing the first row of the 'scalar_metrics' table."
*   **Usage:**
    *   Calls: `db_dashboard.get_db_connection`
    *   Called by: No other functions.

#### Function: `compute_metrics_df1`
   **Sequence diagram for compute_metrics_df1**
```mermaid
sequenceDiagram
    participant dashboard_compute_metrics_df1
    participant dashboard_load
    participant db_dashboard_compute_metrics_df1
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_df1
    participant db_dashboard_get_scalar_metrics
    dashboard_compute_metrics_df1 ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_metrics_df1: return
    db_dashboard_compute_metrics_df1 ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_df1: return
    db_dashboard_compute_metrics_df1 ->> db_dashboard_get_scalar_metrics: []
```
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** "This function retrieves and processes various data quality metrics for the 'df1' dataset (Auftragsdaten) from a database. It establishes a database connection, executes multiple SQL queries to fetch different metric tables, performs data transformations such as setting indices and converting dataframes to dictionaries, and finally compiles all retrieved data into a structured dictionary. The function includes error handling through a try-finally block to ensure the database connection is closed after execution. It also measures and prints the execution time for loading the metrics."
*   **Parameters:**
*   **Returns:**
    *   **metrics_df1** (`dict`): "A dictionary containing various data quality metrics for the 'df1' dataset, including row counts, null ratios, statistical summaries, plausibility checks, grouped cleanliness metrics, and other specific data quality indicators."
*   **Usage:**
    *   Calls: `db_dashboard.get_db_connection`, `db_dashboard.get_scalar_metrics`
    *   Called by: No other functions.

#### Function: `compute_metrics_df2`
   **Sequence diagram for compute_metrics_df2**
```mermaid
sequenceDiagram
    participant dashboard_compute_metrics_df2
    participant dashboard_load
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_get_scalar_metrics
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_df2
    participant db_dashboard_load
    dashboard_compute_metrics_df2 ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_metrics_df2: return
    db_dashboard_compute_metrics_df2 ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_df2: return
    db_dashboard_compute_metrics_df2 ->> db_dashboard_get_scalar_metrics: []
    db_dashboard_compute_metrics_df2 ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_df2: return
    db_dashboard_compute_metrics_df2 ->> db_dashboard_load: []
```
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** "This function computes a comprehensive set of metrics for the 'df2' dataset (Positionsdaten) by retrieving data from a database. It calculates various statistics including row counts, null ratios, numerical statistics, plausibility checks, and discount logic errors. The function handles database connections and ensures proper closure after use. It also performs additional calculations on loaded data to refine the null ratio metrics."
*   **Parameters:**
*   **Returns:**
    *   **metrics_df2** (`dict`): "A dictionary containing computed metrics for the df2 dataset, including row count, null ratios, statistical summaries, plausibility checks, and error counts."
*   **Usage:**
    *   Calls: `db_dashboard.get_db_connection`, `db_dashboard.get_scalar_metrics`, `db_dashboard.load`
    *   Called by: No other functions.

#### Function: `compute_metrics_combined`
   **Sequence diagram for compute_metrics_combined**
```mermaid
sequenceDiagram
    participant dashboard_compute_metrics_combined
    participant dashboard_load
    participant db_dashboard_compute_metrics_combined
    participant db_dashboard_get_db_connection
    participant db_dashboard_compute_metrics_combined
    participant db_dashboard_get_scalar_metrics
    dashboard_compute_metrics_combined ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_metrics_combined: return
    db_dashboard_compute_metrics_combined ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_metrics_combined: return
    db_dashboard_compute_metrics_combined ->> db_dashboard_get_scalar_metrics: []
```
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** "This function retrieves combined metrics from a database by first establishing a connection and fetching scalar metrics. It then executes a query to fetch data related to order position mismatches and constructs a dictionary containing boolean flags for uniqueness checks and the fetched DataFrame. Finally, it prints the loading duration and returns the constructed metrics dictionary."
*   **Parameters:**
*   **Returns:**
    *   **metrics_combined** (`dict`): "A dictionary containing boolean flags indicating whether certain IDs are unique and a DataFrame with order position mismatch data."
*   **Usage:**
    *   Calls: `db_dashboard.get_db_connection`, `db_dashboard.get_scalar_metrics`
    *   Called by: No other functions.

#### Function: `compute_positions_over_time`
   **Sequence diagram for compute_positions_over_time**
```mermaid
sequenceDiagram
    participant dashboard_compute_positions_over_time
    participant dashboard_load
    participant db_dashboard_compute_positions_over_time
    participant db_dashboard_get_db_connection
    dashboard_compute_positions_over_time ->> dashboard_load: []
    dashboard_load ->> dashboard_compute_positions_over_time: return
    db_dashboard_compute_positions_over_time ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_compute_positions_over_time: return
```
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** "This function retrieves position data over time from a database table named 'metric_positions_over_time'. It establishes a database connection, executes a SELECT query to fetch all records, and returns the resulting data as a pandas DataFrame. The function also measures and reports the execution time of the database operation."
*   **Parameters:**
*   **Returns:**
    *   **df_pos_time** (`pandas.DataFrame`): "A DataFrame containing all records from the 'metric_positions_over_time' table."
*   **Usage:**
    *   Calls: `db_dashboard.get_db_connection`
    *   Called by: No other functions.

### File: `metrics.py`

#### Function: `load_data`
   **Sequence diagram for load**
```mermaid
sequenceDiagram
    participant db_dashboard_load
    participant db_dashboard_get_db_connection
    db_dashboard_load ->> db_dashboard_get_db_connection: []
    db_dashboard_get_db_connection ->> db_dashboard_load: return
```
*   **Signature:** `def load_data()`
*   **Description:** This function loads two datasets from Parquet files located at 'resources/Auftragsdaten_konvertiert' and 'resources/Positionsdaten_konvertiert'. It reads these files using pandas and returns both DataFrames as a tuple. The function serves as a data loading utility for subsequent processing steps.
*   **Parameters:**
*   **Returns:**
    *   **df** (`DataFrame`): "The first DataFrame loaded from the 'Auftragsdaten_konvertiert' Parquet file."
    *   **df2** (`DataFrame`): "The second DataFrame loaded from the 'Positionsdaten_konvertiert' Parquet file."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `ratio_null_values_column`
*   **Signature:** `def ratio_null_values_column(input_df)`
*   **Description:** This function computes the ratio of null values for each column in a given pandas DataFrame. It calculates the percentage of missing data per column and returns the results in a new DataFrame. The implementation leverages pandas' built-in methods to efficiently compute null ratios without explicit loops.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "DataFrame that is to be evaluated for null value ratios."
*   **Returns:**
    *   **null_ratio_df** (`pd.DataFrame`): "DataFrame containing two columns: 'index' (representing column names) and 'null_ratio' (the percentage of null entries in each column)."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `ratio_null_values_rows`
*   **Signature:** `def ratio_null_values_rows(input_df, relevant_columns=None)`
*   **Description:** "This function computes the percentage of rows in a DataFrame that contain at least one null value. It allows for evaluation across all columns or a subset of specified columns. The calculation involves determining the total number of rows, identifying rows with null values, and returning the ratio as a percentage."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "DataFrame that is to be evaluated."
    *   **relevant_columns** (`list`): "List of column identifiers; function will only evaluate these columns, by default None."
*   **Returns:**
    *   **row_ratio** (`float`): "Percentage value of rows with at least one null value in the given columns."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `Kundengruppe_containing_test`
*   **Signature:** `def Kundengruppe_containing_test(df, return_frame=False)`
*   **Description:** "This function evaluates a pandas DataFrame to determine the number of rows where the 'Kundengruppe' column contains the substring 'test' (case-insensitive). It optionally returns a filtered DataFrame of those rows. The function uses string operations to identify matching entries and counts them. If the return_frame flag is set to True, it returns both the count and the filtered DataFrame; otherwise, it only returns the count."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "The 'Auftragsdaten'-DataFrame that is to be evaluated."
    *   **return_frame** (`bool`): "If True, this function returns a DataFrame with all found test data, by default False."
*   **Returns:**
    *   **anzahl_test** (`int`): "Total number of test data rows."
    *   **test_Kundengruppen** (`pandas.DataFrame or None`): "DataFrame containing all found test data, returned only if return_frame = True."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `allgemeine_statistiken_num`
*   **Signature:** `def allgemeine_statistiken_num(input_df)`
*   **Description:** "This function computes basic statistical measures for all numeric columns within a given pandas DataFrame. It iterates through each numeric column, calculates the mean, median, standard deviation, minimum, and maximum values, and stores these statistics in a nested dictionary structure. The resulting dictionary maps each column name to its respective set of statistical values. The function is designed to work exclusively with numerical data and returns a structured representation of descriptive statistics."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "A pandas DataFrame that contains the data to be analyzed for statistical values."
*   **Returns:**
    *   **statistiken** (`dict`): "A nested dictionary where keys are column names and values are dictionaries containing the computed statistical values (mean, median, std, min, max) for each numeric column."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `plausibilitaetscheck_forderung_einigung`
*   **Signature:** `def plausibilitaetscheck_forderung_einigung(input_df)`
*   **Description:** "This function performs a plausibility check on a DataFrame by comparing the 'Einigung_Netto' and 'Forderung_Netto' columns. It identifies rows where the 'Einigung_Netto' value exceeds the 'Forderung_Netto' value, which is considered a significant error. The function calculates the difference between these values for all such rows, computes the average of these differences, and returns the differences, their count, and the average."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "DataFrame that is to be evaluated."
*   **Returns:**
    *   **statistik** (`pandas.Series`): "A list of all differences >0 as float values"
    *   **count** (`int`): "Total number of rows with difference >0"
    *   **avg** (`float`): "Average difference over all found instances"
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `uniqueness_check`
*   **Signature:** `def uniqueness_check(df, df2)`
*   **Description:** "The function 'uniqueness_check' verifies the uniqueness of specific ID columns across two pandas DataFrames. It takes two DataFrames as inputs, one containing 'Auftragsdaten' data and the other containing 'Positionsdaten' data. For each DataFrame, it checks whether the respective ID columns ('KvaRechnung_ID' and 'Position_ID') contain only unique values. The function returns a tuple of boolean values indicating the uniqueness status of these columns."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "DataFrame that contains the 'Auftragsdaten' data set"
    *   **df2** (`pandas.DataFrame`): "DataFrame that contains the 'Positionsdaten' data set"
*   **Returns:**
    *   **kvarechnung_id_is_unique** (`bool`): "True if column is unique."
    *   **position_id_is_unique** (`bool`): "True if column is unique."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `count_rows`
*   **Signature:** `def count_rows(input_df)`
*   **Description:** "This function serves as a helper utility to determine the number of rows present in a given pandas DataFrame. It takes a DataFrame as input, calculates its length using the built-in `len()` function, and returns that count as an integer. The function is designed to be simple and straightforward, focusing solely on row counting without any filtering or additional processing."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "DataFrame to be evaluated."
*   **Returns:**
    *   **count** (`int`): "The number of rows in the input DataFrame."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `split_dataframe`
*   **Signature:** `def split_dataframe(input_df, chunks=5)`
*   **Description:** "The function splits a given pandas DataFrame into a specified number of chunks using numpy's array_split method. It is intended to simulate time series data by dividing the dataset into segments. The function is marked as deprecated, indicating it is no longer recommended for use due to the addition of datetime columns that make this approach obsolete."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "The input DataFrame that needs to be split into multiple chunks."
    *   **chunks** (`int`): "The number of chunks to split the DataFrame into. Defaults to 5."
*   **Returns:**
    *   **split_data** (`list of pandas.DataFrame`): "A list containing the DataFrame split into the specified number of chunks."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `data_cleanliness`
   **Sequence diagram for data_cleanliness**
```mermaid
sequenceDiagram
    participant metrics_data_cleanliness
    participant metrics_ratio_null_values_rows
    participant metrics_data_cleanliness
    participant metrics_ratio_null_values_column
    metrics_data_cleanliness ->> metrics_ratio_null_values_rows: ['input_df', 'relevant_columns']
    metrics_ratio_null_values_rows ->> metrics_data_cleanliness: return
    metrics_data_cleanliness ->> metrics_ratio_null_values_column: ['input_df']
    metrics_ratio_null_values_column ->> metrics_data_cleanliness: return
```
*   **Signature:** `def data_cleanliness(input_df, group_by_col=None, specific_group=None)`
*   **Description:** "The function evaluates the cleanliness of a pandas DataFrame by calculating the ratio of null values both per column and per row. It supports optional grouping by a specified column to perform these calculations on subsets of the data. When no grouping column is provided, it returns overall null ratios for rows and columns. When a grouping column is specified, it computes grouped null value ratios for both rows and columns."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "DataFrame that is to be evaluated."
    *   **group_by_col** (`string`): "Column identifier for grouping, defaults to None"
    *   **specific_group** (`string`): "Passes a group entry to filter the result by, if any; defaults to None"
*   **Returns:**
    *   **null_ratio_rows** (`float or None`): "Percentage value of rows with at least one null value in the given columns."
    *   **null_ratio_cols** (`DataFrame or None`): "DataFrame, with null_ratio being the percentage amount of null entries in the column."
    *   **grouped_row_ratios** (`pandas.Series or None`): "Series containing the row ratios of all groups as float."
    *   **grouped_col_ratios** (`pandas.DataFrame or None`): "DataFrame containing groups and null-value-ratios per column for each."
*   **Usage:**
    *   Calls: `metrics.ratio_null_values_column`, `metrics.ratio_null_values_rows`
    *   Called by: No other functions.

#### Function: `groupby_col`
*   **Signature:** `def groupby_col(input_df, col)`
*   **Description:** "This function serves as a helper to group a pandas DataFrame by a specified column. It takes an input DataFrame and a column identifier, then applies the pandas groupby operation on that column with the 'observed' parameter set to True. The result is a grouped DataFrame object which can be used for further aggregation or analysis. The function does not perform any additional transformations or computations beyond the grouping operation itself."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "DataFrame that is to be evaluated."
    *   **col** (`string`): "Identifier of the column to be grouped by."
*   **Returns:**
    *   **input_df_grouped** (`pandas.DataFrame`): "A grouped DataFrame."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `discount_check`
*   **Signature:** `def discount_check(df2)`
*   **Description:** "The function 'discount_check' evaluates a DataFrame containing 'Positionsdaten' data to identify rows that may have discrepancies between their 'Plausibel' status and the net values in 'Einigung_Netto' and 'Forderung_Netto'. It counts the number of rows marked as not plausible, indicating potential errors in the dataset. The function uses a boolean mask to filter rows where the 'Plausibel' column is False and sums these to determine the count of potential errors."
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): "DataFrame containing the 'Positionsdaten' dataset."
*   **Returns:**
    *   **potential_errors** (`int`): "The number of potentially faulty rows based on the 'Plausibel' column."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `proformabelege`
*   **Signature:** `def proformabelege(df)`
*   **Description:** "This function evaluates a pandas DataFrame to identify rows that correspond to pro forma receipts based on a specific condition applied to the 'Einigung_Netto' column. It filters the DataFrame to include only those rows where the value in the 'Einigung_Netto' column is between 0.01 and 1, inclusive. The function then calculates the count of such rows and returns both the filtered DataFrame and the count as a tuple."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "DataFrame that is to be evaluated."
*   **Returns:**
    *   **proforma** (`pandas.DataFrame`): "DataFrame containing all found pro forma receipt rows"
    *   **proforma_count** (`int`): "Amount of found receipts"
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `position_count`
*   **Signature:** `def position_count(input_df)`
*   **Description:** "This function takes a pandas DataFrame as input and groups the data by the 'KvaRechnung_ID' column to count the number of associated positions for each unique ID. It then returns a new DataFrame containing the 'KvaRechnung_ID' and the corresponding count of positions, renamed to 'PositionsAnzahl'. The function leverages pandas groupby and count operations to perform the aggregation."
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): "DataFrame that is to be evaluated."
*   **Returns:**
    *   **position_count** (`pandas.DataFrame`): "DataFrame with the columns 'KvaRechnung_ID' and the amount of associated positions."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `false_negative_df`
*   **Signature:** `def false_negative_df(df)`
*   **Description:** "The function evaluates a DataFrame containing 'Auftragsdaten' data to identify cases where at least two out of three columns (Forderung_Netto, Empfehlung_Netto, Einigung_Netto) are negative, but the third column is not negative. It counts and returns the number of such inconsistencies. The function uses boolean masking to determine which rows meet the criteria for false negatives."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "DataFrame with 'Auftragsdaten' data set that is to be evaluated."
*   **Returns:**
    *   **error_count** (`int`): "Number of entries in any of the three columns Forderung, Empfehlung or Einigung failing the check."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `false_negative_df2`
*   **Signature:** `def false_negative_df2(df2)`
*   **Description:** "The function evaluates a 'Positionsdaten' dataset contained in a pandas DataFrame for entries in specific columns that fall outside of reasonable value ranges. It checks for negative values in columns such as 'Menge', 'Menge_Einigung', 'EP', 'Ep_Einigung', 'Forderung_Netto', and 'Einigung_Netto', and counts how many entries violate these constraints. The function aggregates the total number of invalid entries across all relevant columns and returns this count as an integer."
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): "DataFrame containing 'Positionsdaten' data set that is to be evaluated."
*   **Returns:**
    *   **total_errors** (`int`): "Total amount of non-valid entries aggregated over all relevant columns."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `above_50k`
*   **Signature:** `def above_50k(df)`
*   **Description:** This function filters a pandas DataFrame to identify records where the 'Einigung_Netto' column has a value greater than or equal to 50000. It is designed to flag potentially suspicious financial entries that may require manual review due to their high values. The function takes a DataFrame as input and returns a new DataFrame containing only those rows that meet the specified condition. The purpose is to aid in detecting outliers or anomalies in financial data that could indicate potential issues requiring further investigation.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "DataFrame that is to be evaluated."
*   **Returns:**
    *   **suspicious_data** (`pandas.DataFrame`): "Data frame containing suspiciously high positions"
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `outliers_by_damage`
*   **Signature:** `def outliers_by_damage(df, schadenart=None, set_quantile=0.99, column_choice='Forderung_Netto')`
*   **Description:** "This function identifies outliers in a specified numerical column of a pandas DataFrame based on a given quantile range, considering different damage types. It calculates symmetric upper and lower bounds for each group of damage types and filters the DataFrame to return rows that fall outside these bounds. The function allows filtering by a specific damage type and supports custom column selection for outlier detection."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "DataFrame to be evaluated"
    *   **schadenart** (`string`): "specific damage type label to filter for, by default None"
    *   **set_quantile** (`float`): "desired quantile range, symmetric upper/lower bound is inferred, by default 0.99"
    *   **column_choice** (`str`): "numeric column containing outliers, by default 'Forderung_Netto'"
*   **Returns:**
    *   **df_outlier** (`pandas.DataFrame`): "df containing all suspicious rows"
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `check_zeitwert`
*   **Signature:** `def check_zeitwert(df)`
*   **Description:** The function 'check_zeitwert' evaluates whether the values in the column 'Differenz_vor_Zeitwert_Netto' satisfy a specific condition related to 'Zeitwert = Forderung-Einigung'. It computes the relative error by comparing the difference between 'Forderung_Netto' and 'Einigung_Netto' with the 'Differenz_vor_Zeitwert_Netto'. This function is intended for use with 'Auftragsdaten' datasets. The result is a pandas Series containing only the non-zero error values.
*   **Parameters:**
    *   **df** (`_pandas.DataFrame`): "DataFrame containing 'Auftragsdaten' data set that is to be evaluated."
*   **Returns:**
    *   **zeitwert_error** (`pandas.Series`): "Series of all error values (float) found in the data frame"
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `positions_per_order_over_time`
*   **Signature:** `def positions_per_order_over_time(df, df2, time_col="CRMEingangszeit")`
*   **Description:** "The function 'positions_per_order_over_time' computes the average number of positions per order for each month. It takes two DataFrames, one containing order data and another with position data, and merges them based on a shared identifier. The function aggregates the data by month to calculate metrics such as average positions per order, total positions, and the count of orders. It also calculates the growth rate percentage of the average positions per order over time."
*   **Parameters:**
    *   **df** (`DataFrame`): "Auftragsdaten mit Spalte 'KvaRechnung_ID' und einer Zeitspalte."
    *   **df2** (`DataFrame`): "Positionsdaten mit Spalten 'KvaRechnung_ID' und 'Position_ID'."
    *   **time_col** (`str`): "Name der Zeitspalte in orders_df (z.B. 'CRMEingangszeit')."
*   **Returns:**
    *   **result** (`DataFrame`): "DataFrame mit Spalten: 'Zeitperiode', 'Avg_Positionen_pro_Auftrag', 'Total_Positionen', 'Anzahl_Auftraege', 'Growth_rate_%'"
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `error_frequency_by_weekday_hour`
*   **Signature:** `def error_frequency_by_weekday_hour(df, time_col="CRMEingangszeit", relevant_columns=None)`
*   **Description:** "Die Funktion aggregiert die Fehlerhäufigkeit (NaN-Werte) in einem DataFrame nach Wochentag und Stunde. Ein Auftrag gilt als fehlerhaft, wenn in mindestens einer der relevanten Spalten ein NaN-Wert vorkommt. Sie wandelt die Zeitspalte in ein Datetime-Format um, extrahiert Wochentag und Stunde, bestimmt relevante Spalten zur Prüfung auf NaN-Werte und berechnet anschließend die Fehlerquote pro Zeitfenster. Das Ergebnis ist ein DataFrame mit den Spalten 'weekday', 'hour', 'total_rows', 'error_rows' und 'error_rate'."
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): "Auftragsdaten-DataFrame (z.B. Auftragsdaten_konvertiert), muss 'KvaRechnung_ID' und die Zeitspalte enthalten."
    *   **time_col** (`string`): "Name der Zeitspalte in df, z.B. 'CRMEingangszeit'."
    *   **relevant_columns** (`list`): "Liste der Spalten, die auf NaN geprüft werden sollen. Wenn None -> alle Spalten außer 'KvaRechnung_ID' und time_col."
*   **Returns:**
    *   **result** (`pandas.DataFrame`): "DataFrame mit Spalten: 'weekday' (Name des Wochentags), 'hour' (Stunde von 0 bis 23), 'total_rows' (Anzahl Aufträge in diesem Zeit-Slot), 'error_rows' (Anzahl fehlerhafter Aufträge in diesem Slot), 'error_rate' (Fehlerquote in Prozent)."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `get_mismatched_entries`
*   **Signature:** `def get_mismatched_entries(df, threshold=0.2)`
*   **Description:** "The function 'get_mismatched_entries' computes similarity scores between pairs of 'Gewerk_Name' and 'Handwerker_Name' entries in a DataFrame using sentence embeddings. It leverages a pre-trained multilingual model to encode the text data and calculates cosine distances to determine similarity. Entries with similarity scores below a given threshold are identified as mismatches and returned sorted by similarity score."
*   **Parameters:**
    *   **df** (`DataFrame`): "A pandas DataFrame containing columns 'Gewerk_Name' and 'Handwerker_Name' to compare."
    *   **threshold** (`float`): "A float value representing the minimum similarity score threshold below which entries are considered mismatches. Default is 0.2."
*   **Returns:**
    *   **mismatches** (`DataFrame`): "A copy of the input DataFrame filtered to include only rows where the similarity score is less than the specified threshold, sorted in ascending order of similarity score."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `handwerker_gewerke_outlier`
*   **Signature:** `def handwerker_gewerke_outlier(df)`
*   **Description:** This function processes a DataFrame to identify outliers in the relationship between craftsmen and their specialties (Gewerke). It calculates the ratio of each specialty per craftsman and flags those specialties as outliers if the craftsman has more than one specialty and the ratio of that specialty is less than 20%. The function filters out missing values and returns a DataFrame with the results.
*   **Parameters:**
    *   **df** (`DataFrame`): "A pandas DataFrame containing columns 'Handwerker_Name' and 'Gewerk_Name'."
*   **Returns:**
    *   **stats** (`DataFrame`): "A pandas DataFrame with columns 'Handwerker_Name', 'Gewerk_Name', 'count', 'total_count', 'ratio', 'anzahl_gewerke', and 'is_outlier'."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `check_keywords_vectorized`
*   **Signature:** `def check_keywords_vectorized(df)`
*   **Description:** "This function processes a DataFrame to classify trades based on keyword matching between the 'Handwerker_Name' column and predefined keyword mappings for various trade categories. It identifies whether a trade is confirmed by name, flagged as a conflict due to mismatched keywords, or lacks keyword information. The function uses vectorized string operations for efficiency."
*   **Parameters:**
    *   **df** (`DataFrame`): "A pandas DataFrame containing columns 'Handwerker_Name' and 'Gewerk_Name' which are used to determine trade classifications based on keyword matching."
*   **Returns:**
    *   **final_result** (`ndarray or Series`): "An array or Series of strings indicating the classification result for each row in the DataFrame: 'CONFIRMED_BY_NAME' if the name matches the expected trade, 'CONFLICT_WITH_<TRADE>' if there's a mismatch, or 'NO_KEYWORD_INFO' if no relevant keywords were found."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

#### Function: `abgleich_auftraege`
*   **Signature:** `def abgleich_auftraege(df1, df2)`
*   **Description:** "Die Funktion 'abgleich_auftraege' vergleicht die Kopfdaten von Aufträgen (df1) mit der Summe ihrer Positionen (df2). Sie gruppiert die Positionsdaten nach 'Kva_RechnungID', bildet die Summen für 'Forderung_Netto' und 'Einigung_Netto', und führt einen Vergleich mit den Werten in df1 durch. Dabei werden Gleitkommazahlen berücksichtigt. Die Funktion gibt eine Liste der Abweichungen zurück, wobei nur die IDs angezeigt werden, bei denen die Werte nicht übereinstimmen."
*   **Parameters:**
    *   **df1** (`pd.DataFrame`): "Dataframe mit den Auftragsdaten (Soll-Werte). Muss zwingend folgende Spalten enthalten: 'Kva_RechnungID', 'Forderung_Netto', 'Einigung_Netto'."
    *   **df2** (`pd.DataFrame`): "Dataframe mit den Positionsdaten (Ist-Werte). Muss zwingend folgende Spalten enthalten: 'KvaRechnung_ID', 'Forderung_Netto', 'Einigung_Netto'."
*   **Returns:**
    *   **result_df** (`pd.DataFrame`): "Eine Liste der Abweichungen. Der Dataframe enthält nur die IDs, bei denen die Werte nicht übereinstimmen. Enthaltene Spalten: 'KvaRechnung_ID', 'Diff_Forderung', 'Diff_Einigung'."
*   **Usage:**
    *   Calls: No other functions.
    *   Called by: No other functions.

---