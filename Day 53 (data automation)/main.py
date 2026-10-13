import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
load_dotenv

# SHEET_URL = os.getenv(SHEET_URL)

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
for price in soup.select(".StyledPropertyCardDataArea-fDSTNn"):
    price_text = price.get_text().split("+")[0].replace('\n', '')
    prices.append(price_text.split("/")[0])
print(prices)

addresses = []
for address in soup.select("address"):
    addresses.append(address.text.replace("\n", "").replace("|", "").strip())
# print(addresses)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/viewform?bc=transparent&embedded=true&f=%2522Verdana%2522%252C%2522Helvetica%2522%252C%2522Arial%2522%252C%2Bsans-serif&hl=en&htc=%2523666666&id=1RPP4xUhAQOwAqld2MwXgcx5Ml5tTYt1GwmMSAZgcFL0&lc=%25230000cc&pli=1&tc=%2523000000&ttl=0")

input_fields = driver.find_elements(By.CSS_SELECTOR, ".Qr7Oae input")

for price in prices:
    print(f"price: {price}")
    input_fields[0].send_keys("price")
    input_fields[1].send_keys(addresses[prices.index(price)])
    input_fields[2].send_keys(links[prices.index(price)])
    break