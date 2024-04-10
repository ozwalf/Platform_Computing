import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def countElem(driver, tag_name)->int:
    # find_element returns only 1 vlaue while find_elements returns a list of all the values
    return len(driver.find_elements(By.TAG_NAME, tag_name))

def findKeyword(driver, keyword)->bool:
    # print(driver.page_souce.lower())
    return keyword.lower() in driver.page_source.lower()

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
    elif action.upper() == "LINK":
        num_link = clickLink(driver)
        total_reward_time += reward_time * num_link
    
    return total_reward_time

def clickLink(driver):
    links = driver.find_elements(By.TAG_NAME, "a")
    clickCount = 0
    for link in links:
        # opens link and then waits 2 seconds then switches to new window and closes it
        link.click()
        clickCount += 1
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    return clickCount

def main():
    # Initialize browser
    driver = webdriver.Chrome()
    
    # Navigate to website
    driver.get("http://localhost:3000/")

    reward_time = 10
    reward_per_link = 3

    keywords = ["student", "mochi"]
    tags = ["img"]

    total_reward_time = userAction("KEYWORD", driver, reward_time, keywords)
    total_reward_time += userAction("IMAGES", driver, reward_time, tags)
    total_reward_time += userAction("LINK", driver, reward_per_link, "")
    # clickLink(driver)    

    driver.quit()
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()