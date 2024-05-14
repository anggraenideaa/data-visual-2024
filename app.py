import streamlit as st
import pandas as pd
import numpy as np
import os

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)



# Initialize connection.
# conn = st.connection('mysql', type='sql', username=st.secrets["DB_USER"], password=st.secrets["DB_PASS"], host=st.secrets["HOST"], database=st.secrets["DB"])
# conn = st.connection(**st.secrets.db_credentials)
conn = st.connection("mydb", type="sql", autocommit=True)

# Perform query.
df = conn.query('SELECT EnglishPromotionName, StartDate, EndDate, MaxQty from dimpromotion limit 10;', ttl=600)

st.table(df)
# Print results.
# for row in df.itertuples():
#     st.write(f"{row.EnglishPromotionName} , {row.MaxQty} ")


#import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px
# import numpy as np
# import plotly.figure_factory as ff


# # Menampilkan teks statis
# st.subheader("Visualisasi Data dengan data Tips.csv")
# st.subheader("")
# st.write("Nama : Dea Puspita Anggraeni")
# st.write("NPM : 21082020029")

# #VISUALISASI 1
# # reading the database
# data = pd.read_csv("https://raw.githubusercontent.com/anggraenideaa/data-visual-2024/master/tips.csv")

# # Create a scatter plot
# fig, ax = plt.subplots()
# ax.scatter(data['day'], data['tip'])

# # Adding Title to the Plot
# ax.set_title("Scatter Plot")

# # Setting the X and Y labels
# ax.set_xlabel('Day')
# ax.set_ylabel('Tip')

# # Display the plot in Streamlit
# st.pyplot(fig)

# #VISUALISASI 2
# # Create a line chart using Streamlit
# st.line_chart(data[['tip', 'size']])

# # Adding Title to the Plot
# plt.title("Line Chart")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# # plt.show()  # Not needed in Streamlit

# #VISUALISASI 3
# # Create scatter plot using Plotly Express
# fig = px.scatter(
#     data,
#     x="day",
#     y="tip",
#     color="size",
#     size="total_bill",
#     color_continuous_scale="reds",
# )

# # Display the plot using Streamlit in one tab
# with st.expander("Plotly Chart", expanded=True):
#     # Use the Streamlit theme (default).
#     st.plotly_chart(fig, theme="streamlit", use_container_width=True)




# #Visualisasi 4
# # Select the data for each group
# male_data = data[data['sex'] == 'Male']['total_bill']
# female_data = data[data['sex'] == 'Female']['total_bill']

# # Create a figure using Plotly Express
# fig = px.histogram(data, x='total_bill', color='sex', marginal='rug')

# # Plot!
# st.plotly_chart(fig, use_container_width=True)

# # #Visual 5
# # # Load sample dataset from Plotly Express
# # df = px.data.gapminder()

# # # Create scatter plot using Plotly Express
# # fig = px.scatter(
# #     df.query("year==2007"),
# #     x="gdpPercap",
# #     y="lifeExp",
# #     size="pop",
# #     color="continent",
# #     hover_name="country",
# #     log_x=True,
# #     size_max=60,
# # )

# # # Display the plot using Streamlit in one tab
# # with st.expander("Plotly Chart", expanded=True):
# #     # Use the Streamlit theme (default).
# #     st.plotly_chart(fig, theme="streamlit", use_container_width=True)

