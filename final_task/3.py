import requests
from bs4 import BeautifulSoup
import csv
import time

# URL of the page to scrape
url = 'https://www.bbc.com/news/articles/cw448x7lxggo'

# Fetch the content from URL
response = requests.get(url)
html = response.content

# Parse HTML content
soup = BeautifulSoup(html, 'html.parser')

filename = "headlinesfinal.csv" 
# Create a CSV file and write the data
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'URL'])
    # Extract Headlines
    headlines = soup.find_all('h2')
    # Extract headlines text and URL
    for headline in headlines:
        headline_text = headline.text.strip()
        parent = headline
        while parent.name != 'body':
            parent = parent.parent
            link = parent.find('a',href=True)
            if(link):
                headline_url = link['href']
                if headline_url.startswith('https://www.bbc.com'):
                    break
                else:
                    headline_url = 'https://www.bbc.com' + headline_url
                    break

        writer.writerow([headline_text, headline_url])

print('Data scraping complete and saved to headlines.csv')

