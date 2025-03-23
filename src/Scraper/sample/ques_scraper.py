import json

with open('test.json', 'r') as test:
    data = json.load(test)

BASE_URL = "https://kiet.codetantra.com/secure/course.jsp?eucId=677fa2bd9230d00cb996dd85#/contents"

ques_learning = []

def scrape():
    for item1 in data['contents']:
        id_1 = item1['id']

        for item2 in item1['contents']:
            id_2 = item2['id']

            if item2['type'] == "unit":
                for item3 in item2['contents']:
                    id_3 = item3['id']

                    url = f"{BASE_URL}/{id_1}/{id_2}/{id_3}"
                    question_type = item3['questionType']

                    ques_learning.append({
                    "url": url,
                    "question_type": question_type,
                })

                with open('ques_learning.json', 'w') as ques:
                    json.dump(ques_learning, ques, indent=4)

            elif item2['type'] == "assessment":
                question_type = item2['type']
                url = f"{BASE_URL}/{id_1}/{id_2}"

                ques_learning.append({
                    "url": url,
                    "question_type": question_type,
                })

                with open('ques_learning.json', 'w') as ques:
                    json.dump(ques_learning, ques, indent=4)

scrape()