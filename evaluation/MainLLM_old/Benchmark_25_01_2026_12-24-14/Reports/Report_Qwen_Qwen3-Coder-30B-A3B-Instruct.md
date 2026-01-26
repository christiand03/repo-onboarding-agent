# Project Documentation: analytics-application-development-uni documentation

## 1. Project Overview
    - **Description:** This project is a comprehensive data analytics application designed for monitoring and evaluating data quality within business datasets. It provides a Streamlit-based dashboard that visualizes various data quality metrics including KPIs, error frequencies, plausibility checks, and drift analysis. The application leverages DuckDB for efficient data storage and processing, and integrates with Evidently AI for advanced data drift evaluation. It supports both raw data processing and precomputed database approaches for scalability.
    - **Key Features:** 
      - Real-time dashboard for data quality monitoring
      - Multi-page visualization with KPIs, charts, and detailed tables
      - Comprehensive data validation and plausibility checks
      - Statistical outlier detection for text and numeric data
      - Time-series trend analysis for various metrics
      - Data drift analysis using Evidently AI
      - Export capabilities for detailed findings
    - **Tech Stack:** Streamlit, Pandas, DuckDB, Evidently AI, Altair, Sentence Transformers, PyTorch

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
        Notizen --> Analytics Application Development.md
        Notizen --> Dokumentation AAD.md
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
    1. Install required packages: `pip install -r requirements.txt`
    2. Ensure the necessary data files (`.parquet` and `.duckdb`) are present in the `resources` directory
    3. Run the dashboard: `streamlit run dashboard.py` or `streamlit run db_dashboard.py`

    ### Quick Startup
    - Run `streamlit run dashboard.py` to start the main dashboard
    - Access via browser at `http://localhost:8501`
    - For database-backed version: `streamlit run db_dashboard.py`

    ## 3. Use Cases & Commands
    This analytics application serves several critical data quality and validation use cases:
    
    - **Data Quality Monitoring**: Provides real-time KPIs and visualizations of data completeness, consistency, and validity across both order and position datasets.
    - **Plausibility Checking**: Detects logical inconsistencies such as Forderung_Netto < Einigung_Netto, invalid discount logic, and incorrect sign patterns in financial data.
    - **Outlier Detection**: Identifies statistical outliers in text data (handwerker-gewerk combinations) and numeric data (position counts, invoice amounts).
    - **Time Series Analysis**: Visualizes trends in data quality metrics over time, helping track improvements or degradation.
    - **Data Drift Evaluation**: Uses Evidently AI to compare data distributions between different time periods and identify significant shifts.
    - **Error Frequency Analysis**: Shows when and how often data errors occur based on weekday and hour patterns.
    - **Test Data Identification**: Flags records that appear to be test data based on naming conventions in the 'Kundengruppe' field.
    
    Key commands:
    - `streamlit run dashboard.py` - Launch the interactive dashboard
    - `streamlit run db_dashboard.py` - Launch the database-backed dashboard
    - The application automatically processes data from `resources` directory
    - Report generation for data drift analysis uses specified date ranges

    ## 4. Architecture
    The application features a modular architecture with distinct layers:
    
    1. **Data Ingestion Layer**:
       - Raw data loading from `.parquet` files
       - Data cleaning and transformation via `data_cleaning.py`
       - DuckDB database creation via `build_db.py`
    
    2. **Core Processing Layer**:
       - Metrics computation in `metrics.py`
       - Data quality checks and validations
       - Statistical analysis and outlier detection
    
    3. **Dashboard Layer**:
       - Main dashboard in `dashboard.py`
       - Database-backed version in `db_dashboard.py`
       - Page-specific components in `app_pages/`
    
    4. **Visualization Layer**:
       - Streamlit UI components for interactivity
       - Altair charts for data visualization
       - Data tables with export capabilities
    
    5. **External Integration**:
       - Evidently AI for data drift analysis
       - Sentence Transformers for semantic similarity checks
       - DuckDB for fast data querying and caching
    
    The system employs a two-tier approach:
    - Direct data processing mode (using raw parquet files)
    - Database-backed mode (using precomputed DuckDB database)
    
    Both modes share common core logic while offering different performance characteristics and data access patterns.

    ## 5. Code Analysis

