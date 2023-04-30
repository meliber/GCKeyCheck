import random
import time
from selenium.webdriver.common.by import By

# sleep time between 3 - 6 seconds
sleep_time = 3 + 3 * random.random()

def buttonclick(driver, search_method, search_content, sleep_time=sleep_time):
    driver.find_element(getattr(By, search_method), search_content).click()
    time.sleep(sleep_time)

