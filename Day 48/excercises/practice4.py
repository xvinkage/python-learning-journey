from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome__options = webdriver.ChromeOptions()
chrome__options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome__options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("xvinkage")
last_name.send_keys("streamer")
email.send_keys("xvinkage@email.com")

button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()
