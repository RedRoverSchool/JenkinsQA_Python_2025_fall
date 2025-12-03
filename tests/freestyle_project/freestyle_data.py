import random


class Freestyle:
    project_name = f"Freestyle_Project_{random.randint(10000, 99999)}"
    freestyle_type_text = """Classic, general-purpose job type that checks out from up to one SCM, 
                            executes build steps serially, followed by post-build steps like archiving artifacts 
                            and sending email notifications."""
