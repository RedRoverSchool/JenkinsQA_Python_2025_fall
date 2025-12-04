import random


class Freestyle:
    project_name = f"Freestyle_Project_{random.randint(10000, 99999)}"
    freestyle_type_text = """Classic, general-purpose job type that checks out from up to one SCM, 
                            executes build steps serially, followed by post-build steps like archiving artifacts 
                            and sending email notifications."""
    expected_list_of_environment_checkboxes = [
        'Delete workspace before build starts',
        'Use secret text(s) or file(s)',
        'Add timestamps to the Console Output',
        'Inspect build log for published build scans',
        "Terminate a build if it's stuck",
        'With Ant'
    ]