### File: `app_pages/page1.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1, metrics_df2, metrics_combined, pot_df, comparison_df, issues_df)`
*   **Description:** Renders the first page of the dashboard, displaying KPIs, null value charts, and error frequency heatmaps.
*   **Parameters:** 
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **metrics_combined** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order and position data
    *   **pot_df** (`pandas.DataFrame`): DataFrame containing position data over time
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** 
    *   **void**

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to get delta from comparison_df
*   **Parameters:** 
    *   **metric_name** (`string`): The name of the metric to retrieve delta for
*   **Returns:** 
    *   **string**: Formatted percentage change value or None

---

### File: `app_pages/page2.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1, metrics_df2, metrics_combined, comparison_df, issues_df)`
*   **Description:** Renders page 2 of 5 of the dashboard. Page 2 visualizes metrics concerning the data quality of numeric column data.
*   **Parameters:** 
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **metrics_combined** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order and position data
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** 
    *   **void**

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to get delta from comparison_df
*   **Parameters:** 
    *   **metric_name** (`string`): The name of the metric to retrieve delta for
*   **Returns:** 
    *   **string**: Formatted percentage change value or None

#### Function: `prepare_trend_data`
*   **Signature:** `def prepare_trend_data(df, label, time_col)`
*   **Description:** Helper function grouping values of passed df into monthly intervals.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame containing computed metric values over time.
    *   **label** (`string`): Label for aggregated data, written to column 'Kategorie' of the returned df
    *   **time_col** (`string`): Label of the timestamp column in df, by default "CRMEingangszeit"
*   **Returns:** 
    *   **pandas.DataFrame**: df with metric values aggregated by month. Has a column 'Kategorie' for labels. This returns an empty df if no timestamp was passed.

---

### File: `app_pages/page3.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1, metrics_df2, comparison_df, issues_df)`
*   **Description:** Renders page 3 of 5 of the dashboard. Page 3 visualizes metrics concerning the data quality of textual column data.
*   **Parameters:** 
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **metrics_combined** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order and position data
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** 
    *   **void**

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to get delta from comparison_df
*   **Parameters:** 
    *   **metric_name** (`string`): The name of the metric to retrieve delta for
*   **Returns:** 
    *   **string**: Formatted percentage change value or None

#### Function: `prepare_trend_data`
*   **Signature:** `def prepare_trend_data(df, label, time_col)`
*   **Description:** Bereitet DataFrame für das Zeitreihendiagramm (Aggregation) vor.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame containing computed metric values over time.
    *   **label** (`string`): Label for aggregated data, written to column 'Kategorie' of the returned df
    *   **time_col** (`string`): Label of the timestamp column in df, by default "CRMEingangszeit"
*   **Returns:** 
    *   **pandas.DataFrame**: df with metric values aggregated by month. Has a column 'Kategorie' for labels. This returns an empty df if no timestamp was passed.

---

### File: `app_pages/page4.py`

#### Function: `show_page`
*   **Signature:** `def show_page(metrics_df1, metrics_df2, comparison_df, issues_df)`
*   **Description:** 
*   **Parameters:** 
    *   **metrics_df1** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order data only
    *   **metrics_df2** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning position data only
    *   **metrics_combined** (`pandas.DataFrame`): DataFrame containing values for all metrics concerning order and position data
    *   **comparison_df** (`pandas.DataFrame`): DataFrame with metric value changes over time
    *   **issues_df** (`bool`): DataFrame containing values for all metrics concerning potentially invalid data points
*   **Returns:** 
    *   **void**

#### Function: `get_delta`
*   **Signature:** `def get_delta(metric_name)`
*   **Description:** Helper function to get delta from comparison_df
*   **Parameters:** 
    *   **metric_name** (`string`): The name of the metric to retrieve delta for
*   **Returns:** 
    *   **string**: Formatted percentage change value or None

---

### File: `app_pages/page5.py`

#### Function: `load_df`
*   **Signature:** `def load_df(df_type)`
*   **Description:** 
*   **Parameters:** 
    *   **df_type** (`string`): Type of dataframe to load ('df' for orders, 'df2' for positions)
*   **Returns:** 
    *   **pandas.DataFrame**: Loaded dataframe

