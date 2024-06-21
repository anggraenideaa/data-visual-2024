import mysql.connector
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import toml

# Function to load database configuration from secrets.toml
def load_db_config():
    try:
        with open('.streamlit/secrets.toml', 'r') as f:
            config = toml.load(f)
        return config['database']
    except FileNotFoundError:
        st.error("File '.streamlit/secrets.toml' not found.")
        st.stop()
    except KeyError as e:
        st.error(f"KeyError: {e} not found in database configuration.")
        st.stop()

# Function to create a connection to the database
def create_connection():
    try:
        config = load_db_config()
        return mysql.connector.connect(
            host=config['DB_HOST'],
            user=config['DB_USER'],
            passwd=config['DB_PASS'],
            port=config['DB_PORT'],
            database=config['DB_NAME']
        )
    except mysql.connector.Error as e:
        st.error(f"MySQL connection error: {e}")
        st.stop()

# Function to fetch available countries
def fetch_countries():
    try:
        dataBase = create_connection()
        cursor = dataBase.cursor()

        cursor.execute("SELECT DISTINCT SalesTerritoryCountry FROM dimsalesterritory")
        countries = [row[0] for row in cursor.fetchall()]

        cursor.close()
        dataBase.close()

        return countries
    except mysql.connector.Error as e:
        st.error(f"MySQL error fetching countries: {e}")
        st.stop()

# Function to fetch data based on selected country
def fetch_data(country=None):
    try:
        dataBase = create_connection()
        cursor = dataBase.cursor()

        # Query to fetch data
        base_query = """
        SELECT dc.YearlyIncome, SUM(fis.SalesAmount) as TotalSales
        FROM factinternetsales fis
        JOIN dimcustomer dc ON fis.CustomerKey = dc.CustomerKey
        JOIN dimsalesterritory dst ON fis.SalesTerritoryKey = dst.SalesTerritoryKey
        {}
        GROUP BY dc.YearlyIncome
        """

        if country:
            query = base_query.format(f"WHERE dst.SalesTerritoryCountry = '{country}'")
        else:
            query = base_query.format("")

        cursor.execute(query)
        data = pd.DataFrame(cursor.fetchall(), columns=['YearlyIncome', 'TotalSales'])

        cursor.close()
        dataBase.close()

        return data
    except mysql.connector.Error as e:
        st.error(f"MySQL error fetching data: {e}")
        st.stop()

# Function to fetch sales data per product category by sales territory
def fetch_sales_data(country=None):
    try:
        dataBase = create_connection()
        cursor = dataBase.cursor()

        base_query = """
        SELECT dst.SalesTerritoryRegion, dpc.EnglishProductCategoryName, SUM(fis.SalesAmount) AS TotalSales
        FROM factinternetsales fis
        JOIN dimsalesterritory dst ON fis.SalesTerritoryKey = dst.SalesTerritoryKey
        JOIN dimproduct dp ON fis.ProductKey = dp.ProductKey
        JOIN dimproductsubcategory dps ON dp.ProductSubcategoryKey = dps.ProductSubcategoryKey
        JOIN dimproductcategory dpc ON dps.ProductCategoryKey = dpc.ProductCategoryKey
        {}
        GROUP BY dst.SalesTerritoryRegion, dpc.EnglishProductCategoryName;
        """
        
        if country:
            query = base_query.format(f"WHERE dst.SalesTerritoryCountry = '{country}'")
        else:
            query = base_query.format("")

        cursor.execute(query)
        data = pd.DataFrame(cursor.fetchall(), columns=['SalesTerritoryRegion', 'ProductCategory', 'TotalSales'])

        cursor.close()
        dataBase.close()
        
        return data
    except mysql.connector.Error as e:
        st.error(f"MySQL error fetching sales data: {e}")
        st.stop()

# Function to fetch and display treemap data
def fetch_treemap_data(country=None):
    try:
        dataBase = create_connection()
        cursor = dataBase.cursor()

        base_query = """
        SELECT dpc.EnglishProductCategoryName, SUM(fis.SalesAmount) AS TotalSales
        FROM factinternetsales fis
        JOIN dimproduct dp ON fis.ProductKey = dp.ProductKey
        JOIN dimproductsubcategory dps ON dp.ProductSubcategoryKey = dps.ProductSubcategoryKey
        JOIN dimproductcategory dpc ON dps.ProductCategoryKey = dpc.ProductCategoryKey
        {}
        GROUP BY dpc.EnglishProductCategoryName;
        """
        
        if country:
            query = base_query.format(f"WHERE EXISTS (SELECT 1 FROM dimsalesterritory dst WHERE fis.SalesTerritoryKey = dst.SalesTerritoryKey AND dst.SalesTerritoryCountry = '{country}')")
        else:
            query = base_query.format("")

        cursor.execute(query)
        data = pd.DataFrame(cursor.fetchall(), columns=['ProductCategory', 'TotalSales'])

        cursor.close()
        dataBase.close()
        
        return data
    except mysql.connector.Error as e:
        st.error(f"MySQL error fetching treemap data: {e}")
        st.stop()

