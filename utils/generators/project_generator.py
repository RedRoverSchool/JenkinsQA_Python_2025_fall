import random


class ProjectGenerator:

    @staticmethod
    def generate_freestyle_name() -> str:
        return f"Freestyle_{random.randint(1, 999_999)}"

    @staticmethod
    def generate_folder_name() -> str:
        return f"Folder_{random.randint(1, 999_999)}"

    @staticmethod
    def generate_random_text(length: int = 20) -> str:
        text = "abcdefghjkmnoprstqywxyz"
        random_text = ''.join(
            random.choices(text.lower() , k=length)
        )
        return f"Description {random_text}"

    @staticmethod
    def generate_pipeline_name() -> str:
        return f"Pipeline_{random.randint(1, 999_999)}"





