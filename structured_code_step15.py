import os
import random
import shutil
import ast
from faker import Faker
import file_operations


OUTPUT_FOLDER = "output_cards"
SKILLS_FILE = "skills_list.txt"
MAPPING_FILE = "letters_mapping.txt"
TEMPLATE_FILE = "src/charsheet.svg"
CARDS_COUNT = 10


def load_skills(skills_file):
    with open(skills_file, encoding="utf-8") as f:
        return f.read().splitlines()


def load_mapping(mapping_file):
    with open(mapping_file, encoding="utf-8") as f:
        mapping_text = f.read().strip()
        return ast.literal_eval(mapping_text)


def style_skills(skills, mapping):
    runic_skills = []
    for skill in skills:
        styled = ""
        for ch in skill:
            styled += mapping.get(ch, ch)
        runic_skills.append(styled)
    return runic_skills
    

def generate_character(faker, runic_skills):
    fake_name = faker.name()
    parts = fake_name.split()
    last_name = parts[0] if len(parts) > 0 else ""
    first_name = parts[1] if len(parts) > 1 else ""
    fake_city = faker.city()
    fake_job = faker.job()
    
    
    
    stats = {
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18)
    }
    
    if len(runic_skills) >= 3:
        selected_skills = random.sample(runic_skills, 3)
    else:
        selected_skills = runic_skills[:]
    
    
    context = {
        "first_name": first_name,
        "last_name": last_name,
        "town": fake_city,
        "job": fake_job,
        **stats,
        "skill_1": selected_skills[0] if len(selected_skills) > 0 else "",
        "skill_2": selected_skills[1] if len(selected_skills) > 1 else "",
        "skill_3": selected_skills[2] if len(selected_skills) > 2 else ""
    }
    return context


def save_card(template_file, output_file, context):
    file_operations.render_template(template_file, output_file, context)
   
   
def prepare_output_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)
    
    
def main():
    faker = Faker("ru_RU")
        
        
    prepare_output_folder(OUTPUT_FOLDER)
    
    
    skills = load_skills(SKILLS_FILE)
    mapping = load_mapping(MAPPING_FILE)
    runic_skills = style_skills(skills, mapping)
    
    
    for number in range(1, CARDS_COUNT + 1):
        context = generate_character(faker, runic_skills)
        filename = os.path.join(OUTPUT_FOLDER, "charsheet-{}.svg".format(number))
        save_card(TEMPLATE_FILE, filename, context)
        
        
if __name__ == "__main__":
    main()
