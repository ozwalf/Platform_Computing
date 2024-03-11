import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    metrics = [
        ['Metric', 'value']
    ]

    title = driver.title
    metrics.append(['Page Title', title])

    # button clicks
    num_clicks = 0

    # Track presence time 
    start_time = time.time()
    presence_time = start_time

    # need to initialise current_time and presence_time outside the while loop else presence_time would equal time.time()
    # time.time() tracks the time since epoch. epoch = Jan 1, 1970. You can see the problem there.
    current_time = time.time()
    presence_time = current_time - start_time

    while (presence_time < 10): # presence_time < 50: # seconds

        current_time = time.time()
        # tracks presence time
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
        # appends presence time per iteration
        metrics.append(['Presence time', presence_time])
        
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")  
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")
        # appends scroll length per iteration
        metrics.append(['Scroll length', f"{current_scroll}/{scroll_height}"])
        
        time.sleep(2) 
        
        # Track button clicks   
        buttons = [driver.find_element(by=By.CSS_SELECTOR, value="button")]
        
        # iterates through all buttons and clicks them. increments num_clicks everytime they are clicked
        for button in buttons:
            button.click()
            num_clicks += 1
            
        print(f"Number of clicks: {num_clicks}")
        # appends total number of click after each iteration of the while loop
        metrics.append(['Button clicks', num_clicks])

    # appends final presence time after the loop
    # metrics.append(['Presence time', presence_time])

    # appends total number of click after the loop
    # metrics.append(['Button clicks', num_clicks])
        
    # writes data into csv file
    with open('metric_tracker.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(metrics) 
    print("Data recorded to metric_tracker.csv")

    print("End of script.")
    driver.quit()

if __name__ == "__main__":
    main()