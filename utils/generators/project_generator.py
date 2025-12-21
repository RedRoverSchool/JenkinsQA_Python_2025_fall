import random


class ProjectGenerator:

    @staticmethod
    def generate_freestyle_name() -> str:
        return f"Freestyle_{random.randint(1, 999_999)}"

    @staticmethod
    def generate_folder_name() -> str:
        return f"Folder_{random.randint(1, 999_999)}"



