import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Lead Scoring Agent", layout="wide")

st.title("My Lead Scoring Agent – 3D In-Vitro Models")

# Check if output file exists
if not os.path.exists("lead_output.csv"):
    st.error("❌ lead_output.csv not found. Please run generate_leads.py first.")
    st.stop()

# Load data
df = pd.read_csv("lead_output.csv")

st.subheader(" :) Scored & Ranked Leads")

# Search box
search = st.text_input("Search by name, title, company, or location")

if search:
    df = df[df.apply(
        lambda row: search.lower() in row.astype(str).str.lower().to_string(),
        axis=1
    )]

st.dataframe(df, use_container_width=True)

st.caption("Data generated via Lead Scoring Pipeline (Identification → Enrichment → Scoring)")
