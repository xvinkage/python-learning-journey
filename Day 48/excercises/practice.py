from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Amazon-Basics-Anticavity-Mouthwash-Refreshing/dp/B09HHC4LG7/?_encoding=UTF8&pd_rd_w=splGj&content-id=amzn1.sym.ecd64fc4-ca41-43f6-b8be-57c22090b385&pf_rd_p=ecd64fc4-ca41-43f6-b8be-57c22090b385&pf_rd_r=EWCJPMY39PCPWX6R62CM&pd_rd_wg=ZIKUL&pd_rd_r=e7a301aa-5734-456a-914b-b043fb7d0f97&ref_=pd_hp_d_r_btf_dealz_dotda_t1&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"{price_dollar.text}.{price_cents.text}")

driver.quit()
