from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def login_chrome(username: str, password: str):
    driver = webdriver.Chrome(options=options)
    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)    
    driver.find_element(By.CSS_SELECTOR, ".radius").click()    
    driver.quit()


def login_fox(username: str, password: str):
    driver = webdriver.Firefox()
    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)    
    driver.find_element(By.CSS_SELECTOR, ".radius").click()    
    driver.quit()
    

login_chrome('tomsmith', 'SuperSecretPassword!')
login_fox('tomsmith', 'SuperSecretPassword!')