#### Function: `fetch_reports_table`
*   **Signature:** `def fetch_reports_table()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame of available reports

#### Function: `refresh_table`
*   **Signature:** `def refresh_table()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **void**

#### Function: `show_page`
*   **Signature:** `def show_page()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **void**

---

### File: `build_db.py`

#### Function: `calc_percent`
*   **Signature:** `def calc_percent(row)`
*   **Description:** 
*   **Parameters:** 
    *   **row** (`pandas.Series`): Row of data containing Old_Value, Current_Value, and Absolute_Change
*   **Returns:** 
    *   **float**: Calculated percentage change

---

### File: `dashboard.py`

#### Function: `load`
*   **Signature:** `def load()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **tuple**: Tuple of loaded dataframes (df, df2)

#### Function: `compute_metrics_df1`
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **dict**: Dictionary of computed metrics for df1

#### Function: `compute_metrics_df2`
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** Teure Metriken für df2 (Positionsdaten) – gecached.
*   **Parameters:** 
*   **Returns:** 
    *   **dict**: Dictionary of computed metrics for df2

#### Function: `compute_metrics_combined`
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** Metriken, die beide DataFrames brauchen – gecached.
*   **Parameters:** 
*   **Returns:** 
    *   **dict**: Dictionary of combined metrics

#### Function: `compute_positions_over_time`
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** Positionsanzahl pro Auftrag über Zeit – gecached.
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with positions over time data

#### Function: `compute_issues_df`
*   **Signature:** `def compute_issues_df()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with computed issues data

#### Function: `compute_comparison_metrics`
*   **Signature:** `def compute_comparison_metrics()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with comparison metrics

---

### File: `data_cleaning.py`

#### Function: `load_data`
*   **Signature:** `def load_data()`
*   **Description:** This function loads the raw data from the programs 'resources' folder. Three .parquet files are expected: 'Auftragsdaten', 'Positionsdaten' and 'Auftragsdaten_Zeit'.
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: Auftragsdaten
    *   **pandas.DataFrame**: Positionsdaten
    *   **pandas.DataFrame**: Auftragsdaten_Zeit

#### Function: `data_cleaning`
*   **Signature:** `def data_cleaning(df, df2, df3)`
*   **Description:** This function merges the given raw data sets with appropriate timestamp data and adds columns for more expedient metric computation.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set
    *   **df2** (`pandas.DataFrame`): DataFrame containing 'Positionsdaten' data set_
    *   **df3** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten_Zeit' data set
*   **Returns:** 
    *   **pandas.DataFrame**: cleaned Auftrags- and Positionsdaten sets with timestamp information added

---

### File: `data_drift_metrics.py`

#### Function: `check_start_end_date`
*   **Signature:** `def check_start_end_date(start, end)`
*   **Description:** Helper function. Checks if end follows start chronologically and reorders the two if needed.
*   **Parameters:** 
    *   **start** (`datetime`): The assumed beginning of the interval.
    *   **end** (`datetime`): The assumed end of the interval.
*   **Returns:** 
    *   **tuple**: Pair of chronologically sorted datetime values.

#### Function: `datetime_slice_mask`
*   **Signature:** `def datetime_slice_mask(df, start_date, end_date)`
*   **Description:** Helper function. Returns a chronologically sliced Dataset according to passed datetime.
*   **Parameters:** 
    *   **df** (`pandas.Dataframe`): input df
    *   **start_date** (`date`): 
    *   **end_date** (`date`): 
*   **Returns:** 
    *   **evidently.Dataset**: sliced DataFrame, converted to Dataset.

#### Function: `data_drift_evaluation`
*   **Signature:** `def data_drift_evaluation(df, start_date_reference, end_date_reference, start_date_eval, end_date_eval)`
*   **Description:** Uses the standard preset in the evidentlyai framework to evaluate data drift between two samples (chosen by time interval) from the passed DataFrame. The resulting Snapshot object is saved as html for easy embedding.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame to sample from
    *   **start_date_reference** (`datetime`): starting datetime of the reference, baseline dataset
    *   **end_date_reference** (`datetime`): ending datetime of the reference, baseline dataset
    *   **start_date_eval** (`datetime`): starting datetime of the evaluated dataset 
    *   **end_date_eval** (`datetime`): starting datetime of the evaluated dataset
