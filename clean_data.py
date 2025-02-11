import json

f = open("data/raw_data.json")


data = json.load(f)

list = []

seen_set = set()

for word in data:
    current_word = word["M"]["mot"]
    if "no" in word["M"]:
        if(not current_word in seen_set):
            seen_set.add(current_word)
            list.append(current_word)
    else:
        list.append(current_word)



with open("data/data.json", "w", encoding="utf-8") as file:
    json.dump(list, file, ensure_ascii=False, indent=4)