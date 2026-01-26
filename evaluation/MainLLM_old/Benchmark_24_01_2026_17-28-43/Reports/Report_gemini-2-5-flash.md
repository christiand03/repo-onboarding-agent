# Project Documentation: analytics-application-development-uni

## 1. Project Overview

-   **Description:** The project is a Streamlit-based data analytics application designed for monitoring and evaluating data quality. It integrates with DuckDB for data storage and leverages various libraries for data processing, metric calculation, and visualization. Its core functionality includes detecting data anomalies, performing plausibility checks, analyzing data drift over time, and providing interactive dashboards for insights into numerical and textual data quality.
-   **Key Features:**
    -   Interactive Streamlit Dashboard
    -   Comprehensive Data Quality Metrics (numerical, textual)
    -   Plausibility and Logic Error Checks
    -   Data Drift Detection and Reporting
    -   Integration with DuckDB for efficient data management
-   **Tech Stack:** altair, duckdb, evidently, ipython, numpy, pandas, sentence-transformers, streamlit, streamlit-option-menu, torch

*   **Repository Structure:**
    ```mermaid
    graph LR
    project_root["<b>analytics-application-development-uni</b>"]
    _file__DS_Store[".DS_Store"]
    project_root --> _file__DS_Store
    _file__gitignore[".gitignore"]
    project_root --> _file__gitignore
    _file__Notebook_ipynb["Notebook.ipynb"]
    project_root --> _file__Notebook_ipynb
    _file__build_db_py["build_db.py"]
    project_root --> _file__build_db_py
    _file__dashboard_py["dashboard.py"]
    project_root --> _file__dashboard_py
    _file__data_cleaning_py["data_cleaning.py"]
    project_root --> _file__data_cleaning_py
    _file__data_drift_metrics_py["data_drift_metrics.py"]
    project_root --> _file__data_drift_metrics_py
    _file__data_exploration_py["data_exploration.py"]
    project_root --> _file__data_exploration_py
    _file__data_exploration2_py["data_exploration2.py"]
    project_root --> _file__data_exploration2_py
    _file__db_dashboard_py["db_dashboard.py"]
    project_root --> _file__db_dashboard_py
    _file__metrics_py["metrics.py"]
    project_root --> _file__metrics_py
    _file__readme_md["readme.md"]
    project_root --> _file__readme_md
    _file__requirements_txt["requirements.txt"]
    project_root --> _file__requirements_txt
    _streamlit["<b>.streamlit/</b><br/>config.toml"]
    project_root --> _streamlit
    Notizen["<b>Notizen/</b><br/>Analytics Application Development.md<br/>Dokumentation AAD.md<br/>Meeting_17-11-25.md"]
    project_root --> Notizen
    app_pages["<b>app_pages/</b><br/>__init__.py<br/>page1.py<br/>page2.py<br/>page3.py<br/>page4.py<br/>page5.py"]
    project_root --> app_pages
    assets["<b>assets/</b><br/>favicon.png<br/>logo.png"]
    project_root --> assets
    ```

## 2. Installation

### Dependencies
- altair==5.5.0
- duckdb==1.4.3
- evidently==0.7.20
- ipython==8.12.3
- numpy==2.3.5
- pandas==2.3.3
- sentence-transformers==5.2.0
- streamlit==1.51.0
- streamlit-option-menu==0.4.0
- torch==2.9.1+cu126

pip install -r requirements.txt
### Setup Guide
Information not found
### Quick Startup
Information not found

## 3. Use Cases & Commands
The project serves as a comprehensive data analytics and quality monitoring solution. Key use cases include:

*   **Monitor Data Quality:** Utilize the Streamlit dashboard (`dashboard.py` or `db_dashboard.py`) to get an overview of data quality, including null value ratios, numerical anomalies, and textual inconsistencies across various datasets.
*   **Perform Plausibility Checks:** Identify and investigate logical errors in financial data, such as `Forderung_Netto` being less than `Einigung_Netto`, unplausible discounts, or inconsistent sign logic (`metrics.plausibilitaetscheck_forderung_einigung`, `metrics.discount_check`, `metrics.false_negative_df1`, `metrics.false_negative_df2`).
*   **Detect Data Drift:** Evaluate changes in data distributions and characteristics over different time periods using the data drift evaluation page, which leverages the `evidentlyai` framework (`app_pages/page5.py`, `data_drift_metrics.py`).
*   **Identify Textual Anomalies:** Pinpoint suspicious trade-company associations (heuristic and semantic) and detect test data within production datasets (`metrics.mismatched_entries`, `metrics.handwerker_gewerke_outlier`, `metrics.Kundengruppe_containing_test`).
*   **Data Preparation and Database Building:** Clean raw data, enrich it with timestamps, and construct the analytical DuckDB database used by the dashboard (`data_cleaning.py`, `build_db.py`).

**Primary Commands:**
*   To launch the Streamlit dashboard: `streamlit run dashboard.py` (or `streamlit run db_dashboard.py`)
*   To build/update the analytical database: `python build_db.py` (inferred)

## 4. Architecture
The Mermaid Syntax to visualize Graphs is not set up yet and will be added


## 5. Code Analysis

### File: `app_pages/page1.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1: dict, metrics_df2: dict, metrics_combined: dict, pot_df: pandas.DataFrame, comparison_df: pandas.DataFrame | None, issues_df: pandas.DataFrame | None)`
*   **Description:** The `show_page` function renders a comprehensive data quality dashboard within a Streamlit application. It processes various dataframes and dictionaries containing metrics and issues to display Key Performance Indicators (KPIs) such as row counts, null ratios, proforma receipts, empty orders, and ID uniqueness. The function also generates interactive Altair charts, including a bar chart for top N null values per column and a heatmap for error frequency by weekday and hour. Additionally, it presents a trend analysis of average positions per order over time, allowing users to filter the date range and providing insights into the trend.
*   **Parameters:**
    *   **metrics_df1** (`dict`): A dictionary containing various metrics for the first dataset, such as row counts, null ratios, and error frequency data.
    *   **metrics_df2** (`dict`): A dictionary containing various metrics for the second dataset, primarily row counts and null ratios.
    *   **metrics_combined** (`dict`): A dictionary containing combined metrics, specifically used for checking the uniqueness of various IDs.
    *   **pot_df** (`pandas.DataFrame`): A DataFrame containing time-series data for analyzing the trend of average positions per order.
    *   **comparison_df** (`pandas.DataFrame | None`): An optional DataFrame used to calculate percentage changes (deltas) for the displayed KPIs.
    *   **issues_df** (`pandas.DataFrame | None`): An optional DataFrame containing overall issue counts to be displayed as a KPI.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name: str)`
*   **Description:** This function calculates and formats the percentage change for a specified metric. It first checks if a global or externally defined `comparison_df` DataFrame is available and not empty. If the DataFrame is valid, it attempts to locate a row where the 'Metric' column matches the provided `metric_name`. If a matching metric is found, it extracts the 'Percent_Change' value and returns it as a formatted string, including its sign and a percentage symbol. If `comparison_df` is invalid or the metric is not found, the function returns None.
*   **Parameters:**
    *   **metric_name** (`str`): The name of the metric for which to retrieve the percentage change.
*   **Returns:**
    *   **percentage_change** (`str | None`): A formatted string representing the percentage change (e.g., '+5.23%') if the metric is found and `comparison_df` is valid, otherwise None.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `app_pages/page2.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1: pandas.DataFrame, metrics_df2: pandas.DataFrame, metrics_combined: pandas.DataFrame, comparison_df: pandas.DataFrame, issues_df: pandas.DataFrame)`
*   **Description:** This function, `show_page`, is responsible for rendering the second page of a dashboard, focusing on the data quality of numeric column data. It calculates and displays key performance indicators (KPIs) such as numerical anomalies, errors in 'current value' data, counts of high-value orders, and discrepancies between order and position sums. The function also visualizes trends for these KPIs over time using an interactive Altair chart. Finally, it presents detailed tables of problematic data points, including incorrect 'Zeitwerte', sum discrepancies, and orders exceeding 50,000€, with options to download these details as CSV files.
*   **Parameters:**
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **metrics_combined** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order and position data
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:**
    *   **void** (`None`): This function does not return any explicit value; it renders content directly to a Streamlit page.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name: str)`
