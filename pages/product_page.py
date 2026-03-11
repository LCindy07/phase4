from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class ProductPage(BasePage):
    def open_camera(self):
        self.page.goto("https://demowebshop.tricentis.com/digital-slr-camera")

    def select_black_variant(self):
        self.page.locator("#product_details_form").get_by_text("Digital SLR Camera - Black")

    def add_to_cart(self):
        self.page.locator("#add-to-cart-button-18").click()

    def success_bar_visible(self, timeout=10000):
        try:
            success = self.page.get_by_text("The product has been added").first
            success.wait_for(state="visible", timeout=timeout)
            return success.is_visible()
        except PlaywrightTimeoutError:
            return False

