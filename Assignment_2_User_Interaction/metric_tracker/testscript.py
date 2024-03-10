from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Starts session
driver = webdriver.Chrome()

# Navigates to website
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Gets the page title from the browser
title = driver.title

# A wait command that allows for synchronization by allowing the webpage to load. NOTE: this method is not recommended.
driver.implicitly_wait(0.5)

# Searches for elements
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Takes action on said elements
text_box.send_keys("Selenium")
submit_button.click()

# Requests information on elements
message = driver.find_element(by=By.ID, value="message")
text = message.text

time.sleep(5)

# Ends session
driver.quit()