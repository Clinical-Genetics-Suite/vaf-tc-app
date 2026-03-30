import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Page Configuration for Academic Presentation
st.set_page_config(page_title="VAF-TC Visualizer", layout="wide")

st.title("🧬 VAF-TC Relationship Visualizer")
st.write("An interactive tool to visualize the theoretical relationship between Pathological Tumor Content (TC) and Variant Allele Fraction (VAF).")

# --- Sidebar Parameter Inputs ---
st.sidebar.header("📊 Input Parameters")
tc_input = st.sidebar.slider("Pathological Tumor Content (TC %)", 0, 100, 50)
vaf_input = st.sidebar.slider("Variant Allele Fraction (VAF %)", 0, 100, 50)

# --- Mathematical Model Calculations ---
def calculate_curves():
    tc_range = np.linspace(0, 1, 101)
    
    # Germline Models (Knudson's Two-Hit Theory)
    g_hetero = np.full_like(tc_range, 0.5)
    g_loh_del = 1 / (2 - tc_range)
    g_cnloh = 0.5 * (1 + tc_range)
    
    # Somatic Models
    s_hetero = 0.5 * tc_range
    s_loh_del = tc_range / (2 - tc_range)
    s_cnloh = tc_range
    
    return tc_range * 100, g_hetero * 100, g_loh_del * 100, g_cnloh * 100, s_hetero * 100, s_loh_del * 100, s_cnloh * 100

tc_plot, g_het, g_del, g_cn, s_het, s_del, s_cn = calculate_curves()

# --- Visualization Construction ---
fig = go.Figure()

# Plotting Theoretical Trajectories
fig.add_trace(go.Scatter(x=tc_plot, y=g_cn, name="Germline + cnLOH", line=dict(color='#D4AF37', width=2.5)))
fig.add_trace(go.Scatter(x=tc_plot, y=g_del, name="Germline + LOH (Del)", line=dict(color='red', width=2.5)))
fig.add_trace(go.Scatter(x=tc_plot, y=g_het, name="Germline (Hetero)", line=dict(color='brown', width=2.5)))
fig.add_trace(go.Scatter(x=tc_plot, y=s_cn, name="Somatic + cnLOH", line=dict(color='green', dash='dash')))
fig.add_trace(go.Scatter(x=tc_plot, y=s_del, name="Somatic + LOH (Del)", line=dict(color='#666', dash='dot')))

# Highlighting the Low Confidence Zone (TC < 30%)
fig.add_vrect(x0=0, x1=30, fillcolor="rgba(200, 200, 200, 0.2)", layer="below", line_width=0, 
              annotation_text="Low Confidence Zone", annotation_position="top left")

# User-Defined Data Point
fig.add_trace(go.Scatter(x=[tc_input], y=[vaf_input], name="Current Sample", mode='markers+text',
                         marker=dict(color='black', size=14, symbol='circle'),
                         text=[f"TC:{tc_input}% VAF:{vaf_input}%"], textposition="top right"))

# Axis Formatting (Fixed 0-100% range as requested)
fig.update_layout(
    xaxis=dict(title="Pathological Tumor Content (%)", range=[0, 100], dtick=10, gridcolor='#eee'),
    yaxis=dict(title="Variant Allele Fraction (%)", range=[0, 100], dtick=25, gridcolor='#eee'),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    plot_bgcolor='white',
    margin=dict(l=40, r=40, t=80, b=40),
    height=650
)

st.plotly_chart(fig, use_container_width=True)

# --- Automated Alert System ---

# 1. Convergence Zone (Gray Zone) Alert (Triggered at TC >= 70%)
if tc_input >= 70:
    st.warning(f"""
    ⚠️ **Convergence Zone (Gray Zone) Alert**:  
    At the current Tumor Content of **{tc_input}%**, theoretical VAF values for **Germline LOH** and **Somatic LOH** converge. 
    Distinguishing between these events based solely on VAF is mathematically difficult in this high-purity range. 
    Please incorporate clinical data (e.g., family history or therapeutic response) for accurate interpretation.
    """)

# 2. Low Confidence Zone Alert (Triggered at TC < 30%)
elif tc_input < 30:
    st.info("ℹ️ **Low Confidence Zone**: Please note that interpretation reliability may be limited in samples with Tumor Content below 30%.")

# --- Clinical Interpretation Section ---
st.markdown("---")
st.subheader("📝 Clinical Interpretation Notes")
st.write(f"""
- **Convergence Phenomenon**: The "Gray Zone" occurs because the mathematical difference between somatic and germline VAFs narrows as tumor purity increases toward 100%.
- **High-TC Case Insights**: In our study, high-TC samples ($\ge$ 90%) with elevated VAFs were confirmed as **Germline LOH** rather than somatic events. This distinction is critical, as such cases (e.g., SEC) have demonstrated favorable responses to PARP inhibitors in clinical practice.
""")
