from selenium import webdriver
import time
import pyautogui
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'D:\Selenium\chromedriver.exe')


def login(username, password):
    time.sleep(4)
    driver.get('https://www.instagram.com/')

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.NAME, 'username')
        )
    )
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.NAME, 'password')
        )
    )
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        )
    )

    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()


def upload():
    # Upload
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="QBdPU "]')
        )
    )
    driver.find_element_by_xpath('//div[@class="QBdPU "]').click()
    
    #Select from computer 
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]')
        )
    )
    driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]').click()

    # select the path from computer using py auto gui
    time.sleep(2)
    path = r"C:\Users\lucky\Desktop\django\Confessout\results.jpeg" 
    pyautogui.write(path) 
    pyautogui.press('enter')
    
    # Next 
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')
        )
    )
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()
    time.sleep(2)
       
def confirm():
    # Next again 
    time.sleep(2)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')
        )
    )
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()

    
    # final share
    time.sleep(4)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')
        )
    )
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()
    
    print("Now the image is uploded to the instagram page")
    
    
    


