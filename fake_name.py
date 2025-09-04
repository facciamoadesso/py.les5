from faker import Faker
import file_operations

faker = Faker("ru_RU")

fake_name = faker.name()
fake_city = faker.city()
fake_job = faker.job()

parts = fake_name.split()
first_name = parts[0]
last_name = parts[1]

context = {
    "first_name": first_name,
    "last_name": last_name,
    "town": fake_city,
    "job": fake_job
}

filename = f"output/{first_name}_{last_name}_{fake_city}_{fake_job}.svg"

filename = filename.replace(" ", "_")

file_operations.render_template("src/charsheet.svg", filename, context) 
    