*   **Description:** This function retrieves and formats the percentage change for a specified metric from a `comparison_df` DataFrame. It first checks if `comparison_df` is available and not empty. If the DataFrame is invalid, it returns `None`. Otherwise, it filters the DataFrame to locate the row corresponding to the given `metric_name`. If a matching metric is found, the function extracts its 'Percent_Change' value, formats it as a signed string with two decimal places and a percentage symbol, and returns this string. If the metric is not found, it returns `None`.
*   **Parameters:**
    *   **metric_name** (`str`): The name of the metric to look up within the 'Metric' column of the `comparison_df`.
*   **Returns:**
    *   **formatted_percentage_change** (`str | None`): A string representing the percentage change, formatted with a sign and two decimal places (e.g., "+5.23%"), or `None` if `comparison_df` is empty, `None`, or the `metric_name` is not found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `prepare_trend_data`
*   **Signature:** `def prepare_trend_data(df: pandas.DataFrame, label: string, time_col: str = "CRMEingangszeit")`
*   **Description:** This helper function processes a pandas DataFrame to aggregate its data into monthly intervals. It takes a DataFrame, a label for the aggregated data, and an optional timestamp column name. The function first validates the input DataFrame and the presence of the timestamp column. It then converts the specified time column to datetime objects, extracts the month, groups the data by month, counts the entries, and assigns a category label. The primary goal is to prepare data for trend analysis by providing monthly aggregated counts.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing computed metric values over time.
    *   **label** (`string`): label for aggregated data, written to column 'Kategorie' of the returned df
    *   **time_col** (`str`): label of the timestamp column in df, by default "CRMEingangszeit"
*   **Returns:**
    *   **aggregated** (`pandas.DataFrame`): df with metric values aggregated by month. Has a column 'Kategorie' for labels. This returns an empty df if no timestamp was passed.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions.

### File: `app_pages/page3.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1: pandas.DataFrame, metrics_df2: pandas.DataFrame, comparison_df: pandas.DataFrame, issues_df: pandas.DataFrame)`
*   **Description:** The `show_page` function is responsible for rendering the third page of a dashboard, which focuses on visualizing data quality metrics for textual column data. It processes several input DataFrames to calculate and display Key Performance Indicators (KPIs) related to textual data issues, the presence of test data, and suspicious trade-company associations using Streamlit. The function also provides interactive visualizations of error trends over time using Altair charts and offers detailed tables for raw data and outlier analysis, including options to download the data. It utilizes nested helper functions, `get_delta` for calculating percentage changes and `prepare_trend_data` for aggregating time-series data.
*   **Parameters:**
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name: str)`
*   **Description:** This function calculates and formats the percentage change for a specified metric. It first checks if a global `comparison_df` DataFrame is available and not empty. If valid, it attempts to locate a row in `comparison_df` where the 'Metric' column matches the provided `metric_name`. If a match is found, it retrieves the 'Percent_Change' value from that row, formats it as a signed percentage string (e.g., "+5.23%"), and returns it. If `comparison_df` is invalid or the metric is not found, the function returns `None`.
*   **Parameters:**
    *   **metric_name** (`str`): The name of the metric for which to retrieve the percentage change.
*   **Returns:**
    *   **percentage_change_string** (`str | None`): A formatted string representing the percentage change (e.g., '+5.23%') if the metric is found and `comparison_df` is valid, otherwise `None`.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `prepare_trend_data`
*   **Signature:** `def prepare_trend_data(df: pandas.DataFrame, label: str, time_col: str = "CRMEingangszeit")`
*   **Description:** This function prepares a given pandas DataFrame for time series trend analysis and visualization. It first performs validation checks on the input DataFrame and the specified time column. If valid, it converts the designated time column to datetime objects, extracts the month, and then aggregates the data by month, counting the number of entries for each period. Finally, it adds a categorical label to the aggregated data before returning the processed DataFrame.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): The input DataFrame containing the raw data to be processed for trend analysis.
    *   **label** (`str`): A string label to assign to the 'Kategorie' column in the output aggregated DataFrame.
    *   **time_col** (`str`): The name of the column in the DataFrame that contains the time-related data. Defaults to 'CRMEingangszeit'.
*   **Returns:**
    *   **aggregated** (`pandas.DataFrame`): A DataFrame aggregated by month, containing 'Monat' (month as timestamp), 'Anzahl' (count of entries), and 'Kategorie' (the provided label) columns. Returns an empty DataFrame if initial validation fails.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `app_pages/page4.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1: dict, metrics_df2: dict, comparison_df: pandas.DataFrame, issues_df: pandas.DataFrame)`
*   **Description:** This function, show_page, is designed to render a comprehensive data quality and logic error analysis page within a Streamlit application. It processes multiple input dataframes (metrics_df1, metrics_df2, comparison_df, issues_df) to extract and calculate various key performance indicators and detailed issue lists. The page is structured with multiple tabs, each dedicated to a specific type of check, such as plausibility errors, discount logic, proforma receipts, and sign consistency validation. It utilizes Streamlit widgets for interactive data exploration and Altair for data visualization, allowing users to view metrics, distributions, top outliers, and download detailed issue reports.
*   **Parameters:**
    *   **metrics_df1** (`dict`): A dictionary containing various metrics and dataframes related to the first dataset, such as plausibility data, proforma receipts, and false negative counts.
    *   **metrics_df2** (`dict`): A dictionary containing metrics and dataframes for the second dataset, including plausibility counts, discount errors, and false negative details.
    *   **comparison_df** (`pandas.DataFrame`): A DataFrame used to calculate percentage changes (deltas) for various metrics, expected to contain 'Metric' and 'Percent_Change' columns.
    *   **issues_df** (`pandas.DataFrame`): A DataFrame or dictionary containing aggregated issue counts, specifically used to retrieve 'plausi_issues'.
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name: str)`
*   **Description:** This function calculates and formats the percentage change for a specified metric. It first checks if a global 'comparison_df' DataFrame is available and contains data. If the DataFrame is valid, it attempts to locate the row corresponding to the 'metric_name'. If the metric is found, it extracts the 'Percent_Change' value and returns it as a formatted string, including its sign and a percentage symbol. If the DataFrame is not available, empty, or the metric is not found, the function returns None.
*   **Parameters:**
    *   **metric_name** (`str`): The name of the metric for which to retrieve the percentage change.
