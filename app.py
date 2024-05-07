import pandas as pd
import matplotlib.pyplot as plt

# Reading the database
data = pd.read_csv("https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv")

# Create a figure and axis objects
fig, ax = plt.subplots()

# Scatter plot with size against tip
ax.scatter(data['size'], data['tip'])

# Adding Title to the Plot
ax.set_title("Scatter Plot")

# Setting the X and Y labels
ax.set_xlabel('Size')
ax.set_ylabel('Tip')

# Show the plot
plt.show()
