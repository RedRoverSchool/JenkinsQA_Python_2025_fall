class BaseLocators:
    NEW_ITEM_BUTTON = "a[href='/view/all/newJob']"
    OK_BUTTON = "button#ok-button"
    SAVE_BUTTON = "button[name='Submit']"

    class BaseConfigurationPageLocators:
        TEXTAREA_DESCRIPTION = "//div[normalize-space()='Description']/following-sibling::div[1]//textarea"
        BUTTON_APPLY = "button[name='Apply']"
