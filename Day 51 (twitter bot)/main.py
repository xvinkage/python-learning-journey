from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
from selenium_stealth import stealth

load_dotenv()

URL = "https://www.x.com/"
SPEED_URL = "https://www.speedtest.net/"

PROMISED_DOWN = 1000
PROMISED_UP = 1000
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Edge(options=options) 


        # stealth(
        #     self.driver,
        #     languages=["en-US", "en"],
        #     vendor="Google Inc.",
        #     platform="Win32",
        #     webgl_vendor="Intel Inc.",
        #     renderer="Intel Iris OpenGL Engine",
        #     fix_hairline=True,
        # )       
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        
        self.driver.get(SPEED_URL)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')))
        button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')
        button.click()
        print("waiting")
        time.sleep(45)
        print("wait complete")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/button')))

        exit = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/button')
        exit.click()
        print("finished clicking")

        self.up = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3')
        self.down = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/h3')
        return self.up.text, self.down.text


    def tweet_at_provider(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(options=chrome_options) 
        stealth(
            self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )   

        self.driver.get(URL)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))
        login = self.driver.find_element(By.CSS_SELECTOR, "input")
        login.send_keys(TWITTER_EMAIL)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
        continue_login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/form/button/div')
        continue_login.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "jf-input-password")))
        password_input = self.driver.find_element(By.ID, "jf-input-password")
        password_input.send_keys(TWITTER_PASSWORD)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_r_5_"]/div/div/div[1]/form/div[2]/div/button/div')))
        submit_login = self.driver.find_element(By.XPATH, '//*[@id="_r_5_"]/div/div/div[1]/form/div[2]/div/button/div')
        submit_login.click()

        #we are only drafting the post, we do not want to actually send to our ISP
        draft_post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div')
        tweet = f"Hey provider why is my internet {self.down.text}down/{self.up.text}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        draft_post.send_keys(tweet)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_DOWN:
    bot.tweet_at_provider()


