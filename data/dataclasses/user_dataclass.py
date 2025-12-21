from dataclasses import dataclass

@dataclass
class CreateUserDataClass:
    username: str = None
    password: str = None
    confirm_password: str = None
    fullname: str = None
    email: str = None