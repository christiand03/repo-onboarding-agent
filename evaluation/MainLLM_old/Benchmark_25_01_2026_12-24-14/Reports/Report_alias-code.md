# Project Documentation: analytics-application-development-uni documentation

## 1. Project Overview
    - **Description:** A comprehensive analytics dashboard application designed to monitor data quality metrics for business operations, specifically focusing on order and position data from procurement systems. The system provides visual insights, KPI dashboards, data drift analysis, and detailed error reporting across various dimensions such as numerical integrity, textual consistency, and plausibility checks.
    - **Key Features:** 
      - Real-time data quality monitoring with KPI dashboards
      - Multi-page analytical dashboard using Streamlit
      - Data drift detection using Evidently AI framework
      - Comprehensive error analysis including plausibility checks
      - Statistical outlier detection for trade-company associations
      - Detailed reporting with downloadable CSV exports
    - **Tech Stack:** Python, Streamlit, Pandas, Altair, Evidently AI, DuckDB, Sentence Transformers

*   **Repository Structure:**
    ```mermaid
    graph LR
        root
        root --> .DS_Store
        root --> .gitignore
        root --> .streamlit
        root --> Notebook.ipynb
        root --> Notizen
        root --> app_pages
        root --> assets
        root --> build_db.py
        root --> dashboard.py
        root --> data_cleaning.py
        root --> data_drift_metrics.py
        root --> data_exploration.py
        root --> data_exploration2.py
        root --> db_dashboard.py
        root --> metrics.py
        root --> readme.md
        root --> requirements.txt
        .streamlit --> config.toml
        Notizen --> Analytics_Application_Development.md
        Notizen --> Dokumentation_AAD.md
        Notizen --> Meeting_17-11-25.md
        app_pages --> __init__.py
        app_pages --> page1.py
        app_pages --> page2.py
        app_pages --> page3.py
        app_pages --> page4.py
        app_pages --> page5.py
        assets --> favicon.png
        assets --> logo.png
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

    ### Setup Guide
    1. Clone the repository
    2. Install required packages: `pip install -r requirements.txt`
    3. Ensure the required data files (Parquet files and DuckDB database) are present in the resources folder
    4. Run the main dashboard application with `streamlit run dashboard.py`

    ### Quick Startup
    To launch the dashboard, execute: `streamlit run dashboard.py`

    ## 3. Use Cases & Commands
    This application serves multiple purposes in data quality assurance:
    
    1. **Data Quality Monitoring**: The dashboard provides real-time KPIs for data completeness, consistency, and validity metrics across order and position datasets.
    
    2. **Error Detection**: It identifies various data anomalies including numerical inconsistencies, textual mismatches, and plausibility violations in business data.
    
    3. **Data Drift Analysis**: Using the Evidently AI framework, users can compare data distributions over different time periods to detect changes in data characteristics.
    
    4. **Statistical Outlier Detection**: The system identifies unusual trade-company associations and validates logical consistency in data entries.
    
    Primary command: `streamlit run dashboard.py`

    ## 4. Architecture
    The application follows a modular architecture with distinct layers for data processing, analytics, and presentation. The core components include:
    
    - Data ingestion layer (data_cleaning.py)
    - Analytics calculation module (metrics.py)
    - Dashboard interface (dashboard.py, app_pages/)
    - Database layer (build_db.py, db_dashboard.py)
    - Data drift analysis (data_drift_metrics.py)

    The application leverages DuckDB for efficient data querying and Evidently AI for comprehensive data drift evaluation. Streamlit provides the user interface for interactive dashboards across multiple analytical domains.

    ## 5. Code Analysis

### File: `app_pages/page1.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1,metrics_df2,metrics_combined,pot_df,comparison_df,issues_df)`
*   **Description:** Renders the first page of the dashboard, displaying key performance indicators and visualizations related to data completeness and error frequency. Shows metrics like row counts, null ratios, and error frequencies, along with charts for null value distribution and error frequency over time.
*   **Parameters:**
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **metrics_combined** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order and position data
    *   **pot_df** (`pandas.DataFrame`): DataFrame with positions per order over time data
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** None
*   **Usage:** Called by the main dashboard to display page 1 content

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to retrieve percentage change values from comparison data for dashboard metrics.
*   **Parameters:**
    *   **metric_name** (`str`): Name of the metric to retrieve change value for
*   **Returns:** Formatted percentage change string or None
*   **Usage:** Used internally by show_page to display trend deltas for KPIs

### File: `app_pages/page2.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1,metrics_df2,metrics_combined,comparison_df,issues_df)`
*   **Description:** Renders the second page of the dashboard, focusing on numeric data quality metrics. Displays KPIs for numerical anomalies, error counts in current values, orders exceeding 50k, and discrepancies in order valuation. Includes trend visualization for KPIs over time and tables for detailed error instances.
*   **Parameters:**
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **metrics_combined** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order and position data
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** None
*   **Usage:** Called by the main dashboard to display page 2 content

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to retrieve percentage change values from comparison data for dashboard metrics.
*   **Parameters:**
    *   **metric_name** (`str`): Name of the metric to retrieve change value for
*   **Returns:** Formatted percentage change string or None
*   **Usage:** Used internally by show_page to display trend deltas for KPIs

#### Function: `prepare_trend_data`
*   **Signature:** `def prepare_trend_data(df,label,time_col)`
*   **Description:** Helper function to group values from a dataframe into monthly intervals for trend visualization.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing computed metric values over time
    *   **label** (`str`): Label for aggregated data, written to column 'Kategorie' of the returned df
    *   **time_col** (`str`): Label of the timestamp column in df, defaults to "CRMEingangszeit"
*   **Returns:** DataFrame with metric values aggregated by month, includes a 'Kategorie' column for labels. Returns empty df if no timestamp was passed.
*   **Usage:** Used internally by show_page to prepare trend data for visualization

### File: `app_pages/page3.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1,metrics_df2,comparison_df,issues_df)`
*   **Description:** Renders the third page of the dashboard, focusing on textual data quality metrics. Displays KPIs for text-related issues, test data identification, and statistical outliers in trade-company associations. Provides trend visualizations for identified error types and detailed analysis of outliers.
*   **Parameters:**
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** None
*   **Usage:** Called by the main dashboard to display page 3 content

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to retrieve percentage change values from comparison data for dashboard metrics.
*   **Parameters:**
    *   **metric_name** (`str`): Name of the metric to retrieve change value for
*   **Returns:** Formatted percentage change string or None
*   **Usage:** Used internally by show_page to display trend deltas for KPIs

#### Function: `prepare_trend_data`
*   **Signature:** `def prepare_trend_data(df,label,time_col)`
*   **Description:** Helper function to prepare DataFrame for time series chart aggregation.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing computed metric values over time
    *   **label** (`str`): Label for aggregated data, written to column 'Kategorie' of the returned df
    *   **time_col** (`str`): Label of the timestamp column in df, defaults to "CRMEingangszeit"
*   **Returns:** DataFrame with metric values aggregated by month, includes a 'Kategorie' column for labels. Returns empty df if no timestamp was passed.
*   **Usage:** Used internally by show_page to prepare trend data for visualization

### File: `app_pages/page4.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1,metrics_df2,comparison_df,issues_df)`
*   **Description:** Renders the fourth page of the dashboard, presenting plausibility checks and logic errors within the data. Displays detailed error analysis for logic errors, discount validation, proforma receipts, and sign consistency checks for both order and position data. Provides statistical summaries and visualizations for these critical data quality issues.
*   **Parameters:**
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** None
*   **Usage:** Called by the main dashboard to display page 4 content

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to retrieve percentage change values from comparison data for dashboard metrics.
*   **Parameters:**
    *   **metric_name** (`str`): Name of the metric to retrieve change value for
*   **Returns:** Formatted percentage change string or None
*   **Usage:** Used internally by show_page to display trend deltas for KPIs

### File: `app_pages/page5.py`

#### Function: `load_df`
*   **Signature:** `def load_df(df_type)`
*   **Description:** Loads either order data or position data from a DuckDB database based on the specified type.
*   **Parameters:**
    *   **df_type** (`str`): Type of data to load, either 'df' for order data or 'df2' for position data
*   **Returns:** Loaded pandas DataFrame
*   **Usage:** Called by show_page to retrieve data for report generation

#### Function: `fetch_reports_table`
*   **Signature:** `def fetch_reports_table()`
*   **Description:** Fetches available report data from the reports directory and formats it into a readable table.
*   **Parameters:** None
*   **Returns:** Formatted pandas DataFrame with available reports
*   **Usage:** Called by show_page to display available reports in the UI

#### Function: `refresh_table`
*   **Signature:** `def refresh_table()`
*   **Description:** Refreshes the reports table stored in session state by calling fetch_reports_table.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:** Called when needed to update the displayed reports table

#### Function: `show_page`
*   **Signature:** `def show_page()`
*   **Description:** Renders the fifth page of the dashboard, providing data drift analysis capabilities. Allows users to select time ranges for comparison and displays generated reports using Evidently AI. Supports dynamic report generation when reports don't exist yet.
*   **Parameters:** None
*   **Returns:** None
*   **Usage:** Called by the main dashboard to display page 5 content

### File: `build_db.py`

#### Function: `calc_percent`
*   **Signature:** `def calc_percent(row)`
*   **Description:** Calculates percentage change between old and current values for a given data row.
*   **Parameters:**
    *   **row** (`pandas.Series`): Row from a dataframe with Old_Value, Current_Value, and Absolute_Change columns
*   **Returns:** Calculated percentage change as float
*   **Usage:** Used internally to compute percentage changes for comparison metrics

### File: `dashboard.py`

#### Function: `load`
*   **Signature:** `def load()`
*   **Description:** Loads order and position data from parquet files.
*   **Parameters:** None
*   **Returns:** Tuple of pandas DataFrames (df, df2)
*   **Usage:** Called by various compute functions to access raw data

#### Function: `compute_metrics_df1`
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** Computes comprehensive metrics for order data (df1) including plausibility checks, null value ratios, error frequencies, and outlier detection.
*   **Parameters:** None
*   **Returns:** Dictionary containing computed metrics for df1
*   **Usage:** Called by main dashboard to prepare data for display on pages 1-4

#### Function: `compute_metrics_df2`
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** Computes comprehensive metrics for position data (df2) including plausibility checks, null value ratios, discount validation, and false negative detection.
*   **Parameters:** None
*   **Returns:** Dictionary containing computed metrics for df2
*   **Usage:** Called by main dashboard to prepare data for display on pages 1-4

#### Function: `compute_metrics_combined`
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** Computes metrics that require both dataframes, including uniqueness checks and order-position discrepancy analysis.
*   **Parameters:** None
*   **Returns:** Dictionary containing combined metrics
*   **Usage:** Called by main dashboard to prepare combined data for display on pages 1-4

#### Function: `compute_positions_over_time`
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** Calculates average number of positions per order over time.
*   **Parameters:** None
*   **Returns:** DataFrame with positions per order over time data
*   **Usage:** Called by main dashboard to prepare trend data for page 1

#### Function: `compute_issues_df`
*   **Signature:** `def compute_issues_df()`
*   **Description:** Aggregates all issue types into a single dataframe for comprehensive issue tracking.
*   **Parameters:** None
*   **Returns:** DataFrame containing issue counts and summaries
*   **Usage:** Called by main dashboard to prepare issue data for display on pages 1-4

#### Function: `compute_comparison_metrics`
*   **Signature:** `def compute_comparison_metrics()`
*   **Description:** Computes comparison metrics between different time periods.
*   **Parameters:** None
*   **Returns:** DataFrame containing comparison data
*   **Usage:** Called by main dashboard to prepare comparison data for display on pages 1-4

### File: `data_cleaning.py`

#### Function: `load_data`
*   **Signature:** `def load_data()`
*   **Description:** Loads the raw data from the program's 'resources' folder. Three .parquet files are expected: 'Auftragsdaten', 'Positionsdaten' and 'Auftragsdaten_Zeit'.
*   **Parameters:** None
*   **Returns:** Tuple of pandas DataFrames (df, df2, df3)
*   **Usage:** Called by main data cleaning pipeline to load raw data

#### Function: `data_cleaning`
*   **Signature:** `def data_cleaning(df,df2,df3)`
*   **Description:** Merges the given raw data sets with appropriate timestamp data and adds columns for more expedient metric computation.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set
    *   **df2** (`pandas.DataFrame`): DataFrame containing 'Positionsdaten' data set_
    *   **df3** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten_Zeit' data set
*   **Returns:** Tuple of pandas DataFrames (cleaned df, cleaned df2)
*   **Usage:** Called by main data cleaning pipeline to transform and clean raw data

### File: `data_drift_metrics.py`

#### Function: `check_start_end_date`
*   **Signature:** `def check_start_end_date(start,end)`
*   **Description:** Helper function. Checks if end follows start chronologically and reorders the two if needed.
*   **Parameters:**
    *   **start** (`datetime`): The assumed beginning of the interval
    *   **end** (`datetime`): The assumed end of the interval
*   **Returns:** Tuple of chronologically sorted datetime values
*   **Usage:** Used internally by data_drift_evaluation to ensure proper date ordering

#### Function: `datetime_slice_mask`
*   **Signature:** `def datetime_slice_mask(df,start_date,end_date)`
*   **Description:** Helper function. Returns a chronologically sliced Dataset according to passed datetime.
*   **Parameters:**
    *   **df** (`pandas.Dataframe`): Input dataframe
    *   **start_date** (`date`): Start date for slicing
    *   **end_date** (`date`): End date for slicing
*   **Returns:** Evidently Dataset with sliced data
*   **Usage:** Used internally by data_drift_evaluation to prepare data for drift analysis

#### Function: `data_drift_evaluation`
*   **Signature:** `def data_drift_evaluation(df,start_date_reference,end_date_reference,start_date_eval,end_date_eval)`
*   **Description:** Uses the standard preset in the evidentlyai framework to evaluate data drift between two samples (chosen by time interval) from the passed DataFrame. The resulting Snapshot object is saved as html for easy embedding.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame to sample from
    *   **start_date_reference** (`datetime`): Starting datetime of the reference, baseline dataset
    *   **end_date_reference** (`datetime`): Ending datetime of the reference, baseline dataset
    *   **start_date_eval** (`datetime`): Starting datetime of the evaluated dataset
    *   **end_date_eval** (`datetime`): Starting datetime of the evaluated dataset
*   **Returns:** None
*   **Usage:** Called by page5 show_page to generate data drift reports

### File: `data_exploration.py`

#### Function: `load`
*   **Signature:** `def load()`
*   **Description:** Loads order and position data from parquet files.
*   **Parameters:** None
*   **Returns:** Tuple of pandas DataFrames (df, df2)
*   **Usage:** Called by data exploration scripts to access raw data

### File: `db_dashboard.py`

#### Function: `get_db_connection`
*   **Signature:** `def get_db_connection()`
*   **Description:** Establishes a read-only connection to the DuckDB database.
*   **Parameters:** None
*   **Returns:** DuckDB connection object
*   **Usage:** Called by compute functions to access pre-calculated metrics in the database

#### Function: `compute_metrics_df1`
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** Loads pre-computed metrics for order data from the DuckDB database.
*   **Parameters:** None
*   **Returns:** Dictionary containing loaded metrics for df1
*   **Usage:** Called by main dashboard to access pre-computed order data metrics

#### Function: `compute_metrics_df2`
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** Loads pre-computed metrics for position data from the DuckDB database.
*   **Parameters:** None
*   **Returns:** Dictionary containing loaded metrics for df2
*   **Usage:** Called by main dashboard to access pre-computed position data metrics

#### Function: `compute_metrics_combined`
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** Loads combined metrics from the DuckDB database.
*   **Parameters:** None
*   **Returns:** Dictionary containing loaded combined metrics
*   **Usage:** Called by main dashboard to access combined data metrics

#### Function: `compute_positions_over_time`
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** Loads positions per order over time data from the DuckDB database.
*   **Parameters:** None
*   **Returns:** DataFrame with positions per order over time data
*   **Usage:** Called by main dashboard to access trend data

#### Function: `compute_comparison_metrics`
*   **Signature:** `def compute_comparison_metrics()`
*   **Description:** Loads comparison metrics from the DuckDB database.
*   **Parameters:** None
*   **Returns:** DataFrame containing comparison data
*   **Usage:** Called by main dashboard to access comparison data

#### Function: `compute_issues_df`
*   **Signature:** `def compute_issues_df()`
*   **Description:** Loads issue metrics from the DuckDB database.
*   **Parameters:** None
*   **Returns:** DataFrame containing issue metrics
*   **Usage:** Called by main dashboard to access issue data

### File: `metrics.py`

#### Function: `load_data`
*   **Signature:** `def load_data()`
*   **Description:** Loads order and position data from parquet files.
*   **Parameters:** None
*   **Returns:** Tuple of pandas DataFrames (df, df2)
*   **Usage:** Called by various metric functions to access raw data

#### Function: `ratio_null_values_column`
*   **Signature:** `def ratio_null_values_column(input_df)`
*   **Description:** Helper function that calculates the null-value-ratios (in percent) for each column of the supplied DataFrame.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated
*   **Returns:** DataFrame with column names and their corresponding null ratios
*   **Usage:** Called by data cleanliness metrics to compute null value ratios

#### Function: `ratio_null_values_rows`
*   **Signature:** `def ratio_null_values_rows(input_df,exclude_cols)`
*   **Description:** Helper function that calculates the ratio of rows containing null values in all columns to total number of rows.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated
    *   **exclude_columns** (`list`): List of column identifiers; these columns will be pruned from calculations
*   **Returns:** Percentage value of rows with at least one null value in the given columns
*   **Usage:** Called by data cleanliness metrics to compute row null ratios

#### Function: `Kundengruppe_containing_test`
*   **Signature:** `def Kundengruppe_containing_test(df,return_frame)`
*   **Description:** Determines the number of rows in the 'Auftragsdaten' data set that are suspected to be part of a test data set. Optionally returns a data frame with all relevant instances. A row is considered test data if the entry in 'Kundengruppe' is named accordingly.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): 'Auftragsdaten'-DataFrame that is to be evaluated
    *   **return_frame** (`bool`): If True, this function returns exclusively a DataFrame with all found test data
*   **Returns:** Integer count of test data rows, or DataFrame if return_frame=True
*   **Usage:** Called by various data quality checks to identify test data

#### Function: `plausibilitaetscheck_forderung_einigung`
*   **Signature:** `def plausibilitaetscheck_forderung_einigung(input_df)`
*   **Description:** Checks for diff between Einigung_Netto and Forderung_Netto for all rows in the given dataframe. Cases with Einigung > Forderung are considered faulty.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated
*   **Returns:** Tuple of (results DataFrame, count integer, average float)
*   **Usage:** Called by data quality checks to detect plausibility errors

#### Function: `uniqueness_check`
*   **Signature:** `def uniqueness_check(df,df2)`
*   **Description:** Checks whether the assumed unique ID columns in the data sets are truly unique.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame that contains the 'Auftragsdaten' data set
    *   **df2** (`pandas.DataFrame`): DataFrame that contains the 'Positionsdaten' data set
*   **Returns:** Tuple of boolean values indicating uniqueness of IDs
*   **Usage:** Called by data quality checks to verify data integrity

#### Function: `count_rows`
*   **Signature:** `def count_rows(input_df)`
*   **Description:** Helper function to calculate the number of rows in a data frame after filtering.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame to be evaluated
*   **Returns:** Integer count of rows
*   **Usage:** Called by various metric functions for row counting

#### Function: `data_cleanliness`
*   **Signature:** `def data_cleanliness(input_df,group_by_col,specific_group)`
*   **Description:** Determines ratio of null-values by columns and percentage of rows containing any amount of null values, with optional grouping by a given column. Also supports filtering down to ratio for a single group of interest.
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated
    *   **group_by_col** (`str`): Column identifier for grouping
    *   **specific_group** (`str`): Passes a group entry to filter the result by, if any
*   **Returns:** Tuple of null ratio values for rows and columns, optionally grouped
*   **Usage:** Called by data quality checks to assess data cleanliness

#### Function: `discount_check`
*   **Signature:** `def discount_check(df2)`
*   **Description:** Checks if a row in the 'Positionsdaten' data set does/doesn't describe a discount or similar and if the 'Einigung_Netto' and 'Forderung_Netto' information accurately reflects this (negative or positive values). References values in the 'Plausibel' column, which is calculated during database creation.
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): DataFrame containing the 'Positionsdaten' data set
*   **Returns:** Integer count of potentially faulty rows
*   **Usage:** Called by data quality checks to validate discount logic

#### Function: `proformabelege`
*   **Signature:** `def proformabelege(df)`
*   **Description:** Function that checks for pro-forma receipts in the 'Auftragsdaten' data set.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame that is to be evaluated
*   **Returns:** Tuple of (DataFrame with pro-forma receipts, integer count)
*   **Usage:** Called by data quality checks to identify pro-forma receipts

#### Function: `position_count`
*   **Signature:** `def position_count(input_df)`
*   **Description:** Counts the number of positions for each unique KvaRechnung_ID
*   **Parameters:**
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated
*   **Returns:** DataFrame with position counts per order
*   **Usage:** Called by data quality checks to determine position counts

#### Function: `empty_orders`
*   **Signature:** `def empty_orders(df)`
*   **Description:** Function that checks if any orders do not have positions associated with them.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame with 'Auftragsdaten' data set that is to be evaluated
*   **Returns:** Tuple of (integer count, DataFrame with empty orders)
*   **Usage:** Called by data quality checks to identify orders without positions

#### Function: `above_50k`
*   **Signature:** `def above_50k(df)`
*   **Description:** Checks for all receipts or positions that exceed a limit for suspicion of €50k in Einigung_Netto and need to be manually vetted.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame that is to be evaluated
*   **Returns:** DataFrame with suspiciously high values
*   **Usage:** Called by data quality checks to flag high-value transactions

#### Function: `outliers_by_damage`
*   **Signature:** `def outliers_by_damage(df,schadenart,set_quantile,column_choice)`
*   **Description:** Calculates the upper and lower outliers outside the desired quantile range (symmetric over mean) for each kind of damage. Assumes 'Forderung_Netto' as column of interest.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame to be evaluated
    *   **schadenart** (`str`): Specific damage type label to filter for
    *   **set_quantile** (`float`): Desired quantile range
    *   **column_choice** (`str`): Numeric column containing outliers
*   **Returns:** DataFrame with outlier records
*   **Usage:** Called by data quality checks to identify outliers

#### Function: `check_zeitwert`
*   **Signature:** `def check_zeitwert(df)`
*   **Description:** Checks if the value in the column 'Differenz_vor_Zeitwert_Netto' satisfies the condition [Zeitwert = Forderung-Einigung] and calculates the relative error. Only valid for 'Auftragsdaten' data set.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set that is to be evaluated
*   **Returns:** DataFrame with error values and IDs
*   **Usage:** Called by data quality checks to validate time value calculations

#### Function: `positions_per_order_over_time`
*   **Signature:** `def positions_per_order_over_time(df,df2,time_col)`
*   **Description:** Calculates the average number of positions per order by month.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): Order data with 'KvaRechnung_ID' and time column
    *   **df2** (`pandas.DataFrame`): Position data with 'KvaRechnung_ID' and 'Position_ID'
    *   **time_col** (`str`): Name of time column in df
*   **Returns:** DataFrame with positions per order over time data
*   **Usage:** Called by data quality checks to analyze position trends

#### Function: `error_frequency_by_weekday_hour`
*   **Signature:** `def error_frequency_by_weekday_hour(df,time_col,relevant_columns)`
*   **Description:** Aggregates the error frequency (NaN values) by weekday and hour. An order is considered erroneous if at least one of the relevant columns contains a NaN value.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): Order data DataFrame
    *   **time_col** (`str`): Name of time column in df
    *   **relevant_columns** (`list`): List of columns to check for NaN values
*   **Returns:** DataFrame with error frequency data by weekday and hour
*   **Usage:** Called by data quality checks to analyze error patterns over time

#### Function: `mismatched_entries`
*   **Signature:** `def mismatched_entries(df,threshold,process_batch_size,encode_batch_size)`
*   **Description:** Calculates the semantic similarity between 'Gewerk_Name' and 'Handwerker_Name' using a Sentence Transformer model on the GPU. Identifies entries where the similarity score falls below the threshold.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame (Auftragsdaten) that contains the columns 'Gewerk_Name' and 'Handwerker_Name'
    *   **threshold** (`float`): Similarity threshold (default: 0.2)
    *   **process_batch_size** (`int`): Number of rows to be compared simultaneously
    *   **encode_batch_size** (`int`): Number of unique terms to be vectorized simultaneously
*   **Returns:** DataFrame containing rows where similarity score < threshold
*   **Usage:** Called by data quality checks to identify mismatched entries

#### Function: `handwerker_gewerke_outlier`
*   **Signature:** `def handwerker_gewerke_outlier(df)`
*   **Description:** Determines which companies are on record with an unusual trade entry.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): 'Auftragsdaten'-DataFrame
*   **Returns:** DataFrame with company-trade combinations and outlier status
*   **Usage:** Called by data quality checks to identify outlier associations

#### Function: `check_keywords`
*   **Signature:** `def check_keywords(df)`
*   **Description:** This metric tries to check if an observed company-trade combination is valid by checking the company name for relation to a given trade.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing orders; company and trade information
*   **Returns:** Array with validation results for each row
*   **Usage:** Called by data quality checks to validate company-trade combinations

#### Function: `abgleich_auftraege`
*   **Signature:** `def abgleich_auftraege(df1,df2)`
*   **Description:** Compares the head data of orders (df1) with the sum of their positions (df2).
*   **Parameters:**
    *   **df1** (`pandas.DataFrame`): DataFrame with order data (target values)
    *   **df2** (`pandas.DataFrame`): DataFrame with position data (source values)
*   **Returns:** DataFrame with IDs where values don't match
*   **Usage:** Called by data quality checks to verify order-position consistency

#### Function: `false_negative_df1`
*   **Signature:** `def false_negative_df1(df)`
*   **Description:** Calculates detailed statistics and specific error instances for singular sign errors in the column tuple ('Einigung', 'Empfehlung', 'Forderung') in 'Auftragsdaten'. Cannot accurately detect multiple combined errors.
*   **Parameters:**
    *   **df** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set that is to be evaluated
*   **Returns:** Tuple of (statistics DataFrame, details DataFrame)
*   **Usage:** Called by data quality checks to identify sign consistency errors

#### Function: `false_negative_df2`
*   **Signature:** `def false_negative_df2(df2)`
*   **Description:** Performs detailed consistency checks (plausibility & sign) on the DataFrame and returns both statistical summary and affected rows.
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): DataFrame with position data to check
*   **Returns:** Tuple of (statistics DataFrame, details DataFrame)
*   **Usage:** Called by data quality checks to identify sign consistency errors in position data

#### Function: `discount_details`
*   **Signature:** `def discount_details(df2)`
*   **Description:** Aggregates statistics on discount logic errors and returns detailed instances based on the 'Plausibel' column.
*   **Parameters:**
    *   **df2** (`pandas.DataFrame`): DataFrame containing 'Positionsdaten' data set that is to be evaluated
*   **Returns:** Tuple of (statistics DataFrame, details DataFrame)
*   **Usage:** Called by data quality checks to identify discount logic errors