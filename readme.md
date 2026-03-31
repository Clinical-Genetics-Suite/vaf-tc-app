# VAF-TC Precision Analyzer: Clinical Genetics Support Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vaf-tc-app.streamlit.app/)

## 🧬 Overview
**VAF-TC Precision Analyzer** is a clinical decision-support tool designed to differentiate between somatic and germline variants by modeling the mathematical relationship between **Pathological Tumor Content (TC)** and **Variant Allele Frequency (VAF)**. 

By applying theoretical lines based on **Knudson’s two-hit model**, this tool facilitates the identification of hereditary cancer syndromes and helps interpret the clinical significance of variants in high-purity or hypermutated tumor samples.

---

## 🚀 Key Features

### 1. The "50% VAF Trap" Alert (Dynamic Logic)
One of the most critical pitfalls in clinical NGS is the reflexive interpretation of a **VAF ≈ 50%** as a germline variant. 
- **The Intersection:** At TC ≈ 66.7%, a **Somatic LOH (deletion)** event yields a theoretical VAF of exactly **50%**.
- **Dynamic Alert:** When TC is between 60-75%, the app triggers a warning to prevent misidentifying somatic drivers as hereditary findings in this specific "Grey Zone."

### 2. Support for Hypermutated & TMB-High Tumors
Particularly useful for interpreting cases with high mutational burdens, such as **MMR-deficient (Lynch syndrome)** and **POLE-mutant** tumors. The tool allows clinicians to plot and mark multiple variants from a single case on a dedicated Excel-based theoretical model, facilitating practical, case-by-case marking for complex clinical records.

### 3. Mathematical Convergence Analysis (TC ≥ 90%)
At very high tumor purity, theoretical models for Somatic LOH and Germline LOH converge. The tool flags this "Convergence Zone" to remind clinicians that VAF alone cannot distinguish a variant's origin without clinical correlation and family history.

---

## 🩺 Clinical Significance

### Inferring Hereditary Cancer Syndromes
Hereditary cancers driven by tumor suppressor gene alterations (e.g., **HBOC, Lynch Syndrome, and FAP**) can be efficiently inferred using theoretical lines based on Knudson’s two-hit model. The ability to visualize whether an observed VAF aligns with a "two-hit" theoretical line provides strong supportive evidence for the variant's clinical relevance.

### Therapeutic Implications
Identifying the genomic status of a tumor is therapeutically significant:
- **BRCA1/2-associated tumors:** May indicate sensitivity to **PARP inhibitors**.
- **Lynch Syndrome (MMR-d):** May predict responsiveness to **Immune Checkpoint Inhibitors (ICIs)**.
*Note: In Lynch syndrome, the curative potential with ICIs is a significant clinical observation, though it remains a subject of ongoing discussion compared to epigenetic dMMR tumors.*

---

## 🛠 How to Use

- **Online:** Use the [Web App](https://vaf-tc-app.streamlit.app/) for quick, interactive visualization.
- **Offline / Batch Processing:** Download the provided **.xlsx** file to process multiple mutant genes in a single clinical case, allowing for comprehensive marking and paper-based clinical records.

---

## 📊 Mathematical Foundation
The app utilizes the following frameworks ($f$ = Tumor Fraction):
- **Somatic Heterozygous:** $VAF = f / 2$
- **Somatic LOH (Deletion):** $VAF = f / (2 - f)$
- **Germline Heterozygous:** $VAF = 0.5$
- **Germline LOH (Deletion):** $VAF = 1 / (2 - f)$

---

## 👥 Authors & Contribution
- **Organization:** Clinical Genetics Suite
- **Maintainer:** Sawai1960
- **License:** MIT License
