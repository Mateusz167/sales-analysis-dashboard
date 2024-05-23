# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V5cgHeqUTDlzCpZ95zWfpTRSzUpKotCB
"""

# import of modules used during work and creation of a data frame from available data
import pandas

data = pandas.read_csv('Sales_data.csv', sep=';')

data_to_use = pandas.DataFrame(data)
print(data)

# Display data framve overview
# First five rows
print(data_to_use.head())
# Summary statistics for numerical columns
print(data_to_use.describe())
# DataFrame structure, non-null counts, and data types
print(data_to_use.info())

#counting blank values
missing_values_per_column = data_to_use.isnull().sum()
print(missing_values_per_column)

# Checing if there are duplicates apears in the data set
print(data_to_use.duplicated().sum())

# #Remove duplicates
# data_to_use = data_to_use.drop_duplicates() there are no duplicates in data set

# Transforming quantitative data to float type
# Replace commas with periods in 'UnitPrice' and 'TotalPrice' columns
data_to_use['UnitPrice'] = data_to_use['UnitPrice'].astype(str).str.replace(',', '.')
data_to_use['TotalPrice'] = data_to_use['TotalPrice'].astype(str).str.replace(',', '.')

# Convert 'Quantity', 'UnitPrice', and 'TotalPrice' columns to float
data_to_use['Quantity'] = data_to_use['Quantity'].astype(float)
data_to_use['UnitPrice'] = data_to_use['UnitPrice'].astype(float)
data_to_use['TotalPrice'] = data_to_use['TotalPrice'].astype(float)

# Display updated data types
print(data_to_use.dtypes)

# Data cleaning
data_to_use['OrderDate'] = pandas.to_datetime(data_to_use['OrderDate'])
data_to_use['Month'] = data_to_use['OrderDate'].dt.to_period('M')
data_to_use['Year'] = data_to_use['OrderDate'].dt.to_period('Y')

# Convert 'Month' to month names
data_to_use['Month'] = data_to_use['Month'].dt.strftime('%B')

# Normalizing location data
data_to_use['City'] = data_to_use['City'].str.strip().str.title()
data_to_use['Country'] = data_to_use['Country'].str.strip().str.title()

# Grouping by year and month
time_grouped = data_to_use.groupby(['Year', 'Month']).agg({
    'OrderID': 'count',  # Number of orders
    'TotalPrice': 'sum',  # Total sales
    'Quantity': 'sum'     # Total quantity sold
}).reset_index()

# Grouping by country and city
geographic_grouped = data_to_use.groupby(["Country", "City"]).agg({
    'OrderID': 'count',  # Number of orders
    'TotalPrice': 'sum',  # Total sales
    'Quantity': 'sum'     # Total quantity sold
}).reset_index()

# Grouping by product name
product_grouped = data_to_use.groupby(["ProductName"]).agg({
    'OrderID': 'count',  # Number of orders
    'TotalPrice': 'sum',  # Total sales
    'Quantity': 'sum'     # Total quantity sold
}).reset_index()

# Grouping by customer name
customer_grouped = data_to_use.groupby(["CompanyName"]).agg({
    'OrderID': 'count',  # Number of orders
    'TotalPrice': 'sum',  # Total sales
    'Quantity': 'sum'     # Total quantity sold
})

# Saving grouped data into csv files
time_grouped.to_csv("time_analysis.csv", index=False)
geographic_grouped.to_csv("geographic_analysis.csv",index=False)
product_grouped.to_csv("product_analysis.csv",index=False)
customer_grouped.to_csv("customer_analysis.csv",index=False)