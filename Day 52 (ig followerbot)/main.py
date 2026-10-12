import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

load_dotenv()


SIMILAR_ACCOUNT= "rordongamsay"
USERNAME = os.getenv("USERNAME")     # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = os.getenv("PASSWORD") 
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollower():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        driver = self.driver

        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.NAME, "username")))

        driver.find_element(By.NAME, "username").send_keys(USERNAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.CLASS_NAME, "naan-btn-primary").click()
        #cookies
        driver.find_element(By.CLASS_NAME, "naan-popup-dismiss").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popup-notifications"]/div/button[2]')))
        driver.find_element(By.XPATH, '//*[@id="popup-notifications"]/div/button[2]').click()
        #search for similar account
        driver.find_element(By.CSS_SELECTOR, ".naan-rail-item").click()
        driver.find_element(By.CSS_SELECTOR , "input").send_keys(SIMILAR_ACCOUNT)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".naan-search-row")))
        driver.find_element(By.CSS_SELECTOR , ".naan-search-row").click()

    def find_followers(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, ".naan-followers-link").click()

        #locate the followers list
        wait = WebDriverWait(driver, 10)
        modal = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")
        for _ in range(10):
            # "scroll this element to the bottom" → loads the next batch of followers
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):
        driver = self.driver
        all_buttons = driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            if button.text == "Follow":
                time.sleep(1)
                button.click()
            else:
                print("Already following this user.")
        
            

insta = InstaFollower()

insta.login()
insta.find_followers()
insta.follow()