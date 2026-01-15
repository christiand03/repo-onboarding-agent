# Helper LLM Analysis Report

## 1. 🔍 Error Log
*Identify mismatches between Source Code and Generated JSON.*

| Identifier | Issue Type | Input Data (Ground Truth) | LLM Output | Severity |
|---|---|---|---|---|
| `app_pages.page2.show_page` | Type Error (Parameter) | `metrics_df1: dict` | `metrics_df1: pandas.DataFrame` | Medium |
| `app_pages.page2.show_page` | Type Error (Parameter) | `metrics_df2: dict` | `metrics_df2: pandas.DataFrame` | Medium |
| `app_pages.page2.show_page` | Type Error (Parameter) | `metrics_combined: dict` | `metrics_combined: pandas.DataFrame` | Medium |
| `app_pages.page3.show_page` | Type Error (Parameter) | `metrics_df2: dict` | `metrics_df2: pandas.DataFrame` | Medium |
| `app_pages.page3.show_page` | Type Error (Parameter) | `metrics_combined: dict` | `metrics_combined: pandas.DataFrame` | Medium |
| `app_pages.page4.show_page` | Type Error (Parameter) | `metrics_combined: dict` | `metrics_combined: unknown` | Medium |
| `data_drift_metrics.check_start_end_date` | Context Error (called_by) | `called_by: ['data_drift_metrics.data_drift_evaluation']` | `called_by: "This function is not called by any other functions."` | High |
| `data_drift_metrics.datetime_slice_mask` | Context Error (called_by) | `called_by: ['data_drift_metrics.data_drift_evaluation']` | `called_by: "This function is not called by any other functions."` | High |
| `db_dashboard.get_db_connection` | Context Error (called_by) | `called_by: ['db_dashboard.load', 'db_dashboard.get_scalar_metrics', 'db_dashboard.compute_metrics_df1', 'db_dashboard.compute_metrics_df2', 'db_dashboard.compute_metrics_combined', 'db_dashboard.compute_positions_over_time']` | `called_by: "This function is not called by any other functions."` | High |
| `db_dashboard.load` | Context Error (called_by) | `called_by: ['db_dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `db_dashboard.get_scalar_metrics` | Context Error (called_by) | `called_by: ['db_dashboard.compute_metrics_df1', 'db_dashboard.compute_metrics_df2', 'db_dashboard.compute_metrics_combined']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.ratio_null_values_column` | Context Error (called_by) | `called_by: ['metrics.data_cleanliness', 'dashboard.compute_metrics_df1', 'dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.ratio_null_values_rows` | Context Error (called_by) | `called_by: ['app_pages.page1.show_page', 'metrics.data_cleanliness', 'dashboard.compute_metrics_df1', 'dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.Kundengruppe_containing_test` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.allgemeine_statistiken_num` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1', 'dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.plausibilitaetscheck_forderung_einigung` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1', 'dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.uniqueness_check` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_combined']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.count_rows` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1', 'dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.data_cleanliness` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1']` | `called_by: "This function is called by no other functions."` | High |
| `metrics.discount_check` | Context Error (called_by) | `called_by: ['app_pages.page4.show_page', 'dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.proformabelege` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.position_count` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.false_negative_df` | Context Error (called_by) | `called_by: ['app_pages.page4.show_page', 'dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.false_negative_df2` | Context Error (called_by) | `called_by: ['app_pages.page4.show_page', 'dashboard.compute_metrics_df2']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.above_50k` | Context Error (called_by) | `called_by: ['app_pages.page2.show_page', 'dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.check_zeitwert` | Context Error (called_by) | `called_by: ['app_pages.page2.show_page', 'dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.positions_per_order_over_time` | Context Error (called_by) | `called_by: ['dashboard.compute_positions_over_time']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.error_frequency_by_weekday_hour` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.handwerker_gewerke_outlier` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.check_keywords_vectorized` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_df1']` | `called_by: "This function is not called by any other functions."` | High |
| `metrics.abgleich_auftraege` | Context Error (called_by) | `called_by: ['dashboard.compute_metrics_combined']` | `called_by: "This function is not called by any other functions."` | High |

## 2. 📊 Scoring

### 🎯 Signature & Type Accuracy (Weight: 30%)
**Score: 0/10**
**Analysis:** The model made several parameter type errors. Specifically, for `app_pages.page2.show_page`, `app_pages.page3.show_page`, and `app_pages.page4.show_page`, parameters like `metrics_df1`, `metrics_df2`, and `metrics_combined` were incorrectly identified as `pandas.DataFrame` or `unknown` instead of `dict`, which is clearly implied by their usage (`.get()` method) in the source code and consistent with the naming convention. This resulted in a significant deduction.

### 🧠 Logic Description (Weight: 40%)
**Score: 10/10**
**Analysis:** The `overall` descriptions for all functions were consistently accurate, concise, and correctly summarized the purpose and main logic of the code. No significant vagueness or hallucinations were detected in this section.

### 🔗 Context Integration (Weight: 30%)
**Score: 0/10**
**Analysis:** This section represents a critical failure. While the `calls` context was generally accurate, the `called_by` context was almost entirely incorrect for functions that *were* called by other functions. For 25 out of 51 functions, the model explicitly stated, "This function is not called by any other functions," when the `context.called_by` list in the ground truth clearly indicated otherwise. This is a systemic issue in processing and synthesizing the provided `called_by` information, directly violating the instruction to "TRUST ONLY THE 'context' OBJECT IN PART 1." Each instance of this error is considered a high-severity hallucination/missing context.

---
**TOTAL SCORE: 4/100**
---