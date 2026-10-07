from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

URL = "https://app.100daysofpython.dev/services/tindog/u/nXx91gpW_k8f5AOC33iJJ75ejuI7O8u-"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

base_window = driver.window_handles[0]
print(base_window)
sign_in = driver.find_element(By.CSS_SELECTOR, "button")
sign_in.click()

print(driver.title)

WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-facebark')))
facebark = driver.find_element(By.CLASS_NAME, 'btn-facebark')
facebark.click()


login_window = driver.window_handles[1]
driver.switch_to.window(login_window)


WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, 'email')))
email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)

login = driver.find_element(By.CSS_SELECTOR, "button")
login.click()

driver.switch_to.window(base_window)
allow_button = driver.find_element(By.CSS_SELECTOR, "button")
allow_button.click()

notification_button = driver.find_element(By.CLASS_NAME, "btn-secondary")
notification_button.click()

cookies_button = driver.find_element(By.CLASS_NAME, "btn-primary")
cookies_button.click()

WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-like')))

n = 0

while n < 20:
    try:
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-like')))
        like = driver.find_element(By.CLASS_NAME, "btn-like")
        like.click()
        n += 1

    except ElementClickInterceptedException:
        popup = driver.find_element(By.CLASS_NAME, "match-popup-link")
        popup.click()

driver.quit()