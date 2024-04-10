import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def countElem(driver, tag_name)->int:
    # find_element returns only 1 vlaue while find_elements returns a list of all the values
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def main():
    # Initialize browser
    driver = webdriver.Chrome()
    
    # Navigate to website
    driver.get("http://localhost:3000/")

    reward_time = 10
    total_reward_time = 0

    tags = ["img"]
    
    for tag in tags:
        num_images = countElem(driver, tag)
        total_reward_time += reward_time * num_images
        time.sleep(total_reward_time)

    driver.quit()
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()