# Function to fetch data for choropleth map
def fetch_choropleth_data(country=None):
    try:
        dataBase = create_connection()
        cursor = dataBase.cursor()

        base_query = """
        SELECT dst.SalesTerritoryRegion, SUM(fis.SalesAmount) AS TotalSales
        FROM factinternetsales fis
        JOIN dimsalesterritory dst ON fis.SalesTerritoryKey = dst.SalesTerritoryKey
        {}
        GROUP BY dst.SalesTerritoryRegion
        ORDER BY TotalSales DESC;
        """
        
        if country:
            query = base_query.format(f"WHERE dst.SalesTerritoryCountry = '{country}'")
        else:
            query = base_query.format("")

        cursor.execute(query)
        data = pd.DataFrame(cursor.fetchall(), columns=['SalesTerritoryRegion', 'TotalSales'])

        cursor.close()
        dataBase.close()
        
        return data
    except mysql.connector.Error as e:
        st.error(f"MySQL error fetching choropleth data: {e}")
        st.stop()

# Streamlit interface
st.set_page_config(layout="wide")
st.markdown('<h1 style="font-size:30px; text-align:center;">Dashboard Penjualan</h1>', unsafe_allow_html=True)

# Sidebar for selecting country
st.sidebar.title('📊 Dashboard Penjualan')
countries = fetch_countries()
selected_country = st.sidebar.selectbox('Pilih Negara', options=['All'] + countries)

# Fetch data based on selected country
data = fetch_data(country=None if selected_country == 'All' else selected_country)

# Convert columns to appropriate data types
data['YearlyIncome'] = data['YearlyIncome'].astype(float)
data['TotalSales'] = data['TotalSales'].astype(float)

# Layout of the dashboard
col1, col2 = st.columns((3, 3))

with col1:
    # Display scatter plot using Plotly
    st.markdown('<h2 style="font-size:20px; text-align:center;">Hubungan Antara Pendapatan Tahunan dan Total Penjualan</h2>', unsafe_allow_html=True)
    fig = px.scatter(data, x='YearlyIncome', y='TotalSales', color_discrete_sequence=["#543310"])
    st.plotly_chart(fig, use_container_width=True)

    # Fetch sales data based on selected country
    sales_data = fetch_sales_data(country=None if selected_country == 'All' else selected_country)

    # Pivot data for bar chart
    pivot_data = sales_data.pivot_table(index='SalesTerritoryRegion', columns='ProductCategory', values='TotalSales', fill_value=0).reset_index()

    # Display bar chart using Plotly
    st.markdown('<h2 style="font-size:20px; text-align:center;">Perbandingan Penjualan di Berbagai Region Untuk Berbagai Kategori Produk</h2>', unsafe_allow_html=True)
    fig = px.bar(pivot_data, x='SalesTerritoryRegion', y=pivot_data.columns[1:], color_discrete_sequence=["#543310", "#F8F4E1", "#AF8F6F"])
    st.plotly_chart(fig, use_container_width=True)

    # Fetch data for choropleth map
    choropleth_data = fetch_choropleth_data(country=None if selected_country == 'All' else selected_country)
    sales_territory_regions, total_sales = zip(*choropleth_data.values)
    

    st.markdown('<h2 style="font-size:20px; text-align:center;"></h2>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size:20px; text-align:center;"></h2>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size:20px; text-align:center;"></h2>', unsafe_allow_html=True)
    # Display choropleth map
    st.markdown('<h2 style="font-size:20px; text-align:center;">Penjualan Terdistribusi di Berbagai Wilayah Penjualan (SalesTerritoryregion)</h2>', unsafe_allow_html=True)
    fig = go.Figure(go.Choropleth(
        locations=sales_territory_regions,  # Menggunakan nama region sebagai locations
        z=total_sales,  # Menentukan nilai yang akan diplot sebagai warna
        locationmode='country names',  # Menggunakan mode nama negara
        colorscale=[[0,
