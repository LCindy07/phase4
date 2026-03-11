from pages.base_page import BasePage


class LoginPage(BasePage):
    def open_login(self):
        self.page.get_by_role("link", name="Log in").click()

    def login(self, email, password):
        self.page.locator("#Email").fill(email)
        self.page.locator("#Password").fill(password)
        self.page.get_by_role("button", name="Log in").click()

    def authenticated_signal(self, email):
        account_link = self.page.get_by_role("link", name=email)
        account_link.wait_for(state="visible", timeout=10000)
        return account_link.is_visible()