import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.figure_factory as ff


# Menampilkan teks statis
st.subheader("Visualisasi Data dengan data Tips.csv")
st.subheader("")
st.text("Nama : Dea Puspita Anggraeni")
st.text("NPM : 21082020029")

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
# Create scatter plot using Plotly Express
fig = px.scatter(
    data,
    x="day",
    y="tip",
    color="size",
    size="total_bill",
    color_continuous_scale="reds",
)

# Display the plot using Streamlit in one tab
with st.expander("Plotly Chart", expanded=True):
    # Use the Streamlit theme (default).
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
# Load sample dataset from Plotly Express
df = px.data.gapminder()

# Create scatter plot using Plotly Express
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

# Display the plot using Streamlit in one tab
with st.expander("Plotly Chart", expanded=True):
    # Use the Streamlit theme (default).
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)



