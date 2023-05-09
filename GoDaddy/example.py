from selenium import webdriver

# Initialize the Chrome webdriver
driver = webdriver.Chrome()

# Navigate to the webpage you want to scrape
driver.get('https://www.example.com')

# Get the page source
page_source = driver.page_source

# Check if the page title is present in the page source
if 'Example Domain' in page_source:
    print('Page title found in page source')
else:
    print('Page title not found in page source')

# Close the webdriver
driver.quit()
