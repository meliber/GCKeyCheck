import json
import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from common import sleep_time
from common import buttonclick

with open('config.json') as config_file:
    data = json.load(config_file)

def main():
    driver = uc.Chrome()
    url = "https://www.cic.gc.ca/"

    #driver.minimize_window()
    driver.get(url)
    time.sleep(sleep_time)

    buttonclick(driver, 'LINK_TEXT', 'English')
    buttonclick(driver, 'LINK_TEXT', 'Sign in or create an account to apply online')
    buttonclick(driver, 'LINK_TEXT', 'Sign in with GCKey')

    username = driver.find_element(By.ID, 'token1')
    login = data["login"]
    username.send_keys(login)
    time.sleep(sleep_time)
    password_input = driver.find_element(By.ID, 'token2')
    password = data["password"]
    password_input.send_keys(password)
    time.sleep(sleep_time)
    buttonclick(driver, 'ID', 'button')
    buttonclick(driver, 'ID', 'continue')
    buttonclick(driver, 'ID', '_continue')

    challenge = driver.find_element(By.TAG_NAME, 'strong').text.strip('\"')
    try:
        response = data['questions_and_answers'][challenge]
    except:
        raise Exception('failed to get response')
    
    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(response)
    time.sleep(sleep_time)
    buttonclick(driver, 'ID', '_continue')

    # check full application status
    buttonclick(driver, 'XPATH', "//input[@value='Check full application status']")

    # save page html source
    page = driver.page_source
    if not os.path.isfile('status_page.html'):
        with open('status_page.html', 'w', encoding='utf-8') as status_page:
            status_page.write(page)
        previous_status = page
    else:
        with open('status_page.html', encoding='utf-8') as f:
            previous_status = f.read()
    
    if page == previous_status:
        print('status has no changes.')
    else:
        print('status updated!')

if __name__ == '__main__':
    main()
