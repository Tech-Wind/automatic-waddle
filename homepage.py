import streamlit as st
import pandas as pd

# Allow the user to upload a file
uploaded_file = st.file_uploader("Choose a CSV file:")

# Read the CSV file into a dataframe
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.dataframe(df)