import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import strftime, localtime
import mysql.connector

def findKeyword(driver, keyword)->bool:
    # print(driver.page_souce.lower())
    return keyword.lower() in driver.page_source.lower()

def main():
    # Initialize browser
    driver = webdriver.Chrome()
    
    # Navigate to website
    driver.get("http://localhost:3000/")

    reward_time = 10
    total_reward_time = 0
    keywords = ["student", "mochi"]

    for keyword in keywords:
        if findKeyword(driver, keyword):
            print("Found: ", keyword)
            total_reward_time += reward_time
            time.sleep(reward_time)
        else:
            print("Not found: ", keyword)

    driver.quit()
    print("Presence Time:", total_reward_time)

if __name__ == "__main__":
    main()