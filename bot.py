from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

flag = True
while flag:
    # flag = False

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    service = Service('/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.delete_all_cookies()

    print("----------------------------Navigate to the website----------------------------")
    driver.get('https://www.dna.fr/magazine-cuisine-et-vins/2024/09/17/votez-pour-votre-resto-cuisine-du-monde-prefere')
    time.sleep(1)

    print("1 - Handle the cookie consent")
    try:
        cookie_button = driver.find_element(By.CLASS_NAME, 'didomi-continue-without-agreeing')
        cookie_button.click()
    except Exception as e:
        print("error - Cookie consent not found or already accepted:", e)
    time.sleep(1)

    print("2 - Locate the choice for Bottega Renzini")
    try:
        bottega_option = driver.find_element(By.ID, "poll_d0801410-374b-4cb4-9308-3eaf8f0fedcd_Choice_0")
        driver.execute_script("arguments[0].scrollIntoView();", bottega_option)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", bottega_option)
    except Exception as e:
        print("error - Could not find the option for Bottega Renzini:", e)

    print("3 - Submit the vote using JavaScript")
    try:
        submit_button = driver.find_element(By.ID, "poll_d0801410-374b-4cb4-9308-3eaf8f0fedcd_Vote")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
        print("error - Failed to submit the vote:", e)
    time.sleep(1)

    print("4 - Close the browser")
    driver.quit()
