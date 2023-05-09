"""
 Test Case - Open Godaddy.com and Validate Page Title
Steps to Automate:
1. Launch the browser of your choice say., Firefox, chrome, etc.
2. Open this URL - https://www.godaddy.com/
3. Maximize or set the size of the browser window.
4. Get the Title of the page and validate it with the expected value.
5. Get the URL of the current page and validate it with the expected value.
6. Get the Page source of the web page.
7. And Validate that the page title is present in the page source.
8. Close the browser.
"""

from selenium import webdriver

driver=webdriver.Edge() #test step 1

driver.get("https://www.godaddy.com/") #test step 2
driver.maximize_window() #test step 3

act_title=driver.title #test step 4
exp_title="Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy UK"

if act_title==exp_title:
    print("Title test passed")
else:
    print("Title test failed")

act_url=driver.current_url  #test step 5
exp_url= "https://www.godaddy.com/en-uk"

if act_url==exp_url:
    print("Url test passed")
else:
    print("Url test passed")

pageSource=driver.page_source #test step 6

if "Domain Names, Websites, Hosting & Online Marketing Tools - GoDaddy UK" in pageSource: #test step 7
    print("Title present in page source")
else:
    print("Title not present in page source")

driver.close() #test step 8