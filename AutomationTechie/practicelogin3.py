
#edgedriver path unspecified, driver is part of python scripts
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

act_title=driver.title
exp_title="Logged In Successfully | Practice Test Automation"

if act_title==exp_title:
    print("Login Test passed")
else:
    print("Login Test failed")

driver.close()

