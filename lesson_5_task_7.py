from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def input_2_value_chrome(value1, value2, locator):
    driver = webdriver.Chrome(options=options)
    driver.get('http://the-internet.herokuapp.com/inputs')
    input = driver.find_element(By.CSS_SELECTOR, locator)
    input.send_keys(value1)    
    input.clear()   
    input.send_keys(value2)    
    driver.quit()

def input_2_value_fox(value1, value2, locator):
    driver = webdriver.Firefox()
    driver.get('http://the-internet.herokuapp.com/inputs')
    input = driver.find_element(By.CSS_SELECTOR, locator)
    input.send_keys(value1)    
    input.clear()    
    input.send_keys(value2)
    driver.quit()
    

input_2_value_chrome (1000, 999, 'input')
input_2_value_fox (1000, 999, 'input')