from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def input_2_value(driver, value1, value2, locator):
    driver.get('http://the-internet.herokuapp.com/inputs')
    input = driver.find_element(By.CSS_SELECTOR, locator)
    input.send_keys(value1)    
    input.clear()   
    input.send_keys(value2)    
    driver.quit()

chrome = webdriver.Chrome(options=options)
ff = webdriver.Firefox()

input_2_value(chrome, 1000, 999, 'input')
input_2_value(ff, 1000, 999, 'input')