*   **Returns:** 
    *   **void**

---

### File: `data_exploration.py`

#### Function: `load`
*   **Signature:** `def load()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **tuple**: Tuple of loaded dataframes (df, df2)

---

### File: `db_dashboard.py`

#### Function: `get_db_connection`
*   **Signature:** `def get_db_connection()`
*   **Description:** Establishes a read-only connection to the DuckDB database.
*   **Parameters:** 
*   **Returns:** 
    *   **duckdb.Connection**: DuckDB connection object

#### Function: `compute_metrics_df1`
*   **Signature:** `def compute_metrics_df1()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **dict**: Dictionary of computed metrics for df1

#### Function: `compute_metrics_df2`
*   **Signature:** `def compute_metrics_df2()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **dict**: Dictionary of computed metrics for df2

#### Function: `compute_metrics_combined`
*   **Signature:** `def compute_metrics_combined()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **dict**: Dictionary of combined metrics

#### Function: `compute_positions_over_time`
*   **Signature:** `def compute_positions_over_time()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with positions over time data

#### Function: `compute_comparison_metrics`
*   **Signature:** `def compute_comparison_metrics()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with comparison metrics

#### Function: `compute_issues_df`
*   **Signature:** `def compute_issues_df()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with computed issues data

---

### File: `metrics.py`

#### Function: `load_data`
*   **Signature:** `def load_data()`
*   **Description:** 
*   **Parameters:** 
*   **Returns:** 
    *   **tuple**: Tuple of loaded dataframes (df, df2)

#### Function: `ratio_null_values_column`
*   **Signature:** `def ratio_null_values_column(input_df)`
*   **Description:** Helper function that calculates the null-value-ratios (in percent) for each column of the supplied DataFrame.
*   **Parameters:** 
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:** 
    *   **pd.DataFrame**: DataFrame of the form |column_name |  null_ratio (float)| with null_ratio being the percentage amount of null entries in the column

#### Function: `ratio_null_values_rows`
*   **Signature:** `def ratio_null_values_rows(input_df, exclude_cols)`
*   **Description:** Helper function that calculates the ratio of rows containing null values in all columns to total number of rows.
*   **Parameters:** 
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
    *   **exclude_columns** (`list`): List of column identifiers; these columns will be pruned from calculations, by default None.
*   **Returns:** 
    *   **float**: Percentage value of rows with at least one null value in the given columns.

#### Function: `Kundengruppe_containing_test`
*   **Signature:** `def Kundengruppe_containing_test(df, return_frame)`
*   **Description:** Determines the number of rows in the 'Auftragsdaten' data set that are suspected to be part of a test data set. Optionally returns a data frame with all relevant instances. A row is conidered test data if the entry in 'Kundengruppe' is named accordingly.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): 'Auftragsdaten'-DataFrame that is to be evaluated.
    *   **return_frame** (`bool`): If True, this function returns exclusively a DataFrame with all found test data, by default False
*   **Returns:** 
    *   **int**: total number of test data rows.
    *   **pandas.DataFrame or None**: DataFrame containing all found test data, returned only if return_frame = True

#### Function: `plausibilitaetscheck_forderung_einigung`
*   **Signature:** `def plausibilitaetscheck_forderung_einigung(input_df)`
*   **Description:** Checks for diff between Einigung_Netto and Forderung_Netto for all rows in the given dataframe. Cases with Einigung > Forderung are cosidered faulty.
*   **Parameters:** 
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:** 
    *   **pandas.DataFrame**: a DataFrame of all differences > 0 as float values alongside their ID, Forderung_Netto and Einigung_Netto 
    *   **int**: total number of rows with difference >0
    *   **float**: average difference over all found instances

#### Function: `uniqueness_check`
*   **Signature:** `def uniqueness_check(df, df2)`
*   **Description:** Checks whether the assumed unique ID columns in the data sets are truly unique.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame that contains the 'Auftragsdaten' data set
    *   **df2** (`pandas.DataFrame`): DataFrame that contains the 'Positionsdaten' data set
*   **Returns:** 
    *   **bool**: True if column is unique.
    *   **bool**: True if column is unique.

#### Function: `count_rows`
*   **Signature:** `def count_rows(input_df)`
*   **Description:** Helper function to calculate the number of rows in a data frame after filtering.
*   **Parameters:** 
    *   **input_df** (`pandas.DataFrame`): DataFrame to be evaluated.
*   **Returns:** 
    *   **int**: 

#### Function: `data_cleanliness`
*   **Signature:** `def data_cleanliness(input_df, group_by_col, specific_group)`
*   **Description:** Determines ratio of null-values by columns and percentage of rows containing any amount of null values, with optional grouping by a given column. Also supports filtering down to ratio for a single group of interest.
*   **Parameters:** 
    *   **input_df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
    *   **group_by_col** (`string`): Column identifier for grouping, default = 'Kundengruppe'
    *   **specific_group** (`string`): Passes a group entry to filter the result by, if any. Default = None   
*   **Returns:** 
    *   **float or None**: Percentage value of rows with at least one null value in the given columns.
    *   **DataFrame or None**: DataFrame, with null_ratio being the percentage amount of null entries in the column.   
    *   **pandas.Series or None**: Series containing the row ratios of all groups as float.
    *   **pandas.DataFrame or None**: DataFrame containing groups and null-value-ratios per column for each.

#### Function: `discount_check`
*   **Signature:** `def discount_check(df2)`
*   **Description:** Checks if a row in the 'Positionsdaten' data set does/doesn't describe a discount or similar and if the 'Einigung_Netto' and 'Forderung_Netto' information accurately reflects this (negative or positive values). References values in the 'Plausibel' column, which is calculated during database creation (see build_db.py).
*   **Parameters:** 
    *   **df2** (`pandas.DataFrame`): DataFrame containing the 'Positionsdaten' data set
*   **Returns:** 
    *   **int**: The number of potentially faulty rows

#### Function: `proformabelege`
*   **Signature:** `def proformabelege(df)`
*   **Description:** Function that checks for pro-forma receipts in the 'Auftragsdaten' data set.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame containing all found pro-forma receipt rows
    *   **int**: Amount of found receipts

#### Function: `position_count`
*   **Signature:** `def position_count(input_df)`
*   **Description:** Counts the number of positions for each unique KvaRechnung_ID
*   **Parameters:** 
    *   **input_df** (`input_df : pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with the columns 'KvaRechnung_ID' and the amount of associated positions.

