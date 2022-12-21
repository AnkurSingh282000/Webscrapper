import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_data(url):
  # Make a request to the URL
  page = requests.get(url)
  # Parse the HTML content
  soup = BeautifulSoup(page.content, 'html.parser')
  # Find all the tables in the HTML content
  tables = soup.find_all('table')
  # Create an empty list to store the data
  data = []
  # Loop through all the tables
  for table in tables:
    # Extract the data from each table and store it in a list
    table_data = []
    for row in table.find_all('tr'):
      row_data = []
      for cell in row.find_all('td'):
        row_data.append(cell.text)
      table_data.append(row_data)
    # Add the table data to the list
    data.append(table_data)
  return data

st.title('Table Scraper')

# Get the URL from the user
url = st.text_input('Enter the URL:')

# Scrape the data from the URL
data = scrape_data(url)

# Display the data in a table
st.header('Tables')
for i, table in enumerate(data):
  st.table(pd.DataFrame(table))
  st.markdown(f'<a href="#table{i+1}">View table {i+1}</a>', unsafe_allow_html=True)

# Allow the user to select a table
table_index = st.selectbox('Select a table:', range(len(data)))

# Display the selected table
st.header(f'Table {table_index+1}')
st.table(pd.DataFrame(data[table_index]))

# Allow the user to select columns for visualization
columns = st.multiselect('Select columns for visualization:', data[table_index][0])

# Create a plot using the selected columns
st.line_chart(pd.DataFrame(data[table_index][1:], columns=data[table_index][0])[columns])

# Create a plot using the selected columns
st.line_chart(pd.DataFrame(data[table_index][1:], columns=data[table_index][0])[columns])
