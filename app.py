import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import io

# 1. Page Configuration
st.set_page_config(page_title="VAF-TC Precision Analyzer", layout="wide")

# 2. Title
st.title("🧬 VAF-TC Precision Analyzer")
st.markdown("Interactive clinical decision-support tool for germline/somatic variant differentiation.")

# 3. Sidebar Input Parameters
st.sidebar.header("📋 Patient Data Input")
st.sidebar.markdown("👉 **Please enter Gene Name, TC, and VAF.**")

gene_name = st.sidebar.text_input("Gene Name", value="BRCA2")
tc_input = st.sidebar.slider("Pathological Tumor Content (TC %)", 0, 100, 50) # Set default to 50 to show the trap
vaf_input = st.sidebar.slider("Variant Allele Fraction (VAF %)", 0, 100, 50)

st.sidebar.markdown("---")
st.sidebar.info(f"💡 **Analysis Mode:** {gene_name}")

tc = tc_input / 100.0
vaf = vaf_input / 100.0

# 4. Mathematical Foundation (5-Line Logic)
x_range = np.linspace(0.01, 1.0, 100)
y_germ_cnloh = (1 + x_range) / 2
y_germ_del = 1 / (2 - x_range)
y_germ_hetero = np.full_like(x_range, 0.5)
y_som_cnloh = x_range
y_som_del = x_range / (2 - x_range)

# 5. Main Layout (Left 1 : Right 2)
col_alerts, col_graph = st.columns([1, 2])

# --- LEFT COLUMN: Clinical Interpretation & Alerts ---
with col_alerts:
    st.subheader("📋 Interpretation & Alerts")
    
    # Mathematical Match Analysis (±10% error margin)
    error_margin = 0.10
    models_check = {
        "Germline + cnLOH": (1 + tc) / 2,
        "Germline + LOH (Del)": 1 / (2 - tc),
        "Germline (Hetero)": 0.5,
        "Somatic + cnLOH": tc,
        "Somatic + LOH (Del)": tc / (2 - tc)
    }
    compatible_models = [name for name, val in models_check.items() if abs(val - vaf) <= error_margin]

    if compatible_models:
        st.success(f"**Compatible Models for {gene_name}:**")
        for m in compatible_models:
            st.markdown(f"- **{m}**")

    # --- Specific Clinical Alerts (The "Traps") ---
    
    # NEW: The cnLOH Trap (TC ≈ 50%)
    if 40 <= tc_input <= 60:
        st.warning(f"⚠️ **Somatic cnLOH Trap:** At TC {tc_input}%, Somatic cnLOH (UPD) produces a VAF of ~50%, perfectly mimicking a Germline Heterozygous variant. Pair-normal testing is essential.")

    # The Deletion Trap (TC 60-75%)
    if 60 <= tc_input <= 75:
        st.warning(f"⚠️ **50% VAF Trap (Del):** At this TC, Somatic LOH (deletion) results in a VAF of ~50%. Do not assume germline origin without confirmation.")

    # Convergence Alert (TC >= 70%)
    if tc_input >= 70:
        st.error("⚠️ **LOH Convergence Alert:** High purity causes Germline and Somatic LOH lines to converge. Origin is hard to distinguish by VAF alone.")

    # Mathematical Limit (TC >= 90%)
    if tc_input >= 90:
        st.info("💡 **Mathematical Limit:** At TC ≥ 90%, models converge toward 100%. Check family history.")

    st.divider()

    # Feature: Excel Template Download
    st.subheader("📊 Multi-variant Workflow")
    template_df = pd.DataFrame({"Gene": [gene_name, "TP53"], "TC": [tc_input, tc_input], "VAF": [vaf_input, 0.0]})
    csv_buffer = io.BytesIO()
    template_df.to_csv(csv_buffer, index=False)
    st.download_button("📥 Download Excel/CSV Template", csv_buffer.getvalue(), "VAF_TC_Template.csv", "text/csv")

    # Clinical Notes
    with st.expander("📝 Clinical Notes", expanded=True):
        st.markdown("""
        **PARPi Indications:**
        - **Ovarian/Prostate:** gBRCA & sBRCA eligible.
        - **Breast/Pancreas:** gBRCA Only (includes **Talazoparib**).
        
        **Lynch Syndrome (MMR-d):**
        - High ICI responsiveness. 
        """)

# --- RIGHT COLUMN: Visualization ---
with col_graph:
    st.subheader("📈 VAF-TC Projection")
    fig = go.Figure()
    
    # 5 Theoretical Lines
    colors = {'Germline + cnLOH': '#d4af37', 'Germline + LOH (Del)': '#e41a1c', 'Germline (Hetero)': '#a65628', 
              'Somatic + cnLOH': '#4daf4a', 'Somatic + LOH (Del)': '#377eb8'}
    
    fig.add_trace(go.Scatter(x=x_range*100, y=y_germ_cnloh*100, name="Germline + cnLOH", line=dict(color=colors['Germline + cnLOH'], width=2)))
    fig.add_trace(go.Scatter(x=x_range*100, y=y_germ_del*100, name="Germline + LOH (Del)", line=dict(color=colors['Germline + LOH (Del)'], width=2)))
    fig.add_trace(go.Scatter(x=x_range*100, y=y_germ_hetero*100, name="Germline (Hetero)", line=dict(color=colors['Germline (Hetero)'], width=2)))
    fig.add_trace(go.Scatter(x=x_range*100, y=y_som_cnloh*100, name="Somatic + cnLOH", line=dict(color=colors['Somatic + cnLOH'], dash='dash')))
    fig.add_trace(go.Scatter(x=x_range*100, y=y_som_del*100, name="Somatic + LOH (Del)", line=dict(color=colors['Somatic + LOH (Del)'], dash='dot')))

    # Case Plot
    fig.add_trace(go.Scatter(
        x=[tc_input], y=[vaf_input], mode='markers+text',
        name=f"Current: {gene_name}",
        text=[f"{gene_name}<br>TC:{tc_input}%<br>VAF:{vaf_input}%"],
        textposition="top right", marker=dict(color='black', size=14, symbol='x')
    ))

    # Low Confidence Zone
    fig.add_vrect(x0=0, x1=30, fillcolor="gray", opacity=0.1, layer="below", line_width=0, 
                  annotation_text="Low Confidence Zone", annotation_position="top left")

    fig.update_layout(
        xaxis_title="Pathological Tumor Content (%)", yaxis_title="Variant Allele Fraction (%)",
        yaxis=dict(range=[0, 105]), xaxis=dict(range=[0, 105]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="simple_white", height=600
    )
    st.plotly_chart(fig, use_container_width=True)

# 6. Footer
st.divider()
st.caption("VAF-TC Precision Analyzer | Clinical Genetics Suite | ver 2.6 ✅")
