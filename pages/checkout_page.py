from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def complete_checkout(self, data):
        # 1. Billing address
        self.page.locator("#BillingNewAddress_CountryId").select_option(label=data["country"])
        self.page.locator("#BillingNewAddress_City").fill(data["city"])
        self.page.locator("#BillingNewAddress_Address1").fill(data["address1"])
        self.page.locator("#BillingNewAddress_ZipPostalCode").fill(data["zip"])
        self.page.locator("#BillingNewAddress_PhoneNumber").fill(data["phone"])

        billing_continue = self.page.locator(
            "#billing-buttons-container input.button-1.new-address-next-step-button"
        )
        billing_continue.wait_for(state="visible", timeout=10000)
        billing_continue.click()

        # 2. Shipping address
        shipping_address_continue = self.page.locator(
            "#shipping-buttons-container input.button-1.new-address-next-step-button"
        )
        shipping_address_continue.wait_for(state="visible", timeout=10000)
        shipping_address_continue.click()

        # 3. Shipping method
        shipping_method_continue = self.page.locator(
            "#shipping-method-buttons-container input.button-1.shipping-method-next-step-button"
        )
        shipping_method_continue.wait_for(state="visible", timeout=10000)
        shipping_method_continue.click()

        # 4. Payment method
        payment_method_continue = self.page.locator(
            "#payment-method-buttons-container input.button-1.payment-method-next-step-button"
        )
        payment_method_continue.wait_for(state="visible", timeout=10000)
        payment_method_continue.click()

        # 5. Payment information
        payment_info_continue = self.page.locator(
            "#payment-info-buttons-container input.button-1.payment-info-next-step-button"
        )
        payment_info_continue.wait_for(state="visible", timeout=10000)
        payment_info_continue.click()

        # 6. Confirm order
        confirm_button = self.page.locator(
            "#confirm-order-buttons-container input.button-1.confirm-order-next-step-button"
        )
        confirm_button.wait_for(state="visible", timeout=10000)
        confirm_button.click()

    def confirmation_visible(self):
        success_message = self.page.get_by_text("Your order has been successfully processed!")
        success_message.wait_for(state="visible", timeout=15000)
        return success_message.is_visible()