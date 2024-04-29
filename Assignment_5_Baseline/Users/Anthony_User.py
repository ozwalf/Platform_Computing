from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Set the base URLs for the websites
url_with_keyword = 'https://en.wikipedia.org/wiki/Web_scraping'
url_without_keyword = 'https://www.example.com/without-images'
url_test = 'http://localhost:3000/'

# Set the keyword to search for
keyword = 'web scraping'

# Path to save screenshots
images_directory = './Images'
os.makedirs(images_directory, exist_ok=True)

def run_test(url, has_keyword):
    driver = None
    try:
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()

        # Open the URL
        driver.get(url)

        # Wait for the page to fully load
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        presence_time = 0
        found_keyword = False
        found_image = False
        found_link = False

        # Continuously check if the content contains the keyword
        while presence_time < 20:
            content = driver.find_element(By.TAG_NAME, 'body').text
            if keyword in content:
                found_keyword = True
                presence_time += 10
                break

            time.sleep(1)
            presence_time += 1

        # Check for images on the page
        images = driver.find_elements(By.TAG_NAME, 'img')
        if images:
            found_image = True
            for image in images:
                time.sleep(10)
                presence_time += 10

        # Check for links on the page
        link = driver.find_element(By.TAG_NAME, 'a')
        if link:
            found_link = True
            # Additional checks and navigation can be included here

            # Take action on the link
            link.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Print results
        print(f'Presence time on {url}: {presence_time} seconds')
        print(f'Keyword found: {found_keyword}')
        print(f'Image found: {found_image}')
        print(f'Link found: {found_link}')

        # Save screenshots based on condition
        screenshot_filename = os.path.join(images_directory, 'with-keyword.png' if has_keyword else 'without-keyword.png')
        driver.get_screenshot_as_file(screenshot_filename)

    except Exception as e:
        print(e)
    finally:
        if driver:
            driver.quit()

# Run the tests
run_test(url_test, False)
# run_test(url_with_keyword, True)
# run_test(url_without_keyword, False)
