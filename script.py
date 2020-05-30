from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def runScript(train_num):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)    

    driver.get('https://www.trainspnrstatus.com/train-schedule');

    elem = driver.find_element_by_id("tags")
    elem.send_keys(train_num)

    searchButton= driver.find_element_by_xpath('//*[@id="contact_form"]/div/button')
    searchButton.click()
    element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[3]/table")))
    res = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/table')
    res_html = res.get_attribute('outerHTML')
    driver.close()
    return(res_html)
    

    
