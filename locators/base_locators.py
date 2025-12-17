class BaseLocators:

    NEW_ITEM_BUTTON = "a[href='/view/all/newJob']"
    OK_BUTTON = "button#ok-button"
    SAVE_BUTTON = "button[name='Submit']"

    class BaseConfigurationPageLocators:
        TEXTAREA_DESCRIPTION = "textarea[name='_.description']"
        BUTTON_APPLY = "button[name='Apply']"

    class BaseProjectPage:
        DESCRIPTION_TEXT = "div[id='view-message']"