*   **Returns:**
    *   **percentage_change** (`str | None`): A formatted string representing the percentage change (e.g., '+5.23%') if the metric is found, otherwise None.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `app_pages/page5.py`

#### Function: `load_df`
*   **Signature:** `def load_df(df_type: str)`
*   **Description:** This function establishes a read-only connection to a DuckDB database named "dashboard_data.duckdb". It conditionally loads data into a Pandas DataFrame based on the `df_type` parameter. If `df_type` is "df", it queries the "auftragsdaten" table; if `df_type` is "df2", it queries the "positionsdaten" table. The function ensures the database connection is closed after the query, regardless of success or failure, and returns the resulting DataFrame.
*   **Parameters:**
    *   **df_type** (`str`): A string indicating which type of DataFrame to load. Expected values are 'df' for 'auftragsdaten' or 'df2' for 'positionsdaten'.
*   **Returns:**
    *   **df** (`pandas.DataFrame`): A Pandas DataFrame containing the data retrieved from the specified database table.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `fetch_reports_table`
*   **Signature:** `def fetch_reports_table()`
*   **Description:** This function is responsible for fetching and processing report metadata. It reads filenames from the 'resources/reports' directory, parses these filenames by splitting them, and then constructs a pandas DataFrame. The DataFrame is initialized with specific column names, undergoes a column drop operation, and has certain values in the 'Quelle' column replaced for better readability. The function ultimately returns this cleaned and structured DataFrame.
*   **Parameters:** None
*   **Returns:**
    *   **df_reports** (`pandas.DataFrame`): A pandas DataFrame containing processed report metadata, derived from filenames in the 'resources/reports' directory, with columns like 'Quelle', 'Start Ref.', 'Ende Ref.', 'Start Vergl.', and 'Ende Vergl.'.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `refresh_table`
*   **Signature:** `def refresh_table()`
*   **Description:** This function, `refresh_table`, is designed to update the `reports_table` within Streamlit's session state. It achieves this by calling `fetch_reports_table()` to retrieve the latest data and then assigns the result to `st.session_state.reports_table`. This effectively refreshes the displayed or processed reports data in the application.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `show_page`
*   **Signature:** `def show_page()`
*   **Description:** The `show_page` function renders a Streamlit dashboard page designed for data drift evaluation. It initializes by connecting to a DuckDB database to retrieve the earliest and latest `CRMEingangszeit` from `auftragsdaten`, which are then used to set date picker boundaries. The page presents a user interface where users can select a data source (Auftragsdaten or Positionsdaten) and define reference and evaluation date ranges. Upon form submission, it determines the expected path for an HTML report. If the report does not exist or a refresh is forced, it generates the report using `data_drift_evaluation` before displaying it; otherwise, it loads and displays the existing report.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

### File: `build_db.py`

#### Function: `calc_percent`
*   **Signature:** `def calc_percent(row: dict)`
*   **Description:** This function calculates the percentage change between an 'Old_Value' and a 'Current_Value' provided within a row object. It first extracts 'Old_Value', 'Current_Value', and 'Absolute_Change' from the input row. Special handling is implemented for cases where 'Old_Value' is zero: if 'Current_Value' is also zero, it returns 0.0; otherwise, it returns 100.0. For all other scenarios, the percentage is calculated as (Absolute_Change / Old_Value) * 100.
*   **Parameters:**
    *   **row** (`dict`): A dictionary-like object (e.g., pandas Series) expected to contain 'Old_Value', 'Current_Value', and 'Absolute_Change' keys.
*   **Returns:**
    *   **percentage_change** (`float`): The calculated percentage change between the old and current values, or 0.0/100.0 for specific edge cases.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `dashboard.py`

#### Function: `load`
*   **Signature:** `def load()`
*   **Description:** This function is responsible for loading two distinct datasets from Parquet files into pandas DataFrames. It reads 'resources/Auftragsdaten_konvertiert' into a DataFrame named 'df' and 'resources/Positionsdaten_konvertiert' into a DataFrame named 'df2'. The primary purpose is to prepare these datasets for subsequent analysis or display within a dashboard context. It leverages the `pd.read_parquet` function for efficient data retrieval.
*   **Parameters:** None
*   **Returns:**
    *   **df** (`pandas.DataFrame`): A pandas DataFrame containing data loaded from the 'resources/Auftragsdaten_konvertiert' Parquet file.
    *   **df2** (`pandas.DataFrame`): A pandas DataFrame containing data loaded from the 'resources/Positionsdaten_konvertiert' Parquet file.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_metrics_df1`
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** This function is responsible for calculating a comprehensive set of metrics for a DataFrame, referred to as 'df1' or 'Auftragsdaten'. It begins by loading the primary data. Subsequently, it performs various analytical checks and calculations, including plausibility checks, zeitwert error detection, proforma document analysis, data cleanliness assessments, error frequency by weekday/hour, outlier detection for craftsman/craft comparisons, and false negative identification. Each major calculation step measures and prints its execution time. Finally, all computed metrics are aggregated into a dictionary and returned.
*   **Parameters:** None
*   **Returns:**
    *   **metrics_df1** (`dict`): A dictionary containing various calculated metrics for 'df1' (Auftragsdaten), including row counts, null ratios, plausibility checks, zeitwert errors, proforma document details, data cleanliness ratios, error frequencies, false negatives, mismatched entries, and outlier analysis.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_metrics_df2`
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** This function computes various expensive metrics specifically for `df2` (position data). It first loads the necessary data using `load()`, then sequentially calculates plausibility checks, discount details, and false negative statistics. It also calculates fundamental metrics like row counts and null ratios. Finally, it compiles all these results into a dictionary named `metrics_df2`, which it then returns.
*   **Parameters:** None
*   **Returns:**
    *   **metrics_df2** (`dict`): A dictionary containing various computed metrics for `df2`, including row counts, null value ratios, discount check errors, position counts, plausibility check results, false negative statistics, and discount details.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_metrics_combined`
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** This function calculates a set of combined metrics that require two DataFrames. It begins by printing a status message and recording the start time. It then loads two DataFrames, presumably from a `load()` function, and proceeds to perform uniqueness checks on 'kva_id' and 'position_id' using `mt.uniqueness_check`. Additionally, it reconciles orders using `mt.abgleich_auftraege`. The results of these checks are compiled into a dictionary, which is then returned after printing the total calculation time.
*   **Parameters:** None
*   **Returns:**
    *   **metrics_combined** (`dict`): A dictionary containing the calculated combined metrics, including 'kvarechnung_id_is_unique' (boolean/status for KVA ID uniqueness), 'position_id_is_unique' (boolean/status for position ID uniqueness), and 'auftraege_abgleich' (result of order reconciliation).
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `compute_positions_over_time`
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** This function calculates the number of positions per order over time. It begins by loading two dataframes, `df` and `df2`, using an internal `load()` function. It then records the start time to measure the duration of the calculation. The core logic involves calling `mt.positions_per_order_over_time` with the loaded dataframes and a specified time column. Finally, it prints the calculation duration and returns the resulting dataframe.
*   **Parameters:** None
*   **Returns:**
    *   **positions_over_time_df** (`pandas.DataFrame`): A DataFrame containing the calculated positions per order over time, as computed by `mt.positions_per_order_over_time`.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_issues_df`
