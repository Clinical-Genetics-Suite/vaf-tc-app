# VAF-TC Relationship Visualizer 🧬

## Overview
The **VAF-TC Relationship Visualizer** is an interactive clinical tool designed to assist in the interpretation of genetic variants by modeling the mathematical relationship between **Pathological Tumor Content (TC)** and **Variant Allele Fraction (VAF)**. 

This tool helps clinicians and researchers evaluate the likelihood of germline vs. somatic events, providing a theoretical framework based on Knudson's Two-Hit Theory and various copy number alteration models.

## 🚀 Live Application
Access the interactive web tool here:
**[https://vaf-tc-app.streamlit.app/](https://vaf-tc-app.streamlit.app/)**

## Key Features
* **Interactive Modeling:** Real-time visualization of theoretical trajectories for Germline (Heterozygous, cnLOH, LOH-Deletion) and Somatic (Heterozygous, cnLOH, LOH-Deletion) variants.
* **Measurement Tolerance:** Incorporates a **±10% VAF variance** model to account for NGS technical limitations and biological factors such as aneuploidy.
* **Low Confidence Zone:** Automatic highlighting for samples with TC < 30%, where diagnostic reliability may be reduced due to low tumor purity.
* **Convergence Zone (Gray Zone) Alert:** A targeted warning system for samples where theoretical curves for germline LOH and somatic LOH converge (typically TC 60–75%). In this range, distinguishing events based on VAF alone is mathematically challenging.
* **Fixed Scaling:** A standardized 0–100% scale for both axes ensures a consistent visual perspective for clinical comparison.

## Clinical Significance
Distinguishing between germline and somatic variants is a complex task in tumor-only sequencing. As demonstrated in clinical studies, samples with high tumor content (TC ≥ 90%) and elevated VAFs are at risk of being misidentified as somatic events, while they may actually represent **Germline LOH**.

Accurate identification of **Biallelic inactivation (LOH)** is therapeutically significant. Regardless of whether the initial variant is germline or somatic in origin, the presence of LOH is a critical indicator for sensitivity to targeted therapies, such as **PARP inhibitors** in ovarian and breast cancers.

## How to Use
1. **Input Parameters:** Use the sidebar to input the **Gene Name**, **Pathological TC (%)** (determined via pathological assessment), and observed **VAF (%)**.
2. **Analyze:** The black circle represents your specific clinical sample.
3. **Automated Interpretation:** The tool identifies which theoretical models align within the 10% measurement error of your data.
4. **Clinical Correlation:** If the sample falls into the **Convergence Zone**, a warning will appear prompting further clinical correlation (e.g., family history or drug response).

## Installation (Local Execution)
To run this tool locally:
```bash
git clone [https://github.com/Clinical-Genetics-Suite/vaf-tc-app.git](https://github.com/Clinical-Genetics-Suite/vaf-tc-app.git)
cd vaf-tc-app
pip install -r requirements.txt
streamlit run app.py
