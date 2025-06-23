
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tech Stack Evolution on Kaggle", layout="wide")

st.title("Tech Stack Evolution Dashboard")
st.markdown("Explore how machine learning, deep learning, and other tech stacks evolved in Kaggle notebooks from 2015 to 2024 using Meta Kaggle data.")

# Load data
@st.cache_data
def load_data():
    notebooks = pd.read_csv("day3_notebooks_with_stack.csv")
    trends = pd.read_csv("day3_stack_trends.csv")
    return notebooks, trends

notebooks, trends = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
year_range = st.sidebar.slider("Select Year Range", 2015, 2024, (2017, 2024))
selected_stacks = st.sidebar.multiselect("Select Stack Categories",
                                         notebooks['StackCategory'].unique().tolist(),
                                         default=notebooks['StackCategory'].unique().tolist())

# Day 1 – Dataset Overview
st.header("Dataset Overview")
st.markdown("""
- **Datasets Used**: Kernels.csv, KernelVersions.csv, Tags.csv, KernelTags.csv
- Merged to create a timeline of notebook creation and associated tags.
""")
st.dataframe(notebooks.head())

# Day 2 – Tech Trends
st.header("Tech Stack Trends Over Time")
filtered_trends = trends[(trends['Year'] >= year_range[0]) & (trends['Year'] <= year_range[1])]
fig_trends = px.line(filtered_trends[filtered_trends['StackCategory'].isin(selected_stacks)],
                     x="Year", y="Count", color="StackCategory",
                     title="Year-wise Evolution of Stack Usage", markers=True)
st.plotly_chart(fig_trends, use_container_width=True)

# Day 3 – Stack Categorization
st.header("Stack Categorization & Distribution")
stack_count = notebooks[notebooks['StackCategory'].isin(selected_stacks)]['StackCategory'].value_counts().reset_index()
stack_count.columns = ['StackCategory', 'Count']
fig_stack = px.bar(stack_count, x='StackCategory', y='Count',
                   color='StackCategory', title="Distribution of Notebooks by Stack")
st.plotly_chart(fig_stack, use_container_width=True)

# Optional: Author Analysis
st.subheader("🏆 Top Authors in Each Stack Category")
if 'AuthorUserId' in notebooks.columns:
    top_authors = notebooks.groupby(['AuthorUserId', 'StackCategory']).size().reset_index(name='Count')
    top_authors = top_authors.sort_values(['StackCategory', 'Count'], ascending=[True, False])
    for cat in selected_stacks:
        st.markdown(f"#### 🔹 {cat}")
        st.dataframe(top_authors[top_authors['StackCategory'] == cat].head(5))
else:
    st.info("AuthorUserId column not found in dataset.")

# Day 4 – Final Summary
st.header("Insights & Summary")
st.markdown("""
### 📌 Final Takeaways:
- **Deep Learning** has seen a significant rise post-2020.
- **EDA tools** are consistently used across most stacks.
- **R-based** notebooks are declining steadily.
- Kaggle’s ecosystem reflects the real-world shift toward DL and Python.
""")
