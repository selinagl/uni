import requests
import os
import csv
import random

def laenderabfrage():
    url = "https://restcountries.com/v3.1/region/europe"
    response = requests.get(url)
    if response.status_code == 200:
        laender = response.json()

    laenderdict = {}
    for i in laender:
        name = i.get("name", {}).get("common", "N/A")
        capital = i.get("capital", ["N/A"])[0]
        laenderdict[name] = capital
    return laenderdict

zusammen = laenderabfrage()

for k,v in zusammen.items():
    print(k, v)

path_dir = os.path.dirname(__file__)
name_csv = "quiz_all_questions.csv"
path_csv = os.path.join(path_dir, name_csv)

list_wrong_answers = []
for val in zusammen.values():
    list_wrong_answers.append(val)

for i in range(1, 4):
    random.shuffle(list_wrong_answers)
    print(list_wrong_answers)

with open(path_csv, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    fields = ["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Correct Answer"]

    csv_writer.writerow(fields)
    for key, val in zusammen.items():
        while True:
            random.shuffle(list_wrong_answers)
            if val not in list_wrong_answers[0:3]:
                break
        list_answers = [val, list_wrong_answers[0], list_wrong_answers[1], list_wrong_answers[2]]
        random.shuffle(list_answers)
        right_answer = list_answers.index(val) + 1
        csv_writer.writerow([key, list_answers[0], list_answers[1], list_answers[2], list_answers[3], right_answer])











