from bs4 import BeautifulSoup
import requests

# scrape the wikipedia entry using BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"
html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html.raise_for_status()
soup = BeautifulSoup(html.text, "html.parser")

# extract <h2> section headings from main text
content = soup.find('div', id='mw-content-text')
headings = content.find_all('h2')

# remove headings containing certain words/phrases
excludedWords = ["References", "External links", "See also", "Notes"]
headings = [heading for heading in headings if all(word not in heading for word in excludedWords)]
#headings = filter(lambda heading: all(word not in heading for word in excludedWords), headings)

# remove "[edit]" from filtered headings
headings = [heading.string.replace("[edit]", "") for heading in headings]

# save resulting headings to a file
with open("headings.txt", "w") as file:
    for heading in headings:
        file.write(heading + "\n")
