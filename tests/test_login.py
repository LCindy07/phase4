from pages.register_page import RegisterPage
from pages.login_page import LoginPage

BASE_URL = "https://demowebshop.tricentis.com/"


def test_login(page, user_data):
    register_page = RegisterPage(page)
    login_page = LoginPage(page)

    register_page.navigate(BASE_URL)
    register_page.open_register()
    register_page.register_user(
        user_data["email"],
        user_data["password"]
    )
    assert register_page.registration_success(), "Registration failed before login test"
    register_page.logout()

    login_page.open_login()
    login_page.login(
        user_data["email"],
        user_data["password"]
    )

    assert login_page.authenticated_signal(user_data["email"]), "Authenticated user signal not visible"