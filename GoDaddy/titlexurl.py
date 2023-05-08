""""
Test Case - Open Godaddy.com and Print its Page title.
Steps to Automate:
1. Launch the browser of your choice say., Firefox, chrome, etc.
2. Open this URL - https://www.godaddy.com/
3. Maximize or set the size of the browser window.
4. Get the Title of the page and print it.
4. Get the URL of the current page and print it.
5. Close the browser
"""
from selenium import webdriver

driver = webdriver.Edge() #browser launch
driver.get("https://www.godaddy.com/") #opens url
driver.maximize_window() #maximizes window

title=driver.title #gets title of the page
print(title) #prints title

url=driver.current_url #gets url of current page
print(url) #prints the url

driver.close() #closes the browser
