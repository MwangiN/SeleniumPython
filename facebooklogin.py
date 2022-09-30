from selenium import webdriver

#creates a browser instance even with the browser closed
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("drivers/chromedriver.exe")

#expands the window to the maximum
driver.maximize_window()

#open webpage using get statement
driver.get("https://www.facebook.com/")

#locate the elements by using find element with class name

driver.find_element(By.CLASS_NAME, "_6luy").send_keys("Jesus")
driver.find_element(By.CLASS_NAME, "_9npi").send_keys("Christ")
driver.find_element(By.CLASS_NAME, "_51sy").click()
#closes the browser
driver.close()

