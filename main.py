import json
import math
import random
import os

answers = {}
data = {}

def load_data(src):
    if not os.path.exists(src):
        with open(src, 'w') as f:
            json.dump([], f)
    f = open(src)
    return json.load(f)

def is_answered(id):
    for answer in answers:
        if(answer["id"]==id):
            return True
    return False

def get_question(list):
    id = math.floor(random.random()*len(list))
    while(is_answered(id)):
        id = math.floor(random.random()*len(list))
    return id, list[id]

def save_answers(src):
    f = open(src, "w", encoding="utf-8")
    json.dump(answers, f, ensure_ascii=False)

def answser_question(id, known):
    answers[id]=known

def get_estimated_knowledge():
    good = 0
    for answer in answers:
        if(answer["answer"]):
            good += 1

    percentage = 1
    if(len(answers)!=0):
        percentage = good / len(answers)
    estimation = percentage * len(data)

    return percentage, estimation


data_src="data/data.json"
answers_src="data/answers.json"

data = load_data(data_src)
answers = load_data(answers_src)

current_id, current_question = get_question(data)
percentage, estimation = get_estimated_knowledge()

while(True):
    print('')
    print(f'Estimation: {round(percentage, 2)}% soit {round(estimation)} mots.')
    print(current_question)

    input_text = "Connaissez-vous ce mot ? (y/n/back): "
    ans = input(input_text)
    while(ans != "y" and ans != "n" and ans != "back"):
        ans = input(input_text)

    if(ans=="back" and len(answers)!=0):
        tmp = answers.pop()
        current_id = tmp["id"]
        current_question = tmp["word"]
        save_answers(answers_src)
        continue

    res = {
        "id": current_id,
        "word": current_question,
        "answer": (ans=="y")
    }
    answers.append(res)
    save_answers(answers_src)

    current_id, current_question = get_question(data)
    percentage, estimation = get_estimated_knowledge()


