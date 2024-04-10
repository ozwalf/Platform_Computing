import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def countElem(driver, tag_name)->int:
    # find_element returns only 1 value while find_elements returns a list of all the values
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def findKeyword(driver, keyword)->bool:
    # print(driver.page_souce.lower())
    return keyword.lower() in driver.page_source.lower()

def wordCount(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    word_count = 0
    for paragraph in paragraphs:
        word_count += len(re.findall(r'\w+', paragraph.get_attribute('innerHTML')))
    return word_count


def userAction(action, driver, reward_time, req_list)->float:
    total_reward_time = 0
    if action.upper() == "KEYWORD":
        for keyword in req_list:
            if findKeyword(driver, keyword):
                print("Found", keyword)
                total_reward_time += reward_time
                time.sleep(reward_time)
            else:
                print("Not found")
    elif action.upper() == "IMAGES":
        for tag in req_list:
            num_images = countElem(driver, tag)
            total_reward_time += reward_time * num_images
            time.sleep(total_reward_time)
    elif action.upper() == "READER":
        num_word = wordCount(driver)
        total_reward_time += reward_time * num_word
        time.sleep(total_reward_time)
    
    return total_reward_time

def clickLink(driver, href):
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        link.click()

def main():
    # Initialize browser
    driver = webdriver.Chrome()
    
    # Navigate to website
    driver.get("http://localhost:3000/")

    reward_time = 10
    reward_per_word = 1

    keywords = ["student", "mochi"]
    tags = ["img"]

    # total_reward_time = userAction("KEYWORD", driver, reward_time, keywords)
    # total_reward_time = userAction("IMAGES", driver, reward_time, tags)
    total_reward_time = userAction("READER", driver, reward_per_word, "")

    # clickLink(driver)    

    driver.quit()
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()