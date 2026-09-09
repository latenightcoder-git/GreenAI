import streamlit as st
from sustainability import (
    load_data,
    calculate_energy,
    calculate_co2,
    get_summary,
    responsible_ai_audit
)
from gemini_ai import get_sustainability_advice

# Page Configuration
st.set_page_config(
    page_title="GreenAI Monitor",
    page_icon="🌿",
    layout="wide"
)

# Title
st.title("🌿 GreenAI Monitor")
st.subheader("A GenAI-Powered Sustainable AI Usage Analyzer")

# Load and process data
df = load_data("ai_usage.csv")
df = calculate_energy(df)
df = calculate_co2(df)

summary = get_summary(df)
audit = responsible_ai_audit(df, summary)

# Dashboard Metrics
st.divider()
st.header("📊 Sustainability Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🤖 AI Requests",
        f"{summary['total_requests']:,}"
    )

with col2:
    st.metric(
        "⚡ Energy",
        f"{summary['total_energy']:.2f} kWh"
    )

with col3:
    st.metric(
        "🌍 Estimated CO2",
        f"{summary['total_co2']:.2f} kg"
    )

with col4:
    st.metric(
        "💚 Sustainability Score",
        f"{summary['score']}/100"
    )

# AI Usage Data
st.divider()
st.header("📋 AI Usage Data")
st.dataframe(df, use_container_width=True)

# Model Analysis
st.divider()
st.header("🏗️ Energy by AI Model")
model_energy = df.groupby("model")["energy_kwh"].sum()
st.bar_chart(model_energy)

# Department Analysis
st.divider()
st.header("🏢 Energy by Department")
department_energy = df.groupby("department")["energy_kwh"].sum()
st.bar_chart(department_energy)

# CO2 Analysis
st.divider()
st.header("📈 Daily CO2 Estimate")
daily_co2 = df.groupby("date")["co2_kg"].sum()
st.line_chart(daily_co2)

# Responsible AI Audit
st.divider()
st.header("🔍 Responsible AI Audit")

if audit["responsible_ai"]:
    st.success("✅ All Responsible AI checks passed")
else:
    st.error("❌ Some Responsible AI checks failed")

col1, col2 = st.columns(2)

with col1:
    st.write("✅ Data Complete:" if audit["data_complete"] else "❌ Data Complete:", "✅" if audit["data_complete"] else "❌")
    st.write("✅ No Missing Critical Values:" if audit["no_missing_values"] else "❌ No Missing Critical Values:", "✅" if audit["no_missing_values"] else "❌")
    st.write("✅ Transparent Calculation:" if audit["calculation_transparent"] else "❌ Transparent Calculation:", "✅" if audit["calculation_transparent"] else "❌")

with col2:
    st.write("✅ Explainable Score:" if audit["score_explainable"] else "❌ Explainable Score:", "✅" if audit["score_explainable"] else "❌")
    st.write("✅ Human Oversight:" if audit["human_oversight"] else "❌ Human Oversight:", "✅" if audit["human_oversight"] else "❌")
    st.write("✅ Grounded in Data:" if audit["grounded_in_data"] else "❌ Grounded in Data:", "✅" if audit["grounded_in_data"] else "❌")
    st.write("✅ Estimate Disclosed:" if audit["estimate_disclosed"] else "❌ Estimate Disclosed:", "✅" if audit["estimate_disclosed"] else "❌")

# Gemini AI Advisor
st.divider()
st.header("🤖 Gemini Sustainable AI Advisor")

st.write(
    "Gemini will analyze the calculated metrics and provide sustainability recommendations."
)

if st.button("🚀 Generate AI Sustainability Report"):
    with st.spinner("🧠 Gemini is analyzing the AI usage..."):
        try:
            advice = get_sustainability_advice(summary)
            st.success("✅ AI Sustainability Report Generated")
            st.markdown(advice)
        except Exception as e:
            st.error(f"❌ Gemini error: {e}")

# Responsible AI & Digital Trust
st.divider()
st.header("🌟 Responsible AI & Digital Trust")

st.markdown("""
### 🔍 Transparency
The application shows how energy and CO₂ estimates are calculated.

### 📖 Explainability
The sustainability score is based on understandable rules.

### 👤 Human Oversight
Gemini provides recommendations. Humans make the final decisions.

### 🌱 Sustainability
The application encourages efficient AI usage and smaller models where possible.

### 🔒 Digital Trust
Users can inspect the underlying dataset, calculations and AI-generated recommendations.
""")

st.caption(
    "Note: Energy and CO₂ figures are educational estimates based on dummy data and assumptions."
)