from pages.base_page import BasePage


class RegisterPage(BasePage):
    def open_register(self):
        self.page.get_by_role("link", name="Register").click()

    def register_user(self, email, password):
        self.page.locator("#gender-female").check()
        self.page.locator("#FirstName").fill("Barbara")
        self.page.locator("#LastName").fill("Gordon")
        self.page.locator("#Email").fill(email)
        self.page.locator("#Password").fill(password)
        self.page.locator("#ConfirmPassword").fill(password)
        self.page.get_by_role("button", name="Register").click()

    def registration_success(self):
        message = self.page.get_by_text("Your registration completed")
        message.wait_for(state="visible", timeout=10000)
        return message.is_visible()

    def logout(self):
        self.page.get_by_role("link", name="Log out").click()

    def login_link_visible(self):
        login_link = self.page.get_by_role("link", name="Log in")
        login_link.wait_for(state="visible", timeout=10000)
        return login_link.is_visible()