import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/digital_readiness_master.csv")

st.set_page_config(page_title="India Digital Readiness Dashboard", layout="wide")

st.title("🧭 Digital Commerce Readiness & Entrepreneurship Dashboard")

# Sidebar filters
state = st.sidebar.selectbox("Select a State", sorted(df['state_name'].unique()))

# Tab layout
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 DCRI Heatmap",
    "🏢 MSME vs Startup",
    "💳 Financial Inclusion",
    "📦 Cluster Analysis",
    "🔍 Outliers",
    "📚 Literacy & Broadband"
])

# --- Tab 1: DCRI Heatmap ---
with tab1:
    st.subheader("State-wise Digital Commerce Readiness Index (DCRI)")
    fig = px.choropleth(df,
                        locations="state_name",
                        locationmode="geojson-id",  # requires India geojson map
                        color="DCRI",
                        color_continuous_scale="YlGnBu",
                        title="DCRI Score by State")
    st.plotly_chart(fig, use_container_width=True)

# --- Tab 2: MSME and Startups ---
with tab2:
    st.subheader("MSME and Startup Density")
    fig = px.scatter(df, x="msmes_per_1000_pop", y="total_startups",
                     color="cluster",
                     size="population", hover_name="state_name",
                     title="MSME vs Startups")
    st.plotly_chart(fig, use_container_width=True)

# --- Tab 3: PMJDY and RuPay ---
with tab3:
    st.subheader("Financial Inclusion Metrics")
    fig = px.scatter(df, x="pmjdy_accounts_per_1000_pop", y="rupay_cards_per_account",
                     size="avg_balance_per_account", color="DCRI",
                     hover_name="state_name",
                     title="PMJDY vs RuPay Card Usage")
    st.plotly_chart(fig, use_container_width=True)

# --- Tab 4: Clustering ---
with tab4:
    st.subheader("Cluster Typology")
    st.dataframe(df[['state_name', 'cluster', 'DCRI', 'total_startups', 'msmes_per_1000_pop']])

# --- Tab 5: Outliers ---
with tab5:
    st.subheader("Outlier States")
    high_dcri_low_entre = df[(df['DCRI'] > 0.6) & (df['total_startups'] < 0.3)]
    st.write("📌 High DCRI but Low Entrepreneurship:")
    st.dataframe(high_dcri_low_entre)

# --- Tab 6: Education + Broadband ---
with tab6:
    st.subheader("Literacy, Enrollment & Broadband")
    fig = px.scatter_3d(df, x='literacy_rate', y='enrollment_per_1000_pop', z='broadband_rural',
                        color='cluster', hover_name='state_name',
                        title="Education & Access Factors")
    st.plotly_chart(fig, use_container_width=True)
