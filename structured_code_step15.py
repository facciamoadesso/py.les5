import os
import random
import shutil
from faker import Faker
import file_operations


OUTPUT_FOLDER = "output_cards"
TEMPLATE_FILE = "src/charsheet.svg"
CARDS_COUNT = 10

SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
] 
   

MAPPING = { 
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}

  
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
    first_name, last_name = fake_name.split(maxsplit=1)
    town = faker.city()
    job = faker.job()

    
    stats = {
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18)
    }
    
    selected_skills = random.sample(runic_skills, 3)
   
    
    context = {
        "first_name": first_name,
        "last_name": last_name,
        "town": town,
        "job": job,
        "strength": stats["strength"],
        "agility": stats["agility"],
        "endurance": stats["endurance"],
        "intelligence": ["intelligence"],
        "luck": stats ["luck"], 
        "skill_1": selected_skills[0],
        "skill_2": selected_skills[1],
        "skill_3": selected_skills[2]
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
    
    runic_skills = style_skills(SKILLS, MAPPING)
    
    for number in range(1, CARDS_COUNT + 1):
        context = generate_character(faker, runic_skills)
        filename = os.path.join(OUTPUT_FOLDER, f"charsheet-{number}.svg")
        save_card(TEMPLATE_FILE, filename, context)
        
        
if __name__ == "__main__":
    main()
