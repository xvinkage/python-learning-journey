import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time

load_dotenv()

SHEET_URL = os.getenv("SHEET_URL")

zillow = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(zillow)
content = response.content

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify)

links = []
for link in soup.select(".StyledPropertyCardPhotoBody a"):
    listing_link = link.get("href")
    # print(link)
    links.append(listing_link)
print(links)

prices = []
for price in soup.select(".StyledPropertyCardDataArea-fDSTNn"):
    price_text = price.get_text().split("+")[0].replace('\n', '')
    prices.append(price_text.split("/")[0])
# print(prices)

addresses = []
for address in soup.select("address"):
    addresses.append(address.text.replace("\n", "").replace("|", "").strip())
# print(addresses)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(SHEET_URL)


for index, price in enumerate(prices):
    attempts = 0
    while attempts < 3:
    # print(f"price: {price}")
        try:
            input_fields = driver.find_elements(By.CSS_SELECTOR, ".Qr7Oae input")
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Qr7Oae input")))

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Qr7Oae input")))

            input_fields[0].send_keys(price)
            input_fields[1].send_keys(addresses[index])
            input_fields[2].send_keys(links[index])

            driver.find_element(By.CSS_SELECTOR, ".NPEfkd").click()
            driver.find_element(By.CSS_SELECTOR, "a").click()
            break
        except StaleElementReferenceException:
            attempts += 1
            time.sleep(0.5)  # Brief pause to let the DOM finish updating
            continue