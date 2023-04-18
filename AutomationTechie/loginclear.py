from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

driver.find_element(By.XPATH, """//*[@id="Email"]""").clear()
driver.find_element(By.XPATH, """//*[@id="Email"]""").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"""//*[@id="Password"]""").clear()
driver.find_element(By.XPATH,"""//*[@id="Password"]""").send_keys("admin")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"

if act_title==exp_title:
    print("Test Succcesful")
else:
    print("Test failed")

driver.close()


