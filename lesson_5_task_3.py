from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def click_button(driver, times: int):
    driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
    for x in range(0, times):
        driver.find_element(By.CSS_SELECTOR, "button").click()
    buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
    print('Количество кнопок Delit в:', len(buttons))
    driver.quit()

chrome = webdriver.Chrome(options=options)
ff = webdriver.Firefox()

click_button(chrome, 5)
click_button(ff, 5)