#### Function: `empty_orders`
*   **Signature:** `def empty_orders(df)`
*   **Description:** Function that checks if any orders do not have positions associated with them.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame with 'Auftragsdaten' data set that is to be evaluated.
*   **Returns:** 
    *   **int**: Total amount of orders that do not have any positions associated with them.
    *   **pandas.DateFrame**: DataFrame containing all empty orders.

#### Function: `above_50k`
*   **Signature:** `def above_50k(df)`
*   **Description:** Checks for all receipts or positions that exceed a limit for suspicion of €50k in Einigung_Netto and need to be manually vetted.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame that is to be evaluated.
*   **Returns:** 
    *   **pandas.DataFrame**: Data frame containing suspiciously high positions

#### Function: `outliers_by_damage`
*   **Signature:** `def outliers_by_damage(df, schadenart, set_quantile, column_choice)`
*   **Description:** Calculates the upper and lower outliers outside the desired quantile range (symmetric over mean) for each kind of damage. Assumes 'Forderung_Netto' as column of interest.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame to be evaluated
    *   **schadenart** (`string`): specific damage type label to filter for, by default None
    *   **set_quantile** (`float`): desired quantile range, symmetric upper/lower bound is inferred, by default 0.99
    *   **column_choice** (`str`): numeric column containing outliers, by default 'Forderung_netto'
*   **Returns:** 
    *   **pandas.DataFrame**: df containing all suspicious rows

