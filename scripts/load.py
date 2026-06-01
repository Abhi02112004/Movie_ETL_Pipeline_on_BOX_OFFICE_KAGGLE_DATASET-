import os
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Movie Box Office Dashboard",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    current_dir = os.path.dirname(__file__)   
    file_path = os.path.join(current_dir, "..", "data", "cleaned_box_office_dataset.csv")
    file_path = os.path.abspath(file_path)

    df = pd.read_csv(file_path)
    return df

df = load_data()