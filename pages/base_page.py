class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, selector):
        self.page.locator(selector).click()

    def fill(self, selector, value):
        self.page.locator(selector).fill(value)

    def get_text(self, selector):
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()