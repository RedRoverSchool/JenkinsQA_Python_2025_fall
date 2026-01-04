from playwright.sync_api import expect


class NewItemPage:
    def __init__(self, page):
        self.page = page

    def open_dashboard(self):
        self.page.goto("/")

    def create_freestyle_project(self, project_name: str):
        self.page.click("a[href='/view/all/newJob']")
        self.page.fill("input#name", project_name)
        self.page.click("label:has-text('Freestyle project')")
        self.page.click("button#ok-button")
        self.page.click("button[name='Submit']")


class FreestyleProjectPage:
    def __init__(self, page):
        self.page = page

        self.add_description_link = page.locator("a:has-text('Add description')")
        self.description_field = page.locator("textarea[name='description']")
        self.preview_link = page.locator("a.textarea-show-preview")
        self.hide_preview_link = page.locator("a.textarea-hide-preview")
        self.save_button = page.locator("button[name='Submit']")
        self.description_block = page.locator("#description")

    def add_description(self, text: str):
        self.add_description_link.click()
        self.description_field.fill(text)
        self.description_field.click()

    def open_preview(self):
        self.preview_link.click()

    def hide_preview(self):
        self.hide_preview_link.click()

    def save(self):
        self.save_button.click()

    def expect_preview_opened(self):
        expect(self.hide_preview_link).to_be_visible()

    def expect_preview_closed(self):
        expect(self.preview_link).to_be_visible()

    def expect_description_saved(self, text: str):
        expect(self.description_block).to_contain_text(text)


def test_preview_of_the_description(page):
    new_item_page = NewItemPage(page)
    project_page = FreestyleProjectPage(page)

    new_item_page.open_dashboard()
    new_item_page.create_freestyle_project("test_01")

    project_page.add_description("Project Description")

    project_page.open_preview()
    project_page.expect_preview_opened()

    project_page.hide_preview()
    project_page.expect_preview_closed()

    project_page.save()
    project_page.expect_description_saved("Project Description")




