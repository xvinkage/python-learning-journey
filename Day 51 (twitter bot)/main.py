from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import undetected_chromedriver as uc

URL = "https://www.x.com/"
SPEED_URL = "https://www.speedtest.net/"

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)        
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')))
        button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')
        button.click()
        self.driver.implicitly_wait(60)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/h3')
        self.down = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3')
        print(self.up.text, self.down.text)

    def tweet_at_provider(self):
        self.driver.get(URL)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# bot.tweet_at_provider()


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(URL)

# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))
# login = driver.find_element(By.CSS_SELECTOR, "input")

# login.send_keys("username")