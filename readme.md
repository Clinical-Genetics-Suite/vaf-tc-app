# VAF-TC Relationship Visualizer 🧬

## Overview
[cite_start]The **VAF-TC Relationship Visualizer** is an interactive clinical tool designed to assist in the interpretation of genetic variants by modeling the mathematical relationship between **Pathological Tumor Content (TC)** and **Variant Allele Fraction (VAF)**[cite: 10, 22]. 

[cite_start]This tool is uniquely effective for interpreting hypermutated cases, including **MMRd** and **POLEm** tumors, providing high clinical novelty in the analysis of TMB-high cases[cite: 4, 6].

## 🚀 Live Application
Access the interactive web tool here:
**[https://vaf-tc-app.streamlit.app/](https://vaf-tc-app.streamlit.app/)**

## 📂 Data Resources & Offline Analysis
[cite_start]To support users processing multiple variants in a single case or those preferring offline documentation, the following resources are available in this repository[cite: 1, 8, 9]:
- [cite_start]**[VAF_TC_theoretical_model.xlsx](./VAF_TC_theoretical_model.xlsx):** Excel format for batch processing and paper-based records[cite: 8].
- [cite_start]**[VAF_TC_theoretical_model.csv](./VAF_TC_theoretical_model.csv):** Raw data for computational analysis.
- **[data_dictionary.txt](./data_dictionary.txt):** Descriptions of theoretical models and data columns.

## Key Features
* [cite_start]**Automated Interpretation:** Dynamically identifies theoretical models within a **±10% measurement error threshold**, acknowledging variance common in clinical NGS data[cite: 8, 20].
* [cite_start]**Convergence Zone Alert:** A warning system for samples where germline LOH and somatic LOH curves converge (typically TC 60–75%)[cite: 11, 16].
* [cite_start]**Pathological Reliability:** Designed for use with **Pathological TC (%)** to ensure accuracy over NGS-based estimations[cite: 22].

## Clinical Significance
Accurate identification of **Biallelic inactivation (LOH)** is therapeutically significant. [cite_start]Regardless of whether the initial variant is germline or somatic in origin, LOH is a critical indicator for sensitivity to **PARP inhibitors**[cite: 18, 27]. [cite_start]High-VAF variants in high-TC samples (TC ≥ 90%) are statistically more likely to represent **Germline LOH**[cite: 23, 24].

---
© 2026 Clinical-Genetics-Suite
