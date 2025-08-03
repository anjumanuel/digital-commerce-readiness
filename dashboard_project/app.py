import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv("data/digital_readiness_master.csv")

# Drop unwanted columns
df = df.drop(columns=["diff", "outlier"], errors='ignore')

# Title
st.title("📊 Digital Commerce Readiness Dashboard")

# Sidebar
st.sidebar.header("Filters")
selected_cluster = st.sidebar.multiselect("Select Clusters", sorted(df["cluster"].unique()), default=sorted(df["cluster"].unique()))
df = df[df["cluster"].isin(selected_cluster)]

# Section 1: Top 10 states by DCRI
st.header("🔝 Top 10 States by Digital Commerce Readiness Index (DCRI)")
top_states = df.sort_values("DCRI", ascending=False).head(10)
fig1 = px.bar(top_states, x="state_name", y="DCRI", color="DCRI", title="Top 10 DCRI States")
st.plotly_chart(fig1)

# Section 2: Literacy vs DCRI
st.header("📚 Literacy Rate vs DCRI")
fig2 = px.scatter(df, x="literacy_rate", y="DCRI", color="cluster", hover_name="state_name",
                  size="population", title="Literacy vs DCRI by Cluster")
st.plotly_chart(fig2)

# Section 3: MSME Density vs DCRI (Bubble plot)
st.header("🏢 MSME Density vs DCRI")
fig3 = px.scatter(df, x="DCRI", y="msmes_per_1000_pop", size="population", color="cluster",
                  hover_name="state_name", title="MSME per 1000 vs DCRI (Bubble Size = Population)")
st.plotly_chart(fig3)

# Section 4: DCRI by Cluster (Boxplot)
st.header("📦 DCRI Distribution by Cluster")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df, x="cluster", y="DCRI", palette="Set2", ax=ax4)
st.pyplot(fig4)

# Section 5: Correlation Heatmap
st.header("🔗 Feature Correlation Heatmap")
numeric_cols = df.select_dtypes(include='number').drop(columns=["cluster"], errors='ignore')
fig5, ax5 = plt.subplots(figsize=(10, 8))
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", ax=ax5)
st.pyplot(fig5)

# Section 6: Choose your own comparison
st.header("🔍 Custom Feature vs DCRI Comparison")
feature_x = st.selectbox("Select X-axis feature", options=numeric_cols.columns)
fig6 = px.scatter(df, x=feature_x, y="DCRI", color="cluster", hover_name="state_name", trendline="ols")
st.plotly_chart(fig6)

# Section 7: Compare States on Key Normalized Indicators
st.header("📍 Compare States on Key Normalized Indicators")

compare_states = st.multiselect(
    "Select States to Compare",
    options=df["state_name"].unique(),
    default=["ANDHRA PRADESH", "BIHAR"]
)

key_indicators = [
    "broadband_rural", "broadband_urban", "urban_share",
    "pmjdy_accounts_per_1000_pop", "rupay_cards_per_account", 
    "avg_balance_per_account", "literacy_rate", 
    "enrollment_per_1000_pop", "total_startups", 
    "msmes_per_1000_pop"
]

if compare_states:
    compare_df = df[df["state_name"].isin(compare_states)][["state_name"] + key_indicators].set_index("state_name")
    compare_df = compare_df.T  # Transpose for radar chart format

    # Radar chart using plotly
    fig_radar = px.line_polar(
        compare_df.reset_index().melt(id_vars="index", var_name="State", value_name="Value"),
        r="Value", theta="index", color="State",
        line_close=True, title="State-wise Normalized Indicator Comparison"
    )
    fig_radar.update_traces(fill='toself')
    st.plotly_chart(fig_radar)
else:
    st.info("Please select at least one state to view comparison.")

