import requests
from bs4 import BeautifulSoup

zillow = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(zillow)
content = response.content

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify)

links = []
for link in soup.select("ul .List-c11n-8-84-3-photo-cards a"):
    listing_link = link.get("href")
    links.append(listing_link)
# print(links)
prices = []

addresses = []