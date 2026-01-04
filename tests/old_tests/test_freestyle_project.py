from playwright.sync_api import expect


class DashboardPage:
    def __init__(self, page):
        self.page = page
        self._new_item_link = "a[href='/view/all/newJob']"

    def open(self):
        self.page.goto("/")

    def click_new_item(self):
        self.page.click(self._new_item_link)


class NewItemPage:
    def __init__(self, page):
        self.page = page
        self._name_input = "input#name"
        self._freestyle_type = "label:has-text('Freestyle project')"
        self._ok_button = "button#ok-button"

    def create_freestyle_project(self, project_name: str):
        self.page.fill(self._name_input, project_name)
        self.page.click(self._freestyle_type)
        self.page.click(self._ok_button)


class ConfigurePage:
    def __init__(self, page):
        self.page = page
        self._description_textarea = "textarea[name='description']"
        self._save_button = "button[name='Submit']"

    def set_description(self, text: str):
        description = self.page.locator(self._description_textarea)
        description.wait_for(state="visible")
        description.fill(text)

    def save(self):
        self.page.click(self._save_button)


class FreestyleProjectPage:
    def __init__(self, page, project_name: str):
        self.page = page
        self.project_name = project_name

        self._add_description_link = "a:has-text('Add description')"
        self._configure_link = "a[href$='/configure']"
        self._description_block = "#description"

    def open(self):
        self.page.goto(f"/job/{self.project_name}/")

    def open_configure(self):
        self.page.click(self._configure_link)

    def click_add_description(self):
        self.page.click(self._add_description_link)

    def description(self):
        return self.page.locator(self._description_block)

    def add_description_button(self):
        return self.page.locator(self._add_description_link)



def test_freestyle_project_configuration(page):
    project_name = "test_01"
    initial_description = "Project Description"
    updated_description = "New Project Description"

    dashboard = DashboardPage(page)
    new_item = NewItemPage(page)
    configure = ConfigurePage(page)
    project = FreestyleProjectPage(page, project_name)

    dashboard.open()
    dashboard.click_new_item()
    new_item.create_freestyle_project(project_name)

    configure.save()

    project.click_add_description()
    configure.set_description(initial_description)
    configure.save()

    project.open()
    project.open_configure()
    configure.set_description(updated_description)
    configure.save()

    project.open()

    expect(project.description()).to_have_text(updated_description)

    expect(project.add_description_button()).to_have_count(0)

    expect(page).to_have_url(f"/job/{project_name}/")
