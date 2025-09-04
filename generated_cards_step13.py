from faker import Faker
import file_operations
import random
import ast
import os

faker = Faker("ru_RU")

os.makedirs("output", exist_ok=True)

with open("skills_list.txt", encoding="utf-8") as f:
    skills = f.read().splitlines()

with open("letters_mapping.txt", encoding="utf-8") as f:
    mapping_text = f.read().strip()

try:
    letters_mapping = ast.literal_eval(mapping_text)
except Exception:
    if mapping_text and (mapping_text[0] in "\"'" and mapping_text[-1] == mapping_text[0]):
        mapping_text = mapping_text[1:-1]
    letters_mapping = ast.literal_eval(mapping_text)

runic_skills = []
for skill in skills:
    styled = ""
    for ch in skill:
        if ch in letters_mapping:
            styled += letters_mapping[ch]
        else:
            styled += ch
    runic_skills.append(styled)

for number in range(1, 11):  # 1..10
    if len(runic_skills) >= 3:
        selected_skills = random.sample(runic_skills, 3)
    else:
        selected_skills = runic_skills[:]  

    fake_name = faker.name()
    parts = fake_name.split()
    last_name = parts[0] if len(parts) > 0 else ""
    first_name = parts[1] if len(parts) > 1 else ""
    fake_city = faker.city()
    fake_job = faker.job()

    strength = random.randint(3, 18)
    agility = random.randint(3, 18)
    endurance = random.randint(3, 18)
    intelligence = random.randint(3, 18)
    luck = random.randint(3, 18)

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "town": fake_city,
        "job": fake_job,
    "strength": strength,
    "agility": agility,
    "endurance": endurance,
    "intelligence": intelligence,
    "luck": luck,
        "skill_1": selected_skills[0] if len(selected_skills) > 0 else "",
        "skill_2": selected_skills[1] if len(selected_skills) > 1 else "",
        "skill_3": selected_skills[2] if len(selected_skills) > 2 else ""
    }

    filename = "output/charsheet-{}.svg".format(number)

    file_operations.render_template("src/charsheet.svg", filename, context)
