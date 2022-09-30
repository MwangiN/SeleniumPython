from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://github.com/login")

driver.find_element(By.ID, "login_field").send_keys("Optimusprime")
driver.find_element(By.ID, "password").send_keys("Autobots")
driver.find_element(By.NAME, "commit").click()

driver.close()