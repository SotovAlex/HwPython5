from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def wait_clickable_element(driver, element: str):
    driver.get('http://the-internet.herokuapp.com/entry_ad')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element))).click()
    driver.quit()

chrome = webdriver.Chrome(options=options)
ff = webdriver.Firefox()

wait_clickable_element(chrome, 'div.modal-footer')
wait_clickable_element(ff, 'div.modal-footer')




