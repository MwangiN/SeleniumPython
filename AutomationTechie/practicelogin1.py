#Selenium4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service #imports service class
serv_obj=Service("drivers/chromedriver.exe")#create service class object

driver=webdriver.Chrome(service=serv_obj)

#automatically launch browser
#driver is an object of chrome class, chrome class contains one constructor
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
#launches webpage

driver.find_element(By.ID, "username").send_keys("student") #takes in locator and actual value.
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

act_title=driver.title
exp_title="Logged In Successfully | Practice Test Automation"
#verifies that the titles match
if act_title==exp_title:
    print("Login Test passsed")
else:
    print("Login Test failed")
#closes the web browser
driver.close()