#### Function: `check_zeitwert`
*   **Signature:** `def check_zeitwert(df)`
*   **Description:** Checks if the value in the column 'Differenz_vor_Zeitwert_Netto' satisfies the condition [Zeitwert = Forderung-Einigung] and calculates the relative error. Only valid for 'Auftragsdaten' data set.
*   **Parameters:** 
    *   **df** (`_pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set that is to be evaluated.
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame of all error values (float) alongside the ID found in the original data frame

#### Function: `positions_per_order_over_time`
*   **Signature:** `def positions_per_order_over_time(df, df2, time_col)`
*   **Description:** Berechnet die durchschnittliche Anzahl an Positionen pro Auftrag je Monat.
*   **Parameters:** 
    *   **df**: Auftragsdaten mit Spalte 'KvaRechnung_ID' und einer Zeitspalte.
    *   **df2**: Positionsdaten mit Spalten 'KvaRechnung_ID' und 'Position_ID'.
    *   **time_col**: Name der Zeitspalte in orders_df (z.B. 'CRMEingangszeit').
*   **Returns:** 
    *   **DataFrame**: mit Spalten:
        *   'Zeitperiode'
        *   'Avg_Positionen_pro_Auftrag'
        *   'Total_Positionen'
        *   'Anzahl_Auftraege'
        *   'Growth_rate_%'

#### Function: `error_frequency_by_weekday_hour`
*   **Signature:** `def error_frequency_by_weekday_hour(df, time_col, relevant_columns)`
*   **Description:** Aggregiert die Fehlerhäufigkeit (NaN-Werte) nach Wochentag und Stunde. Ein Auftrag gilt als fehlerhaft, wenn in mindestens einer der relevanten Spalten ein NaN-Wert vorkommt.
*   **Parameters:** 
    *   **df**: pandas.DataFrame Auftragsdaten-DataFrame (z.B. Auftragsdaten_konvertiert),muss 'KvaRechnung_ID' und die Zeitspalte enthalten.
    *   **time_col**: string Name der Zeitspalte in df, z.B. 'CRMEingangszeit'.
    *   **relevant_columns**: list Liste der Spalten, die auf NaN geprüft werden sollen. Wenn None -> alle Spalten außer 'KvaRechnung_ID' und time_col.
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame mit Spalten:
        *   'weekday': Name des Wochentags (Monday, Tuesday, ...)
        *   'hour': Stunde (0–23)
        *   'total_rows': Anzahl Aufträge in diesem Zeit-Slot
        *   'error_rows': Anzahl fehlerhafter Aufträge in diesem Slot
        *   'error_rate': Fehlerquote in Prozent

#### Function: `mismatched_entries`
*   **Signature:** `def mismatched_entries(df, threshold, process_batch_size, encode_batch_size)`
*   **Description:** Calculates the semantic similarity between 'Gewerk_Name' and 'Handwerker_Name' using a Sentence Transformer model on the GPU. Identifies entries where the similarity score falls below the threshold.(< 0.2).
*   **Parameters:** 
    *   **df**: pandas.DataFrame DataFrame (Auftragsdaten) that contains the columns 'Gewerk_Name' and 'Handwerker_Name'.
    *   **threshold**: float Similarity threshold (default: 0.2). Values below this limit are considered mismatches. The optimal threshold in a production system would need to be evaluated further.
    *   **process_batch_size**: int Number of rows to be compared simultaneously (high value possible, e.g. 16384).
    *   **encode_batch_size**: int Number of unique terms to be vectorized simultaneously by the model (low value recommended, e.g. 128).
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame containing rows where 'Similarity_Score' < threshold. The results are sorted ascending by similarity and include the new column 'Similarity_Score'.

#### Function: `handwerker_gewerke_outlier`
*   **Signature:** `def handwerker_gewerke_outlier(df)`
*   **Description:** Determines which companies are on record with an unusual trade entry.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): 'Auftragsdaten'-DataFrame
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame containing:
        *   'Handwerker_Name': string, company name
        *   'Gerwerk_Name': string, associated trades
        *   'count': int, amount of observed instances of trade-company combination
        *   'total_count': int, total amount of observations (per company)
        *   'ratio': float, count/total_count (per company)
        *   'anzahl_gewerke': int, absolute amount of trades (per company)  
        *   'is_outlier': bool, True for more than 1 trade, ratio < 0.2

#### Function: `check_keywords`
*   **Signature:** `def check_keywords(df)`
*   **Description:** This metrics tries to check if an observed company-trade combination is valid by checking the company name for relation to a given trade.
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame containing orders; company and trade information
*   **Returns:** 
    *   **numpy.ndarray**: An array with length of df, with each element being one of the following strings:
        *   "CONFIRMED_BY_NAME" : trade coheres with company name
        *   "CONFLICT_WITH_<TRADE>": trade is not confirmed by company name
        *   "NO_KEYWORD_INFO": keyword n/a

#### Function: `abgleich_auftraege`
*   **Signature:** `def abgleich_auftraege(df1, df2)`
*   **Description:** Vergleicht die Kopfdaten von Aufträgen (df1) mit der Summe ihrer Positionen (df2).
*   **Parameters:** 
    *   **df1** (`pd.DataFrame`): Dataframe mit den Auftragsdaten (Soll-Werte). Muss zwingend folgende Spalten enthalten: - 'Kva_RechnungID' (Verbindungsschlüssel) - 'Forderung_Netto' - 'Einigung_Netto'
    *   **df2** (`pd.DataFrame`): Dataframe mit den Positionsdaten (Ist-Werte). Muss zwingend folgende Spalten enthalten: - 'Kva_RechnungID' (Verbindungsschlüssel) - 'Forderung_Netto' - 'Einigung_Netto'
*   **Returns:** 
    *   **pd.DataFrame**: Eine Liste der Abweichungen. Der Dataframe enthält nur die IDs, bei denen die Werte nicht übereinstimmen. Enthaltene Spalten: - 'Kva_RechnungID': ID des betroffenen Auftrags. - 'Diff_Forderung': Differenzbetrag (Wert in df1 - Summe in df2). - 'Diff_Einigung': Differenzbetrag (Wert in df1 - Summe in df2). - 'CRMEingangszeit': Zeitstempel des Auftrags Ist die Differenz positiv, ist der Wert im Auftrag höher als die Summe der Positionen.

#### Function: `false_negative_df1`
*   **Signature:** `def false_negative_df1(df)`
*   **Description:** Calculates detailed statistics and specific error instances for singular sign errors in the column tuple ('Einigung', 'Empfehlung', 'Forderung') in 'Auftragsdaten'. Can not accurately detect multiple combined errors
*   **Parameters:** 
    *   **df** (`pandas.DataFrame`): DataFrame containing 'Auftragsdaten' data set that is to be evaluated.
*   **Returns:** 
    *   **pandas.DataFrame**: Small DataFrame containing error counts per column (Einigung, Empfehlung, Forderung) for visualization.
    *   **pandas.DataFrame**: DataFrame containing the error instances.

#### Function: `false_negative_df2`
*   **Signature:** `def false_negative_df2(df2)`
*   **Description:** Führt detaillierte Konsistenzprüfungen (Plausibilität & Vorzeichen) auf dem DataFrame durch und gibt sowohl eine statistische Zusammenfassung als auch die betroffenen Zeilen zurück.
*   **Parameters:** 
    *   **df2** (`pandas.DataFrame`): Der DataFrame mit den Positionsdaten, der überprüft werden soll. Erwartet idealerweise Spalten wie 'Menge', 'EP', 'Forderung_Netto', etc. Fehlende Spalten werden ignoriert (führen nicht zum Absturz).
*   **Returns:** 
    *   **pandas.DataFrame**: Eine Tabelle mit zwei Spalten: 'Kategorie' (Art des Fehlers) und 'Anzahl' (Häufigkeit). Bleibt leer, wenn keine Fehler gefunden wurden.
    *   **pandas.DataFrame**: Ein Auszug aus df2, der nur die Zeilen enthält, in denen mindestens ein Fehler gefunden wurde. Enthält nur relevante Spalten ('Position_ID', 'Menge', 'EP', Beträge, etc.). Falls 'Position_ID' fehlt, wird der DataFrame-Index als ID verwendet.

#### Function: `discount_details`
*   **Signature:** `def discount_details(df2)`
*   **Description:** Aggregates statistics on discount logic errors and returns detailed instances based on the 'Plausibel' column.
*   **Parameters:** 
    *   **df2** (`pandas.DataFrame`): DataFrame containing 'Positionsdaten' data set that is to be evaluated.
*   **Returns:** 
    *   **pandas.DataFrame**: DataFrame with counts of the most frequent descriptions (Bezeichnung) among invalid entries.
    *   **pandas.DataFrame**: DataFrame containing specific invalid rows.