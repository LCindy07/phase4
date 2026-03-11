from pages.base_page import BasePage


class CartPage(BasePage):
    def open_cart(self):
        self.page.goto("https://demowebshop.tricentis.com/cart")

    def product_name(self):
        return self.page.locator(".product-name").inner_text().strip()

    def quantity(self):
        return self.page.locator(".qty-input").input_value().strip()

    def agree_terms(self):
        checkbox = self.page.locator("#termsofservice")
        checkbox.scroll_into_view_if_needed()
        checkbox.check()

    def checkout(self):
        button = self.page.locator("#checkout")
        button.scroll_into_view_if_needed()
        button.click()