from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def click_button_wo_id_chrome(times: int):
    driver = webdriver.Chrome(options=options)
    driver.get('http://uitestingplayground.com/dynamicid')
    for x in range(0, times):    
        String_id = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').get_attribute("id")
        print ('ID кнопки =', String_id)
        driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
        driver.refresh()
    driver.quit()


def click_button_wo_id_fox(times: int):
    driver = webdriver.Firefox()
    driver.get('http://uitestingplayground.com/dynamicid')
    for x in range(0, times):    
        String_id = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').get_attribute("id")
        print ('ID кнопки =', String_id)
        driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
        driver.refresh()
    driver.quit()


click_button_wo_id_chrome(3)
click_button_wo_id_fox(3)