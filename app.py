import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.figure_factory as ff


# Menampilkan teks statis
st.subheader("Visualisasi Data dengan data Tips.csv")
st.subheader("")

#VISUALISASI 1
# reading the database
data = pd.read_csv("https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv")

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(data['day'], data['tip'])

# Adding Title to the Plot
ax.set_title("Scatter Plot")

# Setting the X and Y labels
ax.set_xlabel('Day')
ax.set_ylabel('Tip')

# Display the plot in Streamlit
st.pyplot(fig)

#VISUALISASI 2
# Create a line chart using Streamlit
st.line_chart(data[['tip', 'size']])

# Adding Title to the Plot
plt.title("Line Chart")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# plt.show()  # Not needed in Streamlit

#VISUALISASI 3

data = pd.read_csv("tips.csv")
fig = px.scatter(
    data,
    x="day",
    y="tip",
    color="size",
    size="total_bill",
    color_continuous_scale="reds",
)

tab1, tab2 = st.columns(2)
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


#Visualisasi 4

# Generate random data
arr = np.random.normal(1, 1, size=100)

# Create a histogram using Matplotlib
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

# Display the histogram using Streamlit
st.pyplot(fig)


#Visual 5
# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

