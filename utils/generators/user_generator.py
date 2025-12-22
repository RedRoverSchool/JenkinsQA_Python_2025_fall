from data.dataclasses.user_dataclass import CreateUserDataClass
from utils.generators.generator import Generator


class UserGenerator(Generator):


    def create_user_generator(self):
        yield CreateUserDataClass(
            username=self.username,
            password=self.password,
            confirm_password=self.confirm_password,
            fullname=self.fullname,
            email=self.email
        )