# Helper LLM Analysis Report

## 1. 🔍 Error Log
*Identify mismatches between Source Code and Generated JSON.*

| Identifier | Issue Type | Input Data (Ground Truth) | LLM Output | Severity |
|---|---|---|---|---|
| `app_pages.page2.show_page` | Parameter Type Error | `metrics_df1: dict` | `metrics_df1: pandas.DataFrame` | Medium |
| `app_pages.page2.show_page` | Parameter Type Error | `metrics_df2: dict` (inferred) | `metrics_df2: pandas.DataFrame` | Medium |
| `app_pages.page2.show_page` | Parameter Type Error | `metrics_combined: dict` | `metrics_combined: pandas.DataFrame` | Medium |
| `app_pages.page3.show_page` | Parameter Type Error | `metrics_df2: dict` (inferred) | `metrics_df2: pandas.DataFrame` | Medium |
| `app_pages.page3.show_page` | Parameter Type Error | `metrics_combined: dict` (inferred) | `metrics_combined: pandas.DataFrame` | Medium |
| `dashboard.load` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1`, `dashboard.compute_metrics_df2`, `dashboard.compute_metrics_combined`, `dashboard.compute_positions_over_time` | Not called by any other functions. | High |
| `data_drift_metrics.check_start_end_date` | Context Omission (called_by) | Called by: `data_drift_metrics.data_drift_evaluation` | Not called by any other functions. | High |
| `data_drift_metrics.datetime_slice_mask` | Context Omission (called_by) | Called by: `data_drift_metrics.data_drift_evaluation` | Not called by any other functions. | High |
| `db_dashboard.get_db_connection` | Context Omission (called_by) | Called by: `db_dashboard.load`, `db_dashboard.get_scalar_metrics`, `db_dashboard.compute_metrics_df1`, `db_dashboard.compute_metrics_df2`, `db_dashboard.compute_metrics_combined`, `db_dashboard.compute_positions_over_time` | Not called by any other functions. | High |
| `db_dashboard.load` | Context Omission (called_by) | Called by: `db_dashboard.compute_metrics_df2` | Not called by any other functions. | High |
| `db_dashboard.get_scalar_metrics` | Context Omission (called_by) | Called by: `db_dashboard.compute_metrics_df1`, `db_dashboard.compute_metrics_df2`, `db_dashboard.compute_metrics_combined` | Not called by any other functions. | High |
| `metrics.ratio_null_values_column` | Context Omission (called_by) | Called by: `metrics.data_cleanliness` | Not called by any other functions. | High |
| `metrics.ratio_null_values_rows` | Context Omission (called_by) | Called by: `app_pages.page1.show_page`, `metrics.data_cleanliness` | Not called by any other functions. | High |
| `metrics.Kundengruppe_containing_test` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.allgemeine_statistiken_num` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1`, `dashboard.compute_metrics_df2` | Not called by any other functions. | High |
| `metrics.plausibilitaetscheck_forderung_einigung` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1`, `dashboard.compute_metrics_df2` | Not called by any other functions. | High |
| `metrics.uniqueness_check` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_combined` | Not called by any other functions. | High |
| `metrics.count_rows` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1`, `dashboard.compute_metrics_df2` | Not called by any other functions. | High |
| `metrics.count_rows` | Logic Vagueness | Description mentions "after filtering" which is not implemented in the source. | "after filtering" | Low |
| `metrics.data_cleanliness` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1` | Not called by any other functions according to the provided context. | High |
| `metrics.discount_check` | Context Omission (called_by) | Called by: `app_pages.page4.show_page`, `dashboard.compute_metrics_df2` | Not called by any other functions. | High |
| `metrics.proformabelege` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.position_count` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df2` | Not called by any other functions. | High |
| `metrics.false_negative_df` | Context Omission (called_by) | Called by: `app_pages.page4.show_page`, `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.false_negative_df2` | Context Omission (called_by) | Called by: `app_pages.page4.show_page`, `dashboard.compute_metrics_df2` | Not called by any other functions. | High |
| `metrics.above_50k` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.check_zeitwert` | Context Omission (called_by) | Called by: `app_pages.page2.show_page`, `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.positions_per_order_over_time` | Context Omission (called_by) | Called by: `dashboard.compute_positions_over_time` | Not called by any other functions. | High |
| `metrics.error_frequency_by_weekday_hour` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.handwerker_gewerke_outlier` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.check_keywords_vectorized` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_df1` | Not called by any other functions. | High |
| `metrics.abgleich_auftraege` | Context Omission (called_by) | Called by: `dashboard.compute_metrics_combined` | Not called by any other functions. | High |

## 2. 📊 Scoring

### 🎯 Signature & Type Accuracy (Weight: 30%)
**Score: 0/10**
**Analysis:** The model made 5 significant parameter type errors, incorrectly identifying dictionary parameters as pandas DataFrames in `app_pages.page2.show_page` and `app_pages.page3.show_page`. Each incorrect type deduction is 2 points, leading to a total of -10 points from a starting score of 10.

### 🧠 Logic Description (Weight: 40%)
**Score: 9/10**
**Analysis:** The overall descriptions for most functions were accurate and captured the core functionality. A minor vagueness was noted in `metrics.count_rows` where the description mentioned "after filtering" which is not present in the code's implementation. This resulted in a deduction of 1 point.

### 🔗 Context Integration (Weight: 30%)
**Score: 0/10**
**Analysis:** This section shows a critical failure. The model consistently failed to correctly identify functions that are called by other functions within the provided `context` object. For 26 out of 51 functions, the `called_by` field incorrectly stated "This function is not called by any other functions." when the ground truth `context` clearly listed callers. This indicates a complete breakdown in processing the `called_by` relationships from the input, which is a severe hallucination/omission. This fundamental error warrants a score of 0.

---
**TOTAL SCORE: 36/100**
---