import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Professional Page Configuration ---
st.set_page_config(page_title="VAF-TC Visualizer", layout="wide")
st.title("🧪 VAF–Tumor Content Graph Visualizer")
st.markdown("""
This interactive tool visualizes the relationship between **Variant Allele Fraction (VAF)** and **Tumor Content (TC)** based on the **Knudson two-hit hypothesis**. It is designed to assist in discriminating between germline and somatic variants in tumor-only sequencing data.
""")

# --- Sidebar for Data Input ---
st.sidebar.header("Patient Data Input")
tc = st.sidebar.slider("Pathological Tumor Content (%)", 0, 100, 60) / 100.0
vaf = st.sidebar.slider("Observed VAF (%)", 0, 100, 50) / 100.0
gene = st.sidebar.text_input("Variant Identifier (e.g., BRCA2 p.L2848*)", "Variant X")

st.sidebar.info("""
**Instructions:** Adjust the sliders to plot the patient's data point (black dot). Observe its alignment with the theoretical reference lines derived from the two-hit model.
""")

# --- Layout: Main Visualization Area ---
col1, col2 = st.columns([3, 1])

with col1:
    x_range = np.linspace(0.01, 1.0, 100)
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Plotting Theoretical Reference Lines
    ax.plot(x_range, 0.5 * x_range + 0.5, color='#D4AF37', label="Germline + Copy-neutral LOH")
    ax.plot(x_range, 1 / (2 - x_range), color='red', label="Germline + LOH (Deletion)")
    ax.axhline(0.5, color='brown', linewidth=2, label="Germline (Heterozygous)")
    ax.plot(x_range, x_range, color='green', linestyle='--', alpha=0.5, label="Somatic + Copy-neutral LOH")
    ax.plot(x_range, x_range / (2 - x_range), color='gray', linestyle=':', label="Somatic + LOH (Deletion)")
    ax.plot(x_range, 0.5 * x_range, color='gray', linestyle='--', alpha=0.5, label="Somatic (Heterozygous)")
    
    # Plotting Patient Data Point
    ax.scatter(tc, vaf, color='black', s=200, zorder=5, label=f"Patient: {gene}")
    
    # Graph Formatting
    ax.set_xlabel("Tumor Content (x)", fontsize=12)
    ax.set_ylabel("Variant Allele Fraction (VAF)", fontsize=12)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Theoretical vs. Observed VAF-TC Distribution", fontsize=14)
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
    ax.grid(True, which='both', linestyle='--', alpha=0.3)
    
    st.pyplot(fig)

with col2:
    st.header("Interpretation")
    st.write(f"**Target:** {gene}")
    st.write(f"**Input TC:** {tc*100:.1f}%")
    st.write(f"**Input VAF:** {vaf*100:.1f}%")
    
    st.markdown("""
    ---
    **Reference Guide:**
    - **Solid Lines:** Suggest potential germline origin or biallelic inactivation (LOH) according to the two-hit model.
    - **Dashed Lines:** Suggest potential somatic origin.
    - **Gray Zone (TC 60-70%):** Note the mathematical overlap between Somatic LOH and Germline lines, where clinical integration is essential.
    """)

# --- Formal Disclaimer for Publication ---
st.divider()
st.caption("""
**Clinical Disclaimer:** This application is intended for educational and supportive visual communication purposes in genetic counseling and expert panel discussions. It is not a standalone diagnostic tool. Interpretations should be integrated with clinical history, family pedigree, and institutional guidelines.
""")
