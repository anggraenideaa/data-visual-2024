
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Menampilkan teks statis
st.text("Visualisasi Data dengan data Tips.csv")

# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv")

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()

