import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_tables(url):
    # Fetch the HTML of the website
    response = requests.get(url)
    html = response.text

    # Use Beautiful Soup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find all table elements in the HTML
    tables = soup.find_all('table')

    # Convert the tables to a list of DataFrames
    dataframes = []
    for table in tables:
        df = pd.read_html(str(table))[0]
        dataframes.append(df)

    return dataframes


st.title('Table Scraper')

# Create a text input for the user to enter the URL
url = st.text_input('Enter the URL of the website:')

# Create a button to start the scraping process
if st.button('Scrape Tables'):
    tables = scrape_tables(url)
    st.success('Scraping complete!')

    # Loop through the tables and display them on the page
    for table in tables:
        st.markdown(table, unsafe_allow_html=True)

