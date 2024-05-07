
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

