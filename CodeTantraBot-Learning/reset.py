from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import getpass
import sys

driver = webdriver.Firefox()

with open('answers.json') as ans:
    data = json.load(ans)

def login():
    print("\t\tCodeTantraBot by Ai-man")

    username = input("username : ")
    password = getpass.getpass("password : ")

    try:
        driver.get("https://kiet.codetantra.com/login.jsp")
        
        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys(username)

        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys(password)

        login_button = driver.find_element(By.ID, 'loginBtn')
        login_button.click()
        
        time.sleep(5)
        driver.find_element(By.CLASS_NAME, 'iframe')
        
    except:
        print("Login failed! use correct username and password")
        driver.quit()
        sys.exit()

def switch_tab(url: str):
    driver.execute_script(f"window.open('{url}', '_blank');")
    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)

    if len(driver.window_handles) > 1:
        old_tab = driver.window_handles[0]
        driver.switch_to.window(old_tab)
        driver.close()

    driver.switch_to.window(new_tab)

def reset(url: str):
    switch_tab(url)
    time.sleep(10)

    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    
    reset = driver.find_element(By.CLASS_NAME, 'btn-warning')
    reset.click()
    
    next_btn = driver.find_element(By.CLASS_NAME, 'btn-info')
    next_btn.click()
    time.sleep(2)
    
def main():
    login()
    
    for item in data:
        url = item['url']
        reset(url)
        
    driver.quit()
    
if __name__ == "__main__":
    main()