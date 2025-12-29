class BaseLocators:
    NEW_ITEM_BUTTON = "a[href='/view/all/newJob']"
    OK_BUTTON = "button#ok-button"
    SAVE_BUTTON = "button[name='Submit']"
    NAME_OF_CREATED_PROJECT = lambda job_name: f"td a[href='job/{job_name}/']"

    class BaseConfigurationPageLocators:
        TEXTAREA_DESCRIPTION = "//div[normalize-space()='Description']/following-sibling::div[1]//textarea"
        BUTTON_APPLY = "button[name='Apply']"

        TOGGLE_INPUT = "input#enable-disable-project"
        TOGGLE_LABEL = "label[for='enable-disable-project']"
        DISABLED_MESSAGE_TEXT = "This project is currently disabled"
        DISABLED_MESSAGE_TEXT_LOC = "form#enable-project"
