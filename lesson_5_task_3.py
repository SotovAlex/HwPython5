from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def click_button_chrome(times: int):

    driver = webdriver.Chrome(options=options)
    driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
    for x in range(0, times):
        driver.find_element(By.CSS_SELECTOR, "button").click()
    buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
    print('Количество кнопок Delit:', len(buttons))
    driver.quit()


def click_button_fox(times: int):
    driver = webdriver.Firefox()
    driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
    for x in range(0, times):
        driver.find_element(By.CSS_SELECTOR, "button").click()
    buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
    print('Количество кнопок Delit:', len(buttons))
    driver.quit()

click_button_chrome(5)
click_button_fox(5)