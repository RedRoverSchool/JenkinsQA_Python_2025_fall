class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()
