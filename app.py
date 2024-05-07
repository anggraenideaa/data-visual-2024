import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# reading the database
url = "https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv"
data = pd.read_csv(url)

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()
