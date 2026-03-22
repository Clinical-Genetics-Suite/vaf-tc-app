import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Professional Page Configuration ---
st.set_page_config(page_title="VAF-TC Visualizer", layout="wide")
st.title("🧪 VAF–Tumor Content Graph Visualizer")
st.markdown("""
This interactive tool visualizes the relationship between **Variant Allele Fraction (VAF)** and **Tumor Content (TC)** based on the **Knudson two-hit hypothesis**. It is designed to assist in discriminating between germline and somatic variants in tumor-only sequencing data[cite: 23, 33, 42].
""")

# --- Sidebar for Data Input ---
st.sidebar.header("Patient Data Input")
tc = st.sidebar.slider("Pathological Tumor Content (%)", 0, 100, 60) / 100.0
vaf = st.sidebar.slider("Observed VAF (%)", 0, 100, 50) / 100.0
gene = st.sidebar.text_input("Variant Identifier (e.g., BRCA2 p.L2848*)", "Variant X")

st.sidebar.info("""
**Instructions:** Adjust the sliders to plot the patient's data point (black dot). Observe its alignment with the theoretical reference lines [cite: 60-65].
""")

# --- Layout: Main Visualization Area ---
col1, col2 = st.columns([3, 1])

with col1:
    # Mathematical Modeling based on Diploid Assumptions [cite: 63, 173-176]
    # Theoretical lines derived from the two-hit model
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
    - **Solid Lines:** Suggest potential germline origin or biallelic inactivation (LOH) [cite: 173-176].
    - **Dashed Lines:** Suggest potential somatic origin[cite: 63, 67].
    - **Gray Zone (TC 60-70%):** Note the mathematical overlap between Somatic LOH and Germline lines [cite: 243-244, 250].
    """)

# --- Formal Disclaimer for Publication ---
st.divider()
st.caption("""
**Clinical Disclaimer:** This application is intended for educational and supportive visual communication purposes in genetic counseling and expert panel discussions[cite: 30, 215]. It is not a standalone diagnostic tool[cite: 233, 271]. Interpretations should be integrated with clinical history, family pedigree, and institutional guidelines [cite: 246-247].
""")