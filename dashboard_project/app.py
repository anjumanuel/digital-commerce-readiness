import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Digital Commerce Readiness Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/digital_readiness_master.csv")

st.title("\U0001F4C8 Digital Commerce Readiness Dashboard")
st.markdown("Analyze normalized metrics across states related to digital access, financial inclusion, education, and entrepreneurship.")

st.sidebar.header("Select chart to view")
option = st.sidebar.selectbox("Chart Options", (
    "Broadband Penetration (Urban vs Rural)",
    "Financial Inclusion Scatter",
    "Literacy vs MSMEs",
    "Enrollment vs Startups",
    "Startups vs MSMEs",
    "Urban Share vs Digital Indicators",
    "Bar Chart of Key Metrics by State"
))

# Chart 1: Urban vs Rural Broadband Access
if option == "Broadband Penetration (Urban vs Rural)":
    fig = px.bar(df, x='state_name', y=['broadband_rural', 'broadband_urban'], 
                 barmode='group', title="Urban vs Rural Broadband Access by State")
    st.plotly_chart(fig, use_container_width=True)

# Chart 2: Financial Inclusion Scatter Plot
elif option == "Financial Inclusion Scatter":
    fig = px.scatter(df, x='pmjdy_accounts_per_1000_pop', y='rupay_cards_per_account',
                     size='avg_balance_per_account', color='state_name',
                     title="PMJDY vs RuPay Usage vs Average Account Balance",
                     labels={"pmjdy_accounts_per_1000_pop": "PMJDY Accounts per 1000",
                             "rupay_cards_per_account": "RuPay Cards per Account"})
    st.plotly_chart(fig, use_container_width=True)

# Chart 3: Literacy vs MSMEs
elif option == "Literacy vs MSMEs":
    fig = px.scatter(df, x='literacy_rate', y='msmes_per_1000_pop', color='state_name',
                     title="Literacy Rate vs MSMEs per 1000 Population")
    st.plotly_chart(fig, use_container_width=True)

# Chart 4: Enrollment vs Startups
elif option == "Enrollment vs Startups":
    fig = px.scatter(df, x='enrollment_per_1000_HH', y='total_startups', color='state_name',
                     size='population', title="Enrollment vs Total Startups")
    st.plotly_chart(fig, use_container_width=True)

# Chart 5: Startups vs MSMEs
elif option == "Startups vs MSMEs":
    fig = px.scatter(df, x='msmes_per_1000_pop', y='total_startups', color='urban_share',
                     title="MSMEs vs Startups with Urban Share as Color")
    st.plotly_chart(fig, use_container_width=True)

# Chart 6: Urban Share vs Digital Metrics
elif option == "Urban Share vs Digital Indicators":
    fig = px.scatter(df, x='urban_share', y='broadband_urban', color='state_name',
                     title="Urban Share vs Urban Broadband Access")
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.scatter(df, x='urban_share', y='total_startups', color='state_name',
                     title="Urban Share vs Startups")
    st.plotly_chart(fig2, use_container_width=True)

# Chart 7: Bar Chart for selected metrics
elif option == "Bar Chart of Key Metrics by State":
    st.markdown("### Compare states on key normalized indicators")
    metrics = ['literacy_rate', 'enrollment_per_1000_HH', 'total_startups', 'msmes_per_1000_pop']
    selected_metric = st.selectbox("Select metric to visualize", metrics)
    fig = px.bar(df.sort_values(by=selected_metric, ascending=False),
                 x='state_name', y=selected_metric, title=f"States ranked by {selected_metric}")
    st.plotly_chart(fig, use_container_width=True)
