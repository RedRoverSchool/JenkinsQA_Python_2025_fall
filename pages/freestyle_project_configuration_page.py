import re
from playwright.sync_api import expect

from pages.base_page import BasePage
from locators.freestyle_project_configuration_locators import FreestyleProjectConfigurationLocators
from utils.generators.project_generator import ProjectGenerator


class FreestyleProjectConfigurationPage(BasePage):

    def create_freestyle_project_precondition(self) -> str:
        """
        Precondition:  Freestyle project exists in the system
        """

        project_name = ProjectGenerator.generate_freestyle_name()

        self.open("/")
        self.click(FreestyleProjectConfigurationLocators.NEW_ITEM_BUTTON)
        self.fill(FreestyleProjectConfigurationLocators.ITEM_NAME_FIELD, project_name)
        self.click(FreestyleProjectConfigurationLocators.FREESTYLE_PROJECT_TYPE)
        self.click(FreestyleProjectConfigurationLocators.OK_BUTTON)
        self.click(FreestyleProjectConfigurationLocators.SAVE_BUTTON)
        self.click(FreestyleProjectConfigurationLocators.HOME_ICON)

        return project_name

    def open_project_configuration(self, project_name: str):
        self.page.get_by_role(
            "link",
            name=project_name,
            exact=True
        ).click()

        self.click(FreestyleProjectConfigurationLocators.CONFIGURE_BUTTON)

        expect(self.page).to_have_url(re.compile(r"/configure/?$"))

    def assert_toggle_is_visible(self):
        expect(
            self.page.locator(
                FreestyleProjectConfigurationLocators.TOGGLE_INPUT
            )
        ).to_be_visible()

    def assert_toggle_is_enabled(self):
        expect(
            self.page.locator(
                FreestyleProjectConfigurationLocators.TOGGLE_INPUT
            )
        ).to_be_checked()
