import streamlit as st
import pandas as pd

st.set_page_config(page_title="Agent Influence Protocol Demo", layout="wide")

st.title("Agent Influence Protocol (AIP) Simulation")
st.subheader("Resolving the Loyalty Paradox in AI-Mediated Commerce")

# --------------------------
# Brand Data
# --------------------------
data = {
    "Brand": ["Brand A (Premium)", "Brand B (Cheapest)", "Brand C (Fast Delivery)"],
    "Price Score": [70, 95, 80],
    "Reliability": [95, 70, 75],
    "Sustainability": [85, 60, 65],
    "Trust History": [90, 65, 70],
    "Profit Margin (%)": [25, 10, 15],
}

df = pd.DataFrame(data)

st.write("### Brand Data")
st.dataframe(df)

# --------------------------
# Baseline Agent
# --------------------------
st.write("## Baseline AI Agent (Price-Only Logic)")
baseline_winner = df.loc[df["Price Score"].idxmax()]

st.write(f"🏆 Winner: **{baseline_winner['Brand']}**")
st.write("Reason: AI optimizes only for lowest price.")

st.divider()

# --------------------------
# AIP Weights
# --------------------------
st.write("## Configure AI Agent Preferences")

price_weight = st.slider("Price Weight (%)", 0, 100, 40)
reliability_weight = st.slider("Reliability Weight (%)", 0, 100, 30)
sustainability_weight = st.slider("Sustainability Weight (%)", 0, 100, 20)
trust_weight = st.slider("Trust Weight (%)", 0, 100, 10)

total_weight = price_weight + reliability_weight + sustainability_weight + trust_weight

if total_weight != 100:
    st.warning(f"Total weight must equal 100%. Current total: {total_weight}%")

else:
    st.success("Weights correctly configured.")

    # Convert weights to decimals
    price_weight /= 100
    reliability_weight /= 100
    sustainability_weight /= 100
    trust_weight /= 100

    # --------------------------
    # AIP Scoring
    # --------------------------
    df["Final Score"] = (
        df["Price Score"] * price_weight +
        df["Reliability"] * reliability_weight +
        df["Sustainability"] * sustainability_weight +
        df["Trust History"] * trust_weight
    )

    st.write("### AIP Weighted Scores")
    st.dataframe(df[["Brand", "Final Score"]].sort_values(by="Final Score", ascending=False))

    aip_winner = df.loc[df["Final Score"].idxmax()]

    st.write(f"🏆 AIP Winner: **{aip_winner['Brand']}**")
    st.write("Reason: Optimized for multi-dimensional loyalty preferences.")

    # --------------------------
    # Ranking Chart
    # --------------------------
    st.write("### Brand Ranking Comparison")
    chart_df = df.sort_values(by="Final Score", ascending=False)
    st.bar_chart(chart_df.set_index("Brand")["Final Score"])

    # --------------------------
    # Business Impact Simulation
    # --------------------------
    st.write("### Business Impact Simulation")

    baseline_margin = baseline_winner["Profit Margin (%)"]
    aip_margin = aip_winner["Profit Margin (%)"]

    st.write(f"Baseline Agent Selected Margin: {baseline_margin}%")
    st.write(f"AIP Agent Selected Margin: {aip_margin}%")

    margin_difference = aip_margin - baseline_margin

    if margin_difference > 0:
        st.success(f"AIP preserves {margin_difference}% higher margin.")
    elif margin_difference < 0:
        st.error(f"AIP reduces margin by {abs(margin_difference)}%.")
    else:
        st.info("No margin difference.")

    st.divider()

    # --------------------------
    # Enterprise Optimization Simulator
    # --------------------------
    st.write("## Enterprise Optimization Simulator")

    selected_brand = st.selectbox(
        "Select a Brand to Improve",
        df["Brand"]
    )

    improvement_metric = st.selectbox(
        "Select Metric to Improve",
        ["Reliability", "Sustainability", "Trust History"]
    )

    improvement_value = st.slider("Increase Score By", 0, 20, 5)

    # Create simulation copy
    sim_df = df.copy()

    sim_df.loc[sim_df["Brand"] == selected_brand, improvement_metric] += improvement_value

    # Recalculate simulated scores
    sim_df["Simulated Score"] = (
        sim_df["Price Score"] * price_weight +
        sim_df["Reliability"] * reliability_weight +
        sim_df["Sustainability"] * sustainability_weight +
        sim_df["Trust History"] * trust_weight
    )

    st.write("### Simulated Ranking After Improvement")
    st.dataframe(
        sim_df[["Brand", "Simulated Score"]]
        .sort_values(by="Simulated Score", ascending=False)
    )

    new_winner = sim_df.loc[sim_df["Simulated Score"].idxmax()]

    st.success(f"New AI Selection After Optimization: {new_winner['Brand']}")

st.divider()

st.markdown("""
### Key Insight

Without AIP → AI selects lowest price.  
With AIP → AI selects long-term value aligned brand.  

Loyalty becomes operational, measurable, and algorithmically influential.
""")