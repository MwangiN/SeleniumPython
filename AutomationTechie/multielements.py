from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()

driver.get("http://automationpractice.pl/index.php")

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))

links=driver.find_elements(By.TAG_NAME, "a")
print(len(links))

driver.close()

