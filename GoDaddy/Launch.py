#teststeps

"""Test Case - Open Godaddy.com and maximize the browser window.
Steps to Automate:
1. Launch the browser of your choice say., Firefox, chrome, etc.
2. Open this URL - https://www.godaddy.com/
3. Maximize or set the size of the browser window.
4. Close the browser."""

from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.godaddy.com/")

driver.maximize_window()
driver.close()
