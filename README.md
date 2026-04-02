# VAF-TC Precision Analyzer

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vaf-tc-app.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive visual tool for differentiating germline and somatic variants in **tumor-only sequencing**, based on the mathematical relationship between pathological **Tumor Content (TC)** and **Variant Allele Fraction (VAF)**.

> **Disclaimer:** This tool is intended as a supportive aid for genetic counseling. It does not replace confirmatory germline testing or established clinical guidelines (ACMG, AMED Kosugi group). Further prospective validation is required.
> This tool does not incorporate gene-specific prior probabilities. Clinical context and family history are essential for interpretation.

## Live Application

**https://vaf-tc-app.streamlit.app/**

## Background

In tumor-only comprehensive genomic profiling (CGP), distinguishing germline from somatic variants is a fundamental challenge. While VAF of approximately 50% is often assumed to indicate a germline heterozygous variant, **somatic variants with LOH can produce the same VAF** depending on tumor content — a diagnostic trap.

This tool visualizes five theoretical VAF-TC models derived from **Knudson's two-hit hypothesis** (diploid model) and provides automated clinical alerts for known ambiguity zones.

## Mathematical Models

Given tumor content *f* (0-1):

| Model | Formula | Description |
|-------|---------|-------------|
| Germline + cnLOH | VAF = (1 + f) / 2 | Germline variant with copy-neutral LOH (UPD) |
| Germline + LOH (Del) | VAF = 1 / (2 - f) | Germline variant with LOH by deletion |
| Germline Heterozygous | VAF = 0.5 | Germline variant without LOH |
| Somatic + cnLOH | VAF = f | Somatic variant with copy-neutral LOH (UPD) |
| Somatic + LOH (Del) | VAF = f / (2 - f) | Somatic variant with LOH by deletion |

A **+/-10% error margin** is applied for model matching to account for variability in pathological TC estimation.

## Clinical Alert System

The app generates six context-dependent alerts based on TC and VAF:

### Alert 1 - Somatic cnLOH Trap (TC 40-60%)

At TC near 50%, Somatic + cnLOH produces VAF = TC, which falls within +/-10% of Germline Heterozygous (50%). A somatic variant with acquired uniparental disomy (UPD) can masquerade as a germline finding. Pair-normal testing is essential.

### Alert 2 - Gray Zone (TC 61-66%)

As TC increases toward 66.7%, Somatic + LOH (Del) = f/(2-f) approaches 50% from below. In this range, the somatic LOH deletion line is close enough to 50% to create ambiguity with Germline Heterozygous variants.

### Alert 3 - LOH Convergence Zone (TC >= 67%)

At TC = 2/3 (approximately 66.7%), Somatic + LOH (Del) **exactly equals** Germline Heterozygous at 50%. Above this TC, the somatic and germline LOH lines converge. This alert fires when:

- **TC >= 67%**, AND
- **VAF >= Somatic LOH (Del) line** at current TC

Both conditions must be met. The alert displays the actual theoretical values for clinical reference.

### Alert 4 - Extreme Tumor Purity (TC >= 90%)

At very high purity, all five theoretical models compress into a narrow VAF range. Variants may still be of somatic origin even at high VAF. This alert fires regardless of VAF, as germline testing becomes essential in all cases.

### Alert 5 - Low VAF (VAF <= 20%)

The reliability of the theoretical line is reduced at low VAF. Low VAF may reflect subclonal variants, admixture with normal tissue, or technical noise.

### Alert 6 - High VAF (VAF >= 60%)

High VAF does not exclude a somatic origin. Somatic LOH or copy number changes can elevate VAF into this range.

## Gene Reference System

The app provides gene-specific contextual messages in three categories:

| Category | Genes | Message |
|---|---|---|
| 🟡 Germline-priority | BRCA1, BRCA2, PALB2, ATM, CHEK2, MLH1, MSH2, MSH6, PMS2, RAD51C, RAD51D, CDH1, VHL, RB1, NF1, STK11 | Germline variants are clinically significant. Confirmatory testing is recommended. |
| 🟠 Both important | TP53, APC, PTEN, CDKN2A | Both germline and somatic variants are clinically important. Clinical context is essential. |
| 🔵 Somatic-priority | KRAS, PIK3CA, BRAF, EGFR, NRAS, IDH1, IDH2, MET, CDK4 | Germline variants are extremely rare. Most likely somatic in origin. |
| ⬜ Not listed | All other genes | Consult established clinical guidelines and family history. |

## Features

- **Interactive graph** with five theoretical VAF-TC curves (Plotly)
- **Model matching** with +/-10% error margin and theoretical VAF display
- **Automated interpretation** based on compatible model combinations
- **Gene-specific messages** for 25 clinically relevant genes
- **Six clinical alerts** based on TC and VAF values
- **Low Confidence Zone** shading for TC < 30%
- **Multi-variant CSV upload** to plot multiple variants simultaneously on the graph
- **CSV template download** for multi-variant workflows
- **Theoretical model data download** (CSV and Excel) directly from the app

## Multi-variant Upload

Multiple variants from a single patient can be uploaded as a CSV file and plotted simultaneously on the graph. This is particularly useful for cases with high mutational burden (e.g., Lynch syndrome, POLE-mutant tumors).

**CSV format:**

```
Gene,TC,VAF
BRCA2,70,57
TP53,70,35
MSH2,70,68
```

Each variant is plotted with a distinct color and gene label. Interpretation and gene-specific messages are shown for each variant. A template CSV can be downloaded from within the app.

## Getting Started

### Requirements

- Python 3.9+
- Dependencies: streamlit, plotly, numpy, pandas

### Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Repository Contents

| File | Description |
|------|-------------|
| app.py | Main Streamlit application (ver 3.2) |
| requirements.txt | Python dependencies |
| VAF-TC theoretical_model.xlsx | Excel file for generating theoretical VAF-TC curves |
| VAF_TC_theoretical_model.csv | CSV version of the theoretical model data |
| data_dictionary.txt | Variable definitions for the theoretical model |

## Citation

If you use this tool in your research, please cite:

> Kashima M, Tsubamoto H, et al. "VAF-Tumor Content Graph: A Simple Visual Tool for Discriminating Germline and Somatic Variants in Tumor-Only Sequencing." *Journal of Human Genetics* (submitted).

## Authors

**Clinical Genetics Suite** - Hyogo Medical University

## License

MIT License
