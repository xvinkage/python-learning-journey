from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized") 


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.CSS_SELECTOR, "#mwDw")
# independece = driver.find_element(By.LINK_TEXT, "Independence Day")

search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)

print(articles.text)
# articles.click()

# driver.quit()