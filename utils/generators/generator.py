from faker import Faker

fake = Faker()

class Generator:
    username = fake.user_name()
    fullname = f"{fake.first_name()} {fake.last_name()}"
    password = fake.password()
    confirm_password = fake.password()
    email = fake.email()
