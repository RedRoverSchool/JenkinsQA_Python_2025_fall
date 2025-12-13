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
    tooltip_environment = [
        ('a[tooltip="Help for feature: Patterns for files to be deleted"]', 'tippy-53', 'Help for feature: Patterns for files to be deleted'),
        ('a[tooltip="Help for feature: Apply pattern also on directories"]', 'tippy-54', 'Help for feature: Apply pattern also on directories'),
        ('a[tooltip="Help for feature: Check parameter"]', 'tippy-55', 'Help for feature: Check parameter'),
        ('a[tooltip="Help for feature: External Deletion Command"]', 'tippy-56', 'Help for feature: External Deletion Command'),
        ('a[tooltip="Help for feature: Disable deferred wipeout"]', 'tippy-57', 'Help for feature: Disable deferred wipeout'),
        ('a[tooltip="Help for feature: Use secret text(s) or file(s)"]', 'tippy-58', 'Help for feature: Use secret text(s) or file(s)'),
        ('a[tooltip="Help for feature: Time-out strategy"]', 'tippy-59', 'Help for feature: Time-out strategy'),
        ('a[tooltip="Help for feature: Absolute"]', 'tippy-62', 'Help for feature: Absolute'),
        ('a[tooltip="Help for feature: Timeout minutes"]', 'tippy-63', 'Help for feature: Timeout minutes'),
        ('a[tooltip="Help for feature: Time-out actions"]', 'tippy-60', 'Help for feature: Time-out actions'),
        ('a[tooltip="Help for feature: With Ant"]', 'tippy-61', 'Help for feature: With Ant')
    ]