import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv("data/digital_readiness_master.csv")
df = df.drop(columns=["diff", "outlier"], errors='ignore')

# Sidebar cluster filter
st.sidebar.header("Filters")
selected_cluster = st.sidebar.multiselect("Select Clusters", sorted(df["cluster"].unique()), default=sorted(df["cluster"].unique()))
df = df[df["cluster"].isin(selected_cluster)]

# Main Title
st.title("📊 Digital Commerce Readiness Dashboard")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏁 Overview",
    "📈 DCRI Breakdown",
    "🏢 Entrepreneurship",
    "💳 Financial Inclusion",
    "🌐 Access & Education",
    "🧩 Clusters & Outliers"
])

# ---- TAB 1: Overview ----
with tab1:
    st.subheader("🔝 Top 10 States by DCRI")
    top_states = df.sort_values("DCRI", ascending=False).head(10)
    fig1 = px.bar(top_states, x="state_name", y="DCRI", color="DCRI", title="Top 10 DCRI States")
    st.plotly_chart(fig1)

# ---- TAB 2: DCRI Breakdown ----
with tab2:
    st.subheader("📚 Literacy Rate vs DCRI")
    fig2 = px.scatter(df, x="literacy_rate", y="DCRI", color="cluster", hover_name="state_name", size="population")
    st.plotly_chart(fig2)

    st.subheader("📦 DCRI by Cluster")
    fig4, ax4 = plt.subplots()
    sns.boxplot(data=df, x="cluster", y="DCRI", palette="Set2", ax=ax4)
    st.pyplot(fig4)

# ---- TAB 3: Entrepreneurship ----
with tab3:
    st.subheader("🏢 MSME Density vs DCRI")
    fig3 = px.scatter(df, x="DCRI", y="msmes_per_1000_pop", size="population", color="cluster", hover_name="state_name")
    st.plotly_chart(fig3)

    st.subheader("📍 Compare States on Key Normalized Indicators")
    compare_states = st.multiselect("Select States", options=df["state_name"].unique(), default=["ANDHRA PRADESH", "BIHAR"])
    indicators = [
        "broadband_rural", "broadband_urban", "urban_share", "pmjdy_accounts_per_1000_pop",
        "rupay_cards_per_account", "avg_balance_per_account", "literacy_rate",
        "enrollment_per_1000_pop", "total_startups", "msmes_per_1000_pop"
    ]
    if compare_states:
        radar_df = df[df["state_name"].isin(compare_states)][["state_name"] + indicators].set_index("state_name").T
        fig_radar = px.line_polar(
            radar_df.reset_index().melt(id_vars="index", var_name="State", value_name="Value"),
            r="Value", theta="index", color="State", line_close=True
        )
        fig_radar.update_traces(fill='toself')
        st.plotly_chart(fig_radar)

# ---- TAB 4: Financial Inclusion ----
with tab4:
    st.subheader("📊 PMJDY Coverage vs RuPay Penetration")
    fig7 = px.scatter(df, x="pmjdy_accounts_per_1000_pop", y="rupay_cards_per_account",
                      size="avg_balance_per_account", color="cluster", hover_name="state_name")
    st.plotly_chart(fig7)

# ---- TAB 5: Access & Education ----
with tab5:
    st.subheader("📶 Broadband Access vs Urban Share")
    fig8 = px.scatter(df, x="broadband_rural", y="broadband_urban", size="urban_share",
                      color="cluster", hover_name="state_name")
    st.plotly_chart(fig8)

    st.subheader("🎓 Enrollment vs Literacy")
    fig9 = px.scatter(df, x="literacy_rate", y="enrollment_per_1000_pop",
                      color="cluster", hover_name="state_name")
    st.plotly_chart(fig9)

# ---- TAB 6: Clustering & Outliers ----
with tab6:
    st.subheader("🔍 Custom Feature vs DCRI")
    numeric_cols = df.select_dtypes(include='number').drop(columns=["cluster"], errors='ignore')
    feature_x = st.selectbox("Select X-axis feature", options=numeric_cols.columns, index=numeric_cols.columns.get_loc("literacy_rate"))
    fig6 = px.scatter(df, x=feature_x, y="DCRI", color="cluster", hover_name="state_name")
    st.plotly_chart(fig6)

    st.subheader("🔗 Correlation Heatmap")
    fig5, ax5 = plt.subplots(figsize=(10, 8))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", ax=ax5)
    st.pyplot(fig5)
