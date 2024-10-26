import faker
import random


def new_user():
    fake = faker.Faker()
    name = "user"
    random_digits = random.randint(100, 999)
    domain = fake.free_email_domain()
    email = f"{name}{random_digits}@{domain}"
    password = f"{random_digits}"
    return email, password, name
