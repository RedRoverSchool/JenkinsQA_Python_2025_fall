import random


class ProjectGenerator:

    @staticmethod
    def generate_freestyle_name() -> str:
        return f"Freestyle_{random.randint(1, 999_999)}"