*   **Signature:** `def compute_issues_df()`
*   **Description:** The `compute_issues_df` function aggregates various error and issue counts from predefined metric dataframes, specifically `metrics_df1` and `metrics_combined`. It retrieves individual metric values such as `zeitwert_errors_count`, `above_50k_df`, `mismatched_entries`, and several others. These individual counts are then categorized into `numeric_issues`, `text_issues`, and `plausi_issues`, which are summed to determine an `overall_issues` total. The function then compiles these categorized and individual issue counts into a dictionary and converts it into a pandas DataFrame, which is subsequently returned.
*   **Parameters:** None
*   **Returns:**
    *   **df_issues** (`pandas.DataFrame`): A pandas DataFrame containing aggregated and individual issue counts, categorized into numeric, text, and plausibility issues, along with an overall total and individual metric counts.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_comparison_metrics`
*   **Signature:** `def compute_comparison_metrics()`
*   **Description:** This function initializes a dictionary named `data` that contains predefined comparison metrics, their current values, old values, and a zero percent change. It also defines a static list of integer indices. The function then constructs a pandas DataFrame using this `data` dictionary and the specified indices. Finally, it returns the newly created DataFrame.
*   **Parameters:** None
*   **Returns:**
    *   **df** (`pandas.DataFrame`): A pandas DataFrame containing 'Metric', 'Current_Value', 'Old_Value', and 'Percent_Change' columns, indexed by a predefined list of integers.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `data_cleaning.py`

#### Function: `load_data`
*   **Signature:** `def load_data()`
*   **Description:** This function is responsible for loading raw data from the 'resources' folder. It expects to find three specific .parquet files: 'Auftragsdaten', 'Positionsdaten', and 'Auftragsdaten_Zeit'. The function reads each of these files into separate pandas DataFrames and then returns all three DataFrames. A message indicating data loading progress is printed to the console.
*   **Parameters:** None
*   **Returns:**
    *   **Auftragsdaten** (`pandas.DataFrame`): A DataFrame containing the data from 'resources/Auftragsdaten'.
    *   **Positionsdaten** (`pandas.DataFrame`): A DataFrame containing the data from 'resources/Positionsdaten'.
    *   **Auftragsdaten_Zeit** (`pandas.DataFrame`): A DataFrame containing the data from 'resources/Auftragsdaten_Zeit'.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `data_cleaning`
*   **Signature:** `def data_cleaning(df: pandas.DataFrame, df2: pandas.DataFrame, df3: pandas.DataFrame)`
*   **Description:** This function `data_cleaning` merges three raw pandas DataFrames: 'Auftragsdaten' (df), 'Positionsdaten' (df2), and 'Auftragsdaten_Zeit' (df3). It enriches the primary dataframes by adding relevant timestamp information and new columns, such as the count of positions per order. The function performs extensive data cleaning, including replacing custom null indicators, correcting common typing errors, and optimizing memory usage through type conversions and downcasting of various columns. Finally, it identifies and flags discount positions within the 'Positionsdaten' DataFrame.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set
    *   **df2** (`pandas.DataFrame`): DataFrame containing 'Positionsdaten' data set
    *   **df3** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten_Zeit' data set
*   **Returns:**
    *   **df** (`pandas.DataFrame`): The cleaned 'Auftragsdaten' DataFrame with timestamp information and additional columns.
    *   **df2** (`pandas.DataFrame`): The cleaned 'Positionsdaten' DataFrame with timestamp information, additional columns, and discount position flags.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `data_drift_metrics.py`

#### Function: `check_start_end_date`
*   **Signature:** `def check_start_end_date(start: datetime, end: datetime)`
*   **Description:** This helper function takes two datetime objects, `start` and `end`, as input. Its primary purpose is to ensure that the `start` date chronologically precedes the `end` date. It achieves this by comparing the two dates and, if `start` is found to be later than `end`, it swaps their values. The function then returns the chronologically ordered pair of datetime values.
*   **Parameters:**
    *   **start** (`datetime`): The assumed beginning of the interval.
    *   **end** (`datetime`): The assumed end of the interval.
*   **Returns:**
    *   **sorted_datetimes** (`tuple[datetime, datetime]`): A pair of chronologically sorted datetime values, where the first element is the earlier date and the second is the later date.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `datetime_slice_mask`
*   **Signature:** `def datetime_slice_mask(df: pandas.Dataframe, start_date: date, end_date: date)`
*   **Description:** This helper function chronologically slices a pandas DataFrame based on a specified start and end date. It first converts the input dates to full datetime objects, setting the time to midnight for precise range comparison. A boolean mask is then applied to the DataFrame's 'CRMEingangszeit' column to filter rows within the defined period. Finally, the function converts the masked DataFrame into an `evidently.Dataset` using a specific data definition, conditionally choosing between `schema_df` or `schema_df2` based on the presence of 'Kundengruppe' or 'Menge' columns.
*   **Parameters:**
    *   **df** (`pandas.Dataframe`): The input pandas DataFrame to be sliced.
    *   **start_date** (`date`): The beginning date for the chronological slice (inclusive).
    *   **end_date** (`date`): The end date for the chronological slice (exclusive).
*   **Returns:**
    *   **sliced_ds** (`evidently.Dataset`): The chronologically sliced DataFrame, converted into an Evidently Dataset object.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `data_drift_evaluation`
*   **Signature:** `def data_drift_evaluation(df: pandas.DataFrame, start_date_reference: datetime, end_date_reference: datetime, start_date_eval: datetime, end_date_eval: datetime)`
*   **Description:** This function evaluates data drift between two datasets sampled from a given pandas DataFrame based on specified time intervals. It first ensures that the provided start and end dates for both the reference and evaluation periods are in chronological order. Subsequently, it slices the input DataFrame into reference and evaluation datasets using a mask-based approach. Depending on the presence of either 'Kundengruppe' or 'Menge' columns in the DataFrame, it configures an evidently.Report with a DataDriftPreset using a predefined set of columns relevant to the data type. The function then executes this report and saves the generated data drift snapshot as an HTML file, incorporating the date ranges into the filename for identification.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame to sample from
    *   **start_date_reference** (`datetime`): starting datetime of the reference, baseline dataset
    *   **end_date_reference** (`datetime`): ending datetime of the reference, baseline dataset
    *   **start_date_eval** (`datetime`): starting datetime of the evaluated dataset
    *   **end_date_eval** (`datetime`): ending datetime of the evaluated dataset
*   **Returns:** None
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

### File: `data_exploration.py`

#### Function: `load`
*   **Signature:** `def load()`
*   **Description:** This function is responsible for loading two separate Parquet files into pandas DataFrames. It reads 'resources/Auftragsdaten_konvertiert' into a DataFrame named 'df' and 'resources/Positionsdaten_konvertiert' into a DataFrame named 'df2'. The primary purpose is to prepare data for further exploration or processing by making these datasets available as DataFrames.
*   **Parameters:** None
*   **Returns:**
    *   **df** (`pandas.DataFrame`): The DataFrame loaded from the 'resources/Auftragsdaten_konvertiert' Parquet file.
    *   **df2** (`pandas.DataFrame`): The DataFrame loaded from the 'resources/Positionsdaten_konvertiert' Parquet file.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

### File: `data_exploration2.py`
*Analysis data not available for this component.*

### File: `db_dashboard.py`

#### Function: `get_db_connection`
*   **Signature:** `def get_db_connection()`
*   **Description:** The `get_db_connection` function is designed to establish a read-only connection to a DuckDB database. It first defines the path to the database file, which is hardcoded as "resources/dashboard_data.duckdb". Subsequently, it utilizes the `duckdb.connect` method to create a connection to this specified database file. The connection is explicitly configured to be read-only, ensuring data integrity. Finally, the function returns the active database connection object.
*   **Parameters:** None
*   **Returns:**
    *   **con** (`duckdb.Connection`): A read-only connection object to the DuckDB database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `compute_metrics_df1`
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** This function, `compute_metrics_df1`, is responsible for loading a comprehensive set of pre-computed metrics and dataframes related to 'Auftragsdaten' (order data) from a DuckDB database. It establishes a database connection and executes numerous SQL `SELECT *` queries to retrieve various data points, such as scalar metrics, null ratios, test data entries, plausibility differences, cleanliness metrics, proforma receipts, high-value orders, zeitwert errors, error frequencies, handwerker outliers, false negative statistics, semantic mismatches, empty orders, and outliers by damage. All retrieved data is then consolidated into a single dictionary, `metrics_df1`, which is returned by the function. The process includes logging the time taken for data loading.
*   **Parameters:** None
*   **Returns:**
    *   **metrics_df1** (`dict`): A dictionary containing various pre-computed metrics and dataframes related to order data. This includes scalar values like row counts and null ratios, as well as dataframes for null ratios per column, test data entries, plausibility differences, cleanliness metrics (grouped by columns and rows), proforma receipts, orders above 50k, zeitwert errors, error frequency, handwerker outliers, false negative statistics and details, semantic mismatches, empty orders, and outliers by damage.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_metrics_df2`
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** This function is responsible for loading a comprehensive set of metrics related to "Positionsdaten" (position data) from a database. It establishes a database connection, executes multiple SQL queries to fetch various scalar values and dataframes, and then aggregates these results into a single dictionary. The function also includes logging statements to indicate the start and completion of the metric loading process, along with the elapsed time.
*   **Parameters:** None
*   **Returns:**
    *   **metrics_df2** (`dict`): A dictionary containing various aggregated metrics for position data, including total row count, column null ratios, row null ratios, discount logic errors, position counts per invoice, plausibility error counts and average differences, false negative statistics, and detailed discount information.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_metrics_combined`
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** This function is responsible for loading and compiling various metrics from a database. It establishes a database connection and executes two SQL queries to retrieve scalar metrics and order position mismatch data. The retrieved data is then processed to form a dictionary containing boolean flags for uniqueness checks and a DataFrame. The function also measures and reports the total time taken for these operations before returning the compiled metrics.
*   **Parameters:** None
*   **Returns:**
    *   **metrics_combined** (`dict`): A dictionary containing various combined metrics, including boolean flags for uniqueness checks (kvarechnung_id_is_unique, kvarechnung_nummer_land_is_unique, position_id_is_unique) and a DataFrame for order position mismatches (auftraege_abgleich).
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_positions_over_time`
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** This function is designed to load historical position data from a database. It records the start time, establishes a database connection using `get_db_connection()`, and then executes a SQL query to retrieve all entries from the `metric_positions_over_time` table. The fetched data is converted into a DataFrame. Finally, it prints the time taken for the data loading operation and returns the resulting DataFrame.
*   **Parameters:** None
*   **Returns:**
    *   **df_pos_time** (`pandas.DataFrame`): A DataFrame containing historical position data over time, retrieved from the `metric_positions_over_time` table in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_comparison_metrics`
*   **Signature:** `def compute_comparison_metrics()`
*   **Description:** This function is designed to retrieve comparison metrics from a database. It records the start time of the operation, then establishes a database connection. It executes a SQL query to fetch all data from the 'metric_comparison' table and converts the result into a DataFrame. The function prints the time taken to load the metrics before returning the resulting DataFrame.
*   **Parameters:** None
*   **Returns:**
    *   **comparison_df** (`pandas.DataFrame`): A DataFrame containing all records retrieved from the 'metric_comparison' table in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `compute_issues_df`
*   **Signature:** `def compute_issues_df()`
*   **Description:** This function is responsible for loading issues metrics from a database. It first prints a message indicating the start of the loading process and records the current time. It then establishes a database connection, executes a SQL query to select all data from the 'issues' table, and retrieves the first row of the result as a DataFrame. Finally, it prints the time taken for the operation and returns the loaded issues data.
*   **Parameters:** None
*   **Returns:**
    *   **issues_df** (`pandas.Series`): A single row (Series) containing issues metrics loaded from the 'issues' table in the database.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

### File: `metrics.py`

#### Function: `load_data`
*   **Signature:** `def load_data()`
*   **Description:** This function is designed to load data from two distinct Parquet files. It reads the file located at "resources/Auftragsdaten_konvertiert" into a pandas DataFrame, assigned to the variable `df`. Subsequently, it reads the file "resources/Positionsdaten_konvertiert" into another pandas DataFrame, assigned to `df2`. The function then returns both of these loaded DataFrames.
*   **Parameters:** None
*   **Returns:**
    *   **df** (`pandas.DataFrame`): A pandas DataFrame containing data loaded from 'resources/Auftragsdaten_konvertiert'.
    *   **df2** (`pandas.DataFrame`): A pandas DataFrame containing data loaded from 'resources/Positionsdaten_konvertiert'.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `ratio_null_values_column`
*   **Signature:** `def ratio_null_values_column(input_df: pandas.DataFrame)`
*   **Description:** This helper function calculates the percentage of null values present in each column of a given pandas DataFrame. It achieves this by first identifying all `NaN` entries within the DataFrame using `isna()`. Subsequently, it computes the mean of these boolean indicators for each column, effectively yielding the proportion of nulls. This proportion is then scaled by 100 to represent a percentage and rounded to two decimal places for clarity. The final output is a new pandas DataFrame containing each column's name and its corresponding null value ratio.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:**
    *   **null_ratio_df** (`pd.DataFrame`): DataFrame of the form |column_name | null_ratio (float)| with null_ratio being the percentage amount of null entries in the column
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `ratio_null_values_rows`
*   **Signature:** `def ratio_null_values_rows(input_df: pandas.DataFrame, exclude_cols: list | None = None)`
*   **Description:** This helper function calculates the percentage of rows in a pandas DataFrame that contain at least one null value. It allows for specific columns to be excluded from this null-value check. The function first prunes the specified columns, then counts rows with any nulls in the remaining DataFrame. It returns 0.0 if the DataFrame is empty, otherwise it computes the ratio of null-containing rows to total rows, multiplied by 100.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): The DataFrame that is to be evaluated for null values.
    *   **exclude_cols** (`list or None`): A list of column identifiers; these columns will be pruned from calculations. Defaults to None, meaning no columns are excluded.
*   **Returns:**
    *   **row_ratio** (`float`): The percentage value of rows with at least one null value in the given columns.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `Kundengruppe_containing_test`
*   **Signature:** `def Kundengruppe_containing_test(df: pandas.DataFrame, return_frame: bool = False)`
*   **Description:** This function analyzes a pandas DataFrame, specifically looking for rows where the 'Kundengruppe' column contains the substring 'test' (case-insensitive). It aims to identify and count rows suspected to be part of a test data set within the 'Auftragsdaten' DataFrame. Depending on the 'return_frame' parameter, it either returns the total count of these identified test data rows or a new DataFrame containing only those rows.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): 'Auftragsdaten'-DataFrame that is to be evaluated.
    *   **return_frame** (`bool`): If True, this function returns exclusively a DataFrame with all found test data, by default False
*   **Returns:**
    *   **anzahl_test** (`int`): total number of test data rows, returned if return_frame is False.
    *   **test_Kundengruppen** (`pandas.DataFrame or None`): DataFrame containing all found test data, returned only if return_frame is True.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `plausibilitaetscheck_forderung_einigung`
*   **Signature:** `def plausibilitaetscheck_forderung_einigung(input_df: pandas.DataFrame)`
*   **Description:** This function performs a plausibility check on a pandas DataFrame to identify rows where the 'Einigung_Netto' value is greater than the 'Forderung_Netto' value. It first determines the appropriate ID column ('KvaRechnung_ID' or 'Position_ID') based on the DataFrame's columns. It then calculates the difference between the rounded 'Einigung_Netto' and 'Forderung_Netto' values, identifies faulty rows, and computes the count of such rows and their average difference. The function returns a DataFrame containing the faulty rows, the total count of faulty rows, and the average difference.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:**
    *   **results** (`pandas.DataFrame`): a DataFrame of all differences > 0 as float values alongside their ID, Forderung_Netto and Einigung_Netto
    *   **count** (`int`): total number of rows with difference >0
    *   **avg** (`float`): average difference over all found instances
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `uniqueness_check`
*   **Signature:** `def uniqueness_check(df: pandas.DataFrame, df2: pandas.DataFrame)`
*   **Description:** This function performs uniqueness checks on specified ID columns within two pandas DataFrames, `df` and `df2`. It first verifies the uniqueness of 'KvaRechnung_ID' in `df` and 'Position_ID' in `df2`. Subsequently, it checks for the uniqueness of the combined columns 'DH_ID' and 'KvaRechnung_Nummer' within `df` after removing rows with NaN values. The function returns boolean flags indicating the uniqueness status of these columns and a DataFrame containing any problematic duplicate entries for the combined 'DH_ID' and 'KvaRechnung_Nummer'.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame that contains the 'Auftragsdaten' data set
    *   **df2** (`pandas.DataFrame`): DataFrame that contains the 'Positionsdaten' data set
*   **Returns:**
    *   **kvarechnung_id_is_unique** (`bool`): True if the 'KvaRechnung_ID' column in `df` is unique.
    *   **position_id_is_unique** (`bool`): True if the 'Position_ID' column in `df2` is unique.
    *   **kvarechnung_nummer_land_is_unique** (`bool`): True if the combination of 'DH_ID' and 'KvaRechnung_Nummer' in `df` is unique after dropping NaN values.
    *   **df_problem** (`pandas.DataFrame`): A DataFrame containing rows from `df` that have duplicated 'DH_ID' and 'KvaRechnung_Nummer' combinations.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `count_rows`
*   **Signature:** `def count_rows(input_df: pandas.DataFrame)`
*   **Description:** This helper function calculates the total number of rows present in a given pandas DataFrame. It directly applies the `len()` function to the input DataFrame, which returns the count of its top-level elements, effectively counting the rows. The function then returns this calculated count as an integer.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame to be evaluated.
*   **Returns:**
    *   **count** (`int`): The number of rows in the input DataFrame.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `data_cleanliness`
*   **Signature:** `def data_cleanliness(input_df: pandas.DataFrame, group_by_col: string = "Kundengruppe", specific_group: string | None = None)`
*   **Description:** The `data_cleanliness` function evaluates a pandas DataFrame to determine the ratio of null values. It can calculate the percentage of rows containing any null values and the percentage of nulls per column. The function supports an optional grouping mechanism by a specified column, allowing for analysis across different categories. Furthermore, it can filter the results to focus on a particular group of interest. Depending on whether grouping is applied, it returns either overall null ratios or grouped null ratios.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
    *   **group_by_col** (`string, optional`): Column identifier for grouping, default = 'Kundengruppe'
    *   **specific_group** (`string, optional`): Passes a group entry to filter the result by, if any. Default = None
*   **Returns:**
    *   **null_ratio_rows** (`float or None`): Percentage value of rows with at least one null value in the given columns.
    *   **null_ratio_cols** (`DataFrame or None`): DataFrame, with null_ratio being the percentage amount of null entries in the column.
    *   **grouped_row_ratios** (`pandas.Series or None`): Series containing the row ratios of all groups as float.
    *   **grouped_col_ratios** (`pandas.DataFrame or None`): DataFrame containing groups and null-value-ratios per column for each.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `discount_check`
*   **Signature:** `def discount_check(df2: pandas.DataFrame)`
*   **Description:** This function, `discount_check`, evaluates a pandas DataFrame, `df2`, which represents the 'Positionsdaten' data set. Its primary purpose is to identify rows that describe a discount or similar item and verify if the 'Einigung_Netto' and 'Forderung_Netto' values accurately reflect this with appropriate negative or positive values. The function relies on the 'Plausibel' column, which is pre-calculated during database creation. It calculates the sum of rows where the 'Plausibel' column is `False`, indicating potential errors, and returns this count.
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): DataFrame containing the 'Positionsdaten' data set
*   **Returns:**
    *   **potential_errors** (`int`): The number of potentially faulty rows
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `proformabelege`
*   **Signature:** `def proformabelege(df: pandas.DataFrame)`
*   **Description:** The `proformabelege` function is designed to identify and count 'pro-forma' receipts within a given pandas DataFrame. It filters the input DataFrame, `df`, by selecting rows where the 'Einigung_Netto' column's value falls inclusively between 0.01 and 1. The function then calculates the number of rows that meet this criterion. It returns both the filtered DataFrame containing the pro-forma receipts and the count of these receipts.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:**
    *   **proforma** (`pandas.DataFrame`): DataFrame containing all found pro-forma receipt rows
    *   **proforma_count** (`int`): Amount of found receipts
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `position_count`
*   **Signature:** `def position_count(input_df: pandas.DataFrame)`
*   **Description:** This function calculates the number of positions associated with each unique 'KvaRechnung_ID' within a given pandas DataFrame. It groups the input DataFrame by 'KvaRechnung_ID', counts the 'Position_ID' for each group, and then resets the index. Finally, it renames the column containing the position count to 'PositionsAnzahl' before returning the resulting DataFrame.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:**
    *   **position_count** (`pandas.DataFrame`): DataFrame with the columns 'KvaRechnung_ID' and the amount of associated positions.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions.

#### Function: `empty_orders`
*   **Signature:** `def empty_orders(df: pandas.DataFrame)`
*   **Description:** This function, `empty_orders`, is designed to analyze a pandas DataFrame, specifically one containing 'Auftragsdaten'. Its main objective is to identify and quantify orders that do not have any associated positions. It achieves this by filtering the input DataFrame for rows where the 'PositionsAnzahl' column contains NaN values, indicating a lack of positions. The function then calculates the total count of these identified empty orders. Finally, it returns both the integer count of empty orders and a new DataFrame containing only those orders without positions.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame with 'Auftragsdaten' data set that is to be evaluated.
*   **Returns:**
    *   **empty_orders** (`int`): Total amount of orders that do not have any positions associated with them.
    *   **empty_order_df** (`pandas.DataFrame`): DataFrame containing all empty orders.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `above_50k`
*   **Signature:** `def above_50k(df: pandas.DataFrame)`
*   **Description:** The `above_50k` function processes a pandas DataFrame to identify entries that represent potentially suspicious financial positions. It filters the input DataFrame, `df`, to include only those rows where the 'Einigung_Netto' column has a value of 50,000 or greater. These entries are flagged as needing manual vetting due to exceeding a specified limit. After filtering, the function selects a predefined subset of columns from the suspicious data, including identifiers and financial details. The function then returns this refined DataFrame containing only the high-value, suspicious positions.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:**
    *   **suspicious_data** (`pandas.DataFrame`): Data frame containing suspiciously high positions
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `outliers_by_damage`
*   **Signature:** `def outliers_by_damage(df: pandas.DataFrame, schadenart: string | None = None, set_quantile: float = 0.99, column_choice: str = "Forderung_Netto")`
*   **Description:** This function identifies statistical outliers in a pandas DataFrame based on a specified numeric column and quantile range. It can optionally filter the DataFrame by a specific damage type. The function calculates symmetric upper and lower quantile bounds for the chosen column, grouped by 'Schadenart_Name'. It then returns a new DataFrame containing only the rows where the value in the specified column falls outside these calculated quantile bounds.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame to be evaluated
    *   **schadenart** (`string, optional`): specific damage type label to filter for, by default None
    *   **set_quantile** (`float`): desired quantile range, symmetric upper/lower bound is inferred, by default 0.99
    *   **column_choice** (`str`): numeric column containing outliers, by default 'Forderung_netto'
*   **Returns:**
    *   **df_outlier** (`pandas.DataFrame`): df containing all suspicious rows
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_zeitwert`
*   **Signature:** `def check_zeitwert(df: _pandas.DataFrame)`
*   **Description:** This function, `check_zeitwert`, evaluates a pandas DataFrame to verify a specific financial condition. It calculates the difference between 'Forderung_Netto' and 'Einigung_Netto', then compares this result against the 'Differenz_vor_Zeitwert_Netto' column. The function identifies rows where these values are not approximately equal, indicating a discrepancy. It then returns a new DataFrame containing the identifiers and the calculated 'Differenz Zeitwert' for these discrepant entries.
*   **Parameters:**
    *   **df** (`_pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set that is to be evaluated.
*   **Returns:**
    *   **result_df** (`pandas.DataFrame`): DataFrame of all error values (float) alongside the ID found in the original data frame
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `positions_per_order_over_time`
*   **Signature:** `def positions_per_order_over_time(df: pandas.DataFrame, df2: pandas.DataFrame, time_col: str = "CRMEingangszeit")`
*   **Description:** This function calculates the average number of positions per order on a monthly basis. It takes two pandas DataFrames, one for orders and one for positions, along with a time column name. The process involves counting positions per order, preparing the order data by converting the time column to a monthly period, and then merging these datasets. Finally, it aggregates the merged data by month to compute the mean, sum, and count of positions, renames the resulting columns, and calculates the percentage change in the average positions over time.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): Auftragsdaten mit Spalte 'KvaRechnung_ID' und einer Zeitspalte.
    *   **df2** (`pandas.DataFrame`): Positionsdaten mit Spalten 'KvaRechnung_ID' und 'Position_ID'.
    *   **time_col** (`str`): Name der Zeitspalte in orders_df (z.B. 'CRMEingangszeit').
*   **Returns:**
    *   **result** (`pandas.DataFrame`): DataFrame with columns: 'Zeitperiode', 'Avg_Positionen_pro_Auftrag', 'Total_Positionen', 'Anzahl_Auftraege', 'Growth_rate_%'
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is called by no other functions.

#### Function: `error_frequency_by_weekday_hour`
*   **Signature:** `def error_frequency_by_weekday_hour(df: pandas.DataFrame, time_col: str = "CRMEingangszeit", relevant_columns: list | None = None)`
*   **Description:** This function calculates the frequency of errors in a pandas DataFrame, aggregated by weekday and hour. An 'error' is defined as the presence of a NaN value in at least one of the specified relevant columns for a given row. It processes the input DataFrame by converting a time column to datetime objects, extracting the weekday and hour, and then identifying rows with errors. Finally, it groups the data by weekday and hour to count total rows and error rows, calculating an error rate, and returns a DataFrame sorted by weekday and hour.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): Auftragsdaten-DataFrame (z.B. Auftragsdaten_konvertiert), muss 'KvaRechnung_ID' und die Zeitspalte enthalten.
    *   **time_col** (`str`): Name der Zeitspalte in df, z.B. 'CRMEingangszeit'.
    *   **relevant_columns** (`list`): Liste der Spalten, die auf NaN gepr

    <output truncated>
*   **Returns:**
    *   **result** (`pandas.DataFrame`): DataFrame with columns: 'weekday' (Name des Wochentags), 'hour' (Stunde 0–23), 'total_rows' (Anzahl Aufträge in diesem Zeit-Slot), 'error_rows' (Anzahl fehlerhafter Aufträge in diesem Slot), 'error_rate' (Fehlerquote in Prozent).
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `mismatched_entries`
*   **Signature:** `def mismatched_entries(df: pandas.DataFrame, threshold: float = 0.2, process_batch_size: int = 16384, encode_batch_size: int = 128)`
*   **Description:** The `mismatched_entries` function calculates the semantic similarity between text entries in the 'Gewerk_Name' and 'Handwerker_Name' columns of a pandas DataFrame. It utilizes a Sentence Transformer model, specifically 'paraphrase-multilingual-MiniLM-L12-v2', to generate embeddings for unique names, leveraging GPU acceleration if available. The function then computes cosine similarity scores in batches for each row. Finally, it identifies and returns a new DataFrame containing only those entries where the calculated similarity score falls below a specified threshold, sorted by similarity.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame (Auftragsdaten) that contains the columns 'Gewerk_Name' and 'Handwerker_Name'.
    *   **threshold** (`float`): Similarity threshold (default: 0.2). Values below this limit are considered mismatches. The optimal threshold in a production system would need to be evaluated further.
    *   **process_batch_size** (`int`): Number of rows to be compared simultaneously (high value possible, e.g. 16384).
    *   **encode_batch_size** (`int`): Number of unique terms to be vectorized simultaneously by the model (low value recommended, e.g. 128).
*   **Returns:**
    *   **mismatches** (`pandas.DataFrame`): DataFrame containing rows where 'Similarity_Score' < threshold. The results are sorted ascending by similarity and include the new column 'Similarity_Score'.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not called by any other functions.

#### Function: `handwerker_gewerke_outlier`
*   **Signature:** `def handwerker_gewerke_outlier(df: pandas.DataFrame)`
*   **Description:** This function analyzes a pandas DataFrame to identify 'outlier' trade entries for companies. It filters the input DataFrame to include only 'Handwerker_Name' and 'Gewerk_Name', then calculates the frequency of each unique company-trade combination. It also determines the total number of trade observations per company and computes a ratio of individual trade count to total company trade count. Finally, it flags a company-trade entry as an 'is_outlier' if the company is associated with more than one trade and the specific trade's ratio is less than 0.2. The function returns a new DataFrame containing these calculated statistics.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): 'Auftragsdaten'-DataFrame
*   **Returns:**
    *   **stats** (`pandas.DataFrame`): DataFrame containing 'Handwerker_Name' (company name), 'Gerwerk_Name' (associated trades), 'count' (amount of observed instances of trade-company combination), 'total_count' (total amount of observations per company), 'ratio' (count/total_count per company), 'anzahl_gewerke' (absolute amount of trades per company), and 'is_outlier' (True for more than 1 trade and ratio < 0.2).
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `check_keywords`
*   **Signature:** `def check_keywords(df: pandas.DataFrame)`
*   **Description:** This function assesses the validity of a company-trade combination by examining the company name for keywords related to the assigned trade. It iterates through a predefined mapping of trades to associated keywords. For each company name, it checks if any keywords for a given trade are present. Based on this, it determines if the company name confirms the assigned trade, conflicts with another trade, or if no relevant keyword information is found. The function returns an array indicating the outcome for each entry in the input DataFrame.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing orders, specifically company and trade information.
*   **Returns:**
    *   **final_result** (`numpy.ndarray`): An array with the same length as the input DataFrame, where each element is a string indicating the keyword check result: 'CONFIRMED_BY_NAME' if the trade coheres with the company name, 'CONFLICT_WITH_<TRADE>' if the company name suggests a different trade, or 'NO_KEYWORD_INFO' if no relevant keywords are found.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `abgleich_auftraege`
*   **Signature:** `def abgleich_auftraege(df1: pd.DataFrame, df2: pd.DataFrame)`
*   **Description:** This function compares order header data (df1) with the aggregated sum of their line items (df2) to identify discrepancies. It groups the line item data by 'KvaRechnung_ID' and calculates the sum of 'Forderung_Netto' and 'Einigung_Netto' for each group. These aggregated sums are then merged with the order header data. The function calculates the differences between the 'soll' (target) values from df1 and the 'ist' (actual) summed values from df2, handling potential missing 'ist' values by filling them with zero. It then identifies and returns a DataFrame containing only the orders where these calculated differences are significant, accounting for floating-point inaccuracies.
*   **Parameters:**
    *   **df1** (`pd.DataFrame`): Dataframe mit den Auftragsdaten (Soll-Werte). Muss zwingend folgende Spalten enthalten: 'Kva_RechnungID', 'Forderung_Netto', 'Einigung_Netto'.
    *   **df2** (`pd.DataFrame`): Dataframe mit den Positionsdaten (Ist-Werte). Muss zwingend folgende Spalten enthalten: 'Kva_RechnungID', 'Forderung_Netto', 'Einigung_Netto'.
*   **Returns:**
    *   **result_df** (`pd.DataFrame`): Eine Liste der Abweichungen. Der Dataframe enthält nur die IDs, bei denen die Werte nicht übereinstimmen. Enthaltene Spalten: 'KvaRechnung_ID', 'Diff_Forderung', 'Diff_Einigung', 'CRMEingangszeit'. Ist die Differenz positiv, ist der Wert im Auftrag höher als die Summe der Positionen.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `false_negative_df1`
*   **Signature:** `def false_negative_df1(df: pandas.DataFrame)`
*   **Description:** This function calculates detailed statistics and identifies specific error instances related to singular sign errors within the 'Einigung_Netto', 'Empfehlung_Netto', and 'Forderung_Netto' columns of an input pandas DataFrame. It first creates boolean masks to identify negative values in each of these columns. Subsequently, it generates error masks for cases where only one of these columns has a sign different from the other two, indicating a singular sign error. The function then aggregates these error counts into a summary DataFrame and extracts the rows corresponding to these errors into a detailed DataFrame. It is explicitly noted that this function cannot accurately detect multiple combined errors.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set that is to be evaluated.
*   **Returns:**
    *   **stats_df** (`pandas.DataFrame`): Small DataFrame containing error counts per column (Einigung, Empfehlung, Forderung) for visualization.
    *   **details_df** (`pandas.DataFrame`): DataFrame containing the error instances.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `false_negative_df2`
*   **Signature:** `def false_negative_df2(df2: pandas.DataFrame)`
*   **Description:** The function `false_negative_df2` performs detailed consistency and plausibility checks on a given pandas DataFrame, `df2`. It specifically identifies rows where 'Menge' or 'Menge_Einigung' are negative, or where there is a sign mismatch between 'EP' and 'EP_Einigung', or 'Forderung_Netto' and 'Einigung_Netto'. The function dynamically checks for the existence of these columns and ignores missing ones. It returns two DataFrames: one summarizing the count of each error category, and another containing the specific rows from the input DataFrame that exhibit any of these identified inconsistencies, including relevant columns for debugging.
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): Der DataFrame mit den Positionsdaten, der überprüft werden soll. Erwartet idealerweise Spalten wie 'Menge', 'EP', 'Forderung_Netto', etc. Fehlende Spalten werden ignoriert (führen nicht zum Absturz).
*   **Returns:**
    *   **stats_df** (`pandas.DataFrame`): Eine Tabelle mit zwei Spalten: 'Kategorie' (Art des Fehlers) und 'Anzahl' (Häufigkeit). Bleibt leer, wenn keine Fehler gefunden wurden.
    *   **details_df** (`pandas.DataFrame`): Ein Auszug aus df2, der nur die Zeilen enthält, in denen mindestens ein Fehler gefunden wurde. Enthält nur relevante Spalten ('Position_ID', 'Menge', 'EP', Beträge, etc.). Falls 'Position_ID' fehlt, wird der DataFrame-Index als ID verwendet.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

#### Function: `discount_details`
*   **Signature:** `def discount_details(df2: pandas.DataFrame)`
*   **Description:** This function processes a pandas DataFrame to identify and analyze discount logic errors based on a 'Plausibel' column. It first checks for the existence of the 'Plausibel' column, returning empty DataFrames if it's absent. Otherwise, it creates a mask for rows where 'Plausibel' is false, indicating an error. It then generates a summary DataFrame ('stats_df') with counts of the most frequent descriptions ('Bezeichnung') among these invalid entries, limited to the top 15. Finally, it creates a detailed DataFrame ('details_df') containing specific columns from the invalid rows.
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): DataFrame containing 'Positionsdaten' data set that is to be evaluated.
*   **Returns:**
    *   **stats_df** (`pandas.DataFrame`): DataFrame with counts of the most frequent descriptions (Bezeichnung) among invalid entries.
    *   **details_df** (`pandas.DataFrame`): DataFrame containing specific invalid rows.
*   **Usage:**
    *   **Calls:** This function calls no other functions.
    *   **Called By:** This function is not explicitly called by any other functions in the provided context.

---