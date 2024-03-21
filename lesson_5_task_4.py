from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def click_button_wo_id(driver, times: int):
    driver.get('http://uitestingplayground.com/dynamicid')
    for x in range(0, times):    
        String_id = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').get_attribute("id")
        print ('ID кнопки =', String_id)
        driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
        driver.refresh()
    driver.quit()

chrome = webdriver.Chrome(options=options)
ff = webdriver.Firefox()

click_button_wo_id(chrome, 3)
click_button_wo_id(ff, 3)