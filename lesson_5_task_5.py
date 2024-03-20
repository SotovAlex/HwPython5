from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def click_blue_button_chrome(times: int):
    driver = webdriver.Chrome(options=options)
    driver.get('http://uitestingplayground.com/classattr')
    for x in range(0, times):    
        driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
        Alert(driver).accept()
        driver.refresh()
    driver.quit()


def click__blue_button_fox(times: int):
    driver = webdriver.Firefox()
    driver.get('http://uitestingplayground.com/classattr')
    for x in range(0, 3):    
        driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
        Alert(driver).accept()
        driver.refresh()
    driver.quit()


click_blue_button_chrome(3)
click__blue_button_fox(3)