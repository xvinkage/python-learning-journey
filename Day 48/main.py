from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(2)


lang = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
lang.click()

time.sleep(2)
cookie = driver. find_element(By.CSS_SELECTOR, "button")

wait_time = 5
timeout = time.time() + wait_time
countdown = time.time() + 300

while time.time() < countdown:
    cookie.click()

    cookie_count = driver.find_element(By.CSS_SELECTOR, "#cookies").text
    cookies = int(cookie_count.split(" ")[0].replace(",", ""))
    # print(cookie_count)

    if time.time() > timeout:
        upgrades = {}
        stuff = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        for items in stuff:
            price = int(items.text.split("\n")[1].replace(",", ""))
            # upgrades.append(int(price))
            
            if price <= cookies:
                upgrades[price] = items

        # print(max(upgrades))
        timeout = time.time() + wait_time

        if upgrades:
            max_upgrade = upgrades[max(upgrades)]
            max_upgrade.click()
        else:
            continue
print(cookie_count.split(": ")[1])

driver.quit()


