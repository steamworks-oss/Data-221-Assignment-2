from bs4 import BeautifulSoup
import requests

# scrape the wikipedia entry using BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"
html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html.raise_for_status()
soup = BeautifulSoup(html.text, "html.parser")

# extract and print title
title = soup.title
print(f"Page title: {title.string}")

# extract paragraphs from main text
content = soup.find('div', id='mw-content-text')
paragraphs = content.find_all('p')

# print the first paragraph with at least 50 characters
for paragraph in paragraphs:
    text = paragraph.get_text().strip()
    if len(text) >= 50:
        print(f"First Paragraph with at least 50 characters:\n{text}")
        break