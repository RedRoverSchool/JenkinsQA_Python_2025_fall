from locators.base_locators import BaseLocators


class DashboardLocators(BaseLocators):
    @staticmethod
    def folder_with_icon(folder_name):
        return f"tr:has-text('{folder_name}') [class*='folder']"