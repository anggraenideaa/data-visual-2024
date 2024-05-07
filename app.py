import pandas as pd
import matplotlib.pyplot as plt

# Reading the database
data = pd.read_csv("https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv")

# printing the top 10 rows
display(data.head(10))
