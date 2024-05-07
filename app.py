
import streamlit as st
import pandas as pd

# Reading the database
data = pd.read_csv("https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv")


# printing the top 10 rows
st.dataframe(data.head(10))
