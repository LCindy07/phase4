from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

BASE_URL = "https://demowebshop.tricentis.com/"


def test_add_to_cart_and_checkout(page, user_data):
    register_page = RegisterPage(page)
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    email = user_data["email"]
    password = user_data["password"]

    # Register
    register_page.navigate(BASE_URL)
    register_page.open_register()
    register_page.register_user(email, password)
    assert register_page.registration_success(), "Registration failed"
    register_page.logout()

    # Login
    login_page.open_login()
    login_page.login(email, password)
    assert login_page.authenticated_signal(email), "Login failed"

    # Product
    product_page.open_camera()
    product_page.select_black_variant()
    product_page.add_to_cart()
    assert product_page.success_bar_visible(), "Add to cart success signal not visible"

    # Cart validation
    cart_page.open_cart()
    assert cart_page.product_name() == "Digital SLR Camera - Black", "Wrong product or variant in cart"
    assert cart_page.quantity() == "1", "Quantity is not 1"

    # Checkout
    cart_page.agree_terms()
    cart_page.checkout()
    page.wait_for_url("**/onepagecheckout", timeout=10000)

    checkout_data = {
        "country": "Austria",
        "city": "Vienna",
        "address1": "Vienna Street",
        "zip": "1234",
        "phone": "001122334455",
        "card_type": "Visa",
        "cardholder": "Barbara Gordon",
        "card_number": "4485564059489345",
        "expiry_month": "04",
        "expiry_year": "2026",
        "code": "123",
    }

    checkout_page.complete_checkout(checkout_data)
    assert checkout_page.confirmation_visible(), "Checkout confirmation signal not visible"