from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Firefox()

driver.get("https://kiet.codetantra.com/login.jsp")

with open('ques_learning.json', 'r') as ques:
    data = json.load(ques)

CODE_ID = "54883bea2036d78c5efedc3a"
MCQ_ID = "549b4cf30e08f22e46dbf9cf"

answers = []

username = ''
password = '' #getpass.getpass("password : ")

username_field = driver.find_element(By.NAME, 'email')
username_field.send_keys(username)

password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys(password)

login_button = driver.find_element(By.ID, 'loginBtn')
login_button.click()

def switch_tab(url: str):
    driver.execute_script(f"window.open('{url}', '_blank');")
    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)

    if len(driver.window_handles) > 1:
        old_tab = driver.window_handles[0]
        driver.switch_to.window(old_tab)
        driver.close()

    driver.switch_to.window(new_tab)

def mcq(item: dict, answer: list):
    checkboxes = driver.find_elements(By.CLASS_NAME, 'checkbox')

    for checkbox in checkboxes:
        answer.append(checkbox.is_selected())

    url = item['url']
    question_type = item['question_type']

    answers.append({
        "url": url,
        "question_type": question_type,
        "answer": answer,
    })

    with open('answers_learning.json', 'w') as ans:
        json.dump(answers, ans, indent=4)

def code(item: dict):
    content_element = driver.find_element(By.CLASS_NAME, "cm-content")

    answer_html = content_element.get_attribute("innerHTML")
    content = content_element.text

    question_type = item['question_type']
    url = item['url']

    answers.append({
        'url': url,
        'question_type': question_type,
        'answer': content,
        'answer_html': answer_html,
    })

    with open('answers_learning.json', 'w') as ans:
        json.dump(answers, ans, indent=4)

def bot(url: str):
    switch_tab(url)
    time.sleep(10)

    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)

def main():
    for item in data:
        url = item['url']
        question_type = item['question_type']

        bot(url)

        if question_type != "assessment":
            if question_type == CODE_ID:
                code(item)
                print("successfully scraped code !")

            elif question_type == MCQ_ID:
                mcq(item, [])
                print("successfully scraped mcq !")
        else:
            print("skiped the assessment")

main()