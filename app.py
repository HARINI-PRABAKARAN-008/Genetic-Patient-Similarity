import streamlit as st
import pandas as pd

st.set_page_config(page_title="Genetic Patient Similarity", layout="wide")

st.title("Genetic Patient Similarity Analysis")
st.write("Patient Clustering Dashboard")

df = pd.read_csv("/content/genetic_cluster_results.csv")

st.subheader("Clustering Results")
st.dataframe(df, use_container_width=True)

cluster_col = next(
    (c for c in df.columns if "cluster" in c.lower()),
    None
)

if cluster_col:
    st.subheader("Patients in Each Cluster")
    st.bar_chart(df[cluster_col].value_counts())

st.success("Dashboard loaded successfully!")
