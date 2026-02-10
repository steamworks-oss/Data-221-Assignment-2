from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

# scrape the wikipedia entry using BeautifulSoup
url = "https://en.wikipedia.org/wiki/Machine_learning"
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html.raise_for_status()
soup = BeautifulSoup(html.text, "html.parser")

# extract tables from main text
content = soup.find("div", id="mw-content-text")
tables = content.find_all("table")

# get first table with at least three rows
tabularData = None
for table in tables:
    try:
        data = pd.read_html(StringIO(str(table)), flavor="lxml")[0]
    except ValueError:
        continue

    if len(data) >= 3:
        tabularData = data
        break

# if table headers aren't present, then give default headers
if tabularData.columns.isnull().any():
    tabularData.columns = [f"col{i+1}" for i in range(len(tabularData.columns))]

# pad missing row values with default value
tabularData = tabularData.fillna("")

# save extracted data to a csv
tabularData.to_csv("wiki_table.csv")