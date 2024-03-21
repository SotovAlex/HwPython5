from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def login(driver, username: str, password: str):
    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)    
    driver.find_element(By.CSS_SELECTOR, ".radius").click()    
    driver.quit()

chrome = webdriver.Chrome(options=options)
ff = webdriver.Firefox()
    
login(chrome, 'tomsmith', 'SuperSecretPassword!')
login(ff, 'tomsmith', 'SuperSecretPassword!')