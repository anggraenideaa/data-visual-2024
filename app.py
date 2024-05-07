import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Menampilkan teks statis
st.markdown("<h3>Visualisasi Data dengan data Tips.csv</h3>", unsafe_allow_html=True)

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

#VISUALISASI 2
st.subheader("Define a custom colorscale")
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
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)

#Visualisasi 3
# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'], c=data['size'], 
			s=data['total_bill'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar()

plt.show()


# # reading the database
# data = pd.read_csv("https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv")

# # Scatter plot with day against tip
# plt.scatter(data['day'], data['tip'])

# # Adding Title to the Plot
# plt.title("Scatter Plot")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# plt.show()

