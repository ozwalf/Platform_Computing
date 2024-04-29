import time
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium import webdriver
from sys import argv
from math import ceil

def adjust_time(images: any, links: any, iframe: any, search_content: str, keyword: str, preference: str) -> None:
    print(f"User Preference: {preference}")
    sleep_time: float = 5
    if images:
        print(f"User sees {len(images)} image(s)")
        if preference == "image": 
            sleep_time = sleep_time * 2
        sleep_time = len(images) * sleep_time
        print(f"Browsing for {sleep_time}s")
        time.sleep(sleep_time)
        sleep_time = 5
    if links:
        print(f"User sees {len(links)} link(s)")
        if preference == "links": 
            sleep_time = sleep_time * 2
        sleep_time = ceil(len(links) / 3 * sleep_time) # links can be posted like nothing
        print(f"Browsing for {sleep_time}s")
        time.sleep(sleep_time)
        sleep_time = 5
    if keyword.lower() in search_content.lower():
        print(f"Keyword found!")
        if preference == "keyword": 
            sleep_time = sleep_time * 20 # 100s because keyword would make content interesting
            print(f"Browsing for {sleep_time}s")
        time.sleep(sleep_time)
        sleep_time = 5
    if iframe:
        print(f"User spotted {len(links)} iframe(s)")
        if preference == "iframe": 
            sleep_time = (sleep_time * 20 )
            print(f"Browsing for {sleep_time}s")
        sleep_time = (len(iframe) * sleep_time) % 200 # user hits max iframe stare at 200s
        time.sleep(sleep_time)
        sleep_time = 5

def determine_time(url: str, keyword: str) -> None:
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2) # allow page load

    start_time: float = time.time()
    presence_time: float = 0
    content: str = driver.page_source
    images = driver.find_elements(By.TAG_NAME, 'img')
    links = driver.find_elements(By.TAG_NAME, 'a')
    iframe = driver.find_elements(By.TAG_NAME, 'iframe')

    preference = "keyword"

    adjust_time(images, links, iframe, content, keyword, preference)

    current_time: float = round(time.time(), 2)
    presence_time = abs(round(current_time - start_time, 2))
    print(f"Presence time on {url}: {presence_time}s")

    driver.quit()


def main() -> None:
    KEYWORD: str = 'Assignment'                                                             # define keyword: this user loves keywords and iframes
    URL_WITH_PREFERENCE: str = 'http://localhost:3000/'
    URL_WITHOUT_PREFERENCE: str = 'https://google.com/'
    try: 
        if argv[1] == str(0):
            determine_time(URL_WITH_PREFERENCE, KEYWORD)
        else:
            determine_time(URL_WITHOUT_PREFERENCE, KEYWORD)
    except IndexError:
        determine_time(URL_WITH_PREFERENCE, KEYWORD)


if __name__ == '__main__':
    main()