#Test Case
#--------
# 1. Open web browser(Chrome/firefox/edge)
# 2. Open Url https://practicetestautomation.com/practice-test-login/
# 3. Enter username (student)
# 4. Enter password (Password123)
# 5. Click on login
# 6. Capture title of the home page. (Actual title)
# 7. Capture title of the home page: OrangeHRM (Expected)
# 8. close browser

# begin by importing webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("drivers/chromedriver.exe")
#automatically launch browser
#driver is an object of chrome class, chrome class contains one constructor
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
#launches webpage

driver.find_element(By.ID, "username").send_keys("student")
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