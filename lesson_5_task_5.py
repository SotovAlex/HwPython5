from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def click_blue_button(driver, times: int):
    driver.get('http://uitestingplayground.com/classattr')
    for x in range(0, times):    
        driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
        Alert(driver).accept()
        driver.refresh()
    driver.quit()

chrome = webdriver.Chrome(options=options)
ff = webdriver.Firefox()

click_blue_button(chrome, 3)
click_blue_button(ff, 3)