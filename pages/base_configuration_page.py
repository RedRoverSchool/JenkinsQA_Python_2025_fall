import allure
from playwright.sync_api import expect

from data.data import BaseConfigurationPageData
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from utils.assertions import Assertions


class BaseConfigurationPage(BasePage):
    assertion = Assertions()
    locators = BaseLocators()
    data = BaseConfigurationPageData()

    def go_to_configuration_page(self, name):
        self.page.goto(f"/job/{name}/configure")

    def set_or_change_description(self, text):
        self.fill(self.locators.BaseConfigurationPageLocators.TEXTAREA_DESCRIPTION, text)

    def apply_changes(self):
        self.click(self.locators.BaseConfigurationPageLocators.BUTTON_APPLY)

    def disable_project(self):
        self.click(
            self.locators.BaseConfigurationPageLocators.TOGGLE_LABEL
        )

    def save_configuration(self):
        with allure.step("Save changes on configuration page"):
            self.click(self.locators.SAVE_BUTTON)

    def assert_project_disabled_message_is_displayed(self):
        assert self.is_visible(
            f"text={self.locators.BaseConfigurationPageLocators.DISABLED_MESSAGE_TEXT}"
        )

    def check_message_disable(self):
        text = self.get_text(self.locators.BaseConfigurationPageLocators.DISABLED_MESSAGE_TEXT_LOC)
        return text

    def assert_disable_text(self, actual_text):
        self.assertion.assert_text(
            expected_text=self.data.DISABLED_MESSAGE_TEXT,
            actual_text=actual_text
        )

    def expect_locator_enabled(self, loc):
        with allure.step("Expect locator is enabled"):
            expect(self.page.locator(loc)).to_be_enabled()

    def get_inner_text(self, loc):
        with allure.step(f"Inner text"):
           text = self.page.locator(loc).all_inner_texts()

           return text