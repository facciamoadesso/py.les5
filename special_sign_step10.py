from faker import Faker
import file_operations
import random

faker = Faker("ru_RU")

with open("skills_list.txt", encoding="utf-8") as f:
    skills = f.read().splitlines()
    
random_skills = random.sample(skills, 3)

special_sign = []

for skill in random_skills:
    new_skill = skill.replace("e", "е͠")
    special_sign.append(new_skill)
    
fake_name = faker.name()
fake_city = faker.city()
fake_job = faker.job()

parts = fake_name.split()
first_name = parts[0]
last_name = parts[1]

strength = random.randint(3, 18)
agility = random.randint(3, 18)
endurance = random.randint(3, 18)
intelligence = random.randint(3, 18)
luck = random.randint(3, 18)

skill_1 = special_sign[0]
skill_2 = special_sign[1]
skill_3 = special_sign[2]

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
    "skill_1": skill_1,
    "skill_2": skill_2,
    "skill_3": skill_3
}

filename = f"output/{first_name}_{last_name}_{fake_city}_{fake_job}.svg"

filename = filename.replace(" ", "_")

file_operations.render_template("src/charsheet.svg", filename, context) 
    
