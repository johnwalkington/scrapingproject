# This scraper will take a geographic area and scrape all craigslist data #

from requests import get
from bs4 import BeautifulSoup

response = get('https://austin.craigslist.org/')

html_soup = BeautifulSoup(response.text, 'html.parser')

print(html_soup)