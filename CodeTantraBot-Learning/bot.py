from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import getpass
import sys

driver = webdriver.Firefox()

with open('answers.json', 'r') as ans:
    data = json.load(ans)

COMMENT = '"""'
CODE_ID = "54883bea2036d78c5efedc3a"
MCQ_ID = "549b4cf30e08f22e46dbf9cf"

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
        
        time.sleep(10)
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
    
def mcq(answer: list):
    i = 0
    checkboxes = driver.find_elements(By.CLASS_NAME, 'checkbox')
    
    for checkbox in checkboxes:
        if(checkbox.is_selected() != answer[i]):
            checkbox.click()
        i += 1
        
    print("MCQ DONE ")
    
    next_btn = driver.find_element(By.CLASS_NAME, 'btn-info')
    next_btn.click()
    time.sleep(2)
            
def code(answer_html: str):
    unchangable_code = []
    
    element = driver.find_element(By.CLASS_NAME, "cm-content")
    
    unchangable_code = driver.find_elements(By.CLASS_NAME, "bg-error")
    
    try:
        if unchangable_code:
            driver.execute_script(f"arguments[0].insertAdjacentText('afterbegin', '{COMMENT}');", element)
            driver.execute_script(f"arguments[0].insertAdjacentText('beforeend', '{COMMENT}');", element)
            
        else:
            driver.execute_script("arguments[0].innerHTML = '';", element)
            print("CODE DELETED")
            
        time.sleep(1)
        driver.execute_script(f"arguments[0].insertAdjacentHTML('beforeend', '{answer_html}');", element)
        print("CODE INSERTED")
        time.sleep(1)
        
        next_btn = driver.find_element(By.CLASS_NAME, 'btn-info')
        next_btn.click()
        time.sleep(2)
            
    except Exception as e:
        try:
            driver.execute_script(f"arguments[0].innerHTML += {json.dumps(answer_html)};", element)
            print("CODE INSERTED - M2")
            time.sleep(2)
        except:
            print("ERROR !")
     
def bot(url: str):
    switch_tab(url)
    print("\n")
    time.sleep(10)

    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    
def main():
    login()
    
    for item in data:
        url = item['url']
        question_type = item['question_type']
        
        bot(url)
        
        if question_type == CODE_ID:
            answer_html = item['answer_html']
            code(answer_html)
            
        elif question_type == MCQ_ID:
            answer = item['answer']
            mcq(answer)
        
        time.sleep(2)

if __name__ == '__main__':
    main()
