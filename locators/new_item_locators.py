from locators.base_locators import BaseLocators


class NewItemLocators(BaseLocators):

    NEW_ITEM_BTN = "a[href='/view/all/newJob']"
    SELECT_ITEM_TYPE_SECTION = 'div#items'
    ITEM_TYPES = 'div#items li'