from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
# print(events.text)

event_list = {}


for index, event in enumerate(events):
    text_split = (event.text.split("\n"))
    event_list[index] = {"time": text_split[0], "event": text_split[1]}
    # print(event.text)
print(event_list)
driver.quit()