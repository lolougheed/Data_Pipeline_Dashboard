import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Page config
st.set_page_config(page_title="Furniture Store Profitability Dashboard", layout="wide")

# Load cleaned data
@st.cache_data
def load_data():
    df = pd.read_parquet(Path("data/processed/cleaned_sales.parquet"))
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    
    # Create 'month' column for time-based grouping
    df['month'] = df['order_date'].dt.to_period('M').dt.to_timestamp()
    
    return df
df = load_data()

# Title and description
st.title("Furniture Store Profitability Dashboard")
st.markdown("""
Explore retail performance and trends across regions and sub-categories. 
Use the filters below to slice and compare data.
""")

# Sidebar filters
st.sidebar.header("Filter Data")
regions = ['All'] + sorted(df['region'].dropna().unique().tolist())
subcats = ['All'] + sorted(df['sub-category'].dropna().unique().tolist())
years = ['All'] + sorted(df['order_date'].dt.year.unique().astype(str).tolist())

selected_region = st.sidebar.selectbox("Select Region", options=regions)
selected_subcat = st.sidebar.selectbox("Select Sub-Category", options=subcats)
selected_year = st.sidebar.selectbox("Select Year", options=years)

# Filter logic
filtered = df.copy()
if selected_region != 'All':
    filtered = filtered[filtered['region'] == selected_region]
if selected_subcat != 'All':
    filtered = filtered[filtered['sub-category'] == selected_subcat]
if selected_year != 'All':
    filtered = filtered[filtered['order_date'].dt.year == int(selected_year)]

# KPI section
total_profit = filtered['profit'].sum()
total_sales = filtered['sales'].sum()
order_count = filtered['order_id'].nunique()

st.markdown("### Key Metrics")
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Profit", f"${total_profit:,.0f}")
kpi2.metric("Total Sales", f"${total_sales:,.0f}")
kpi3.metric("Unique Orders", f"{order_count}")

# Monthly Profit Chart
monthly = filtered.groupby('month')['profit'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly, x='month', y='profit', ax=ax, marker="o")
ax.set_title("Monthly Profit Trend")
ax.set_ylabel("Profit ($)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Profit by Sub-Category and Region
st.markdown("### Profit Breakdown")
col1, col2 = st.columns(2)

with col1:
    subcat_profit = df.groupby('sub-category')['profit'].sum().sort_values(ascending=False)
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.barplot(x=subcat_profit.values, y=subcat_profit.index, ax=ax1)
    ax1.set_title("Profit by Sub-Category")
    st.pyplot(fig1)

with col2:
    region_profit = df.groupby('region')['profit'].sum().sort_values(ascending=False)
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.barplot(x=region_profit.values, y=region_profit.index, ax=ax2, palette="coolwarm")
    ax2.set_title("Profit by Region")
    st.pyplot(fig2)

# Data download
st.markdown("### Download Filtered Data")
st.download_button("Download CSV", data=filtered.to_csv(index=False), file_name="filtered_data.csv")