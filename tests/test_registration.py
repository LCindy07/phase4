from pages.register_page import RegisterPage

BASE_URL = "https://demowebshop.tricentis.com/"


def test_register_user(page, user_data):
    register_page = RegisterPage(page)

    register_page.navigate(BASE_URL)
    register_page.open_register()
    register_page.register_user(
        user_data["email"],
        user_data["password"]
    )

    assert register_page.registration_success(), "Registration success signal not visible"

    register_page.logout()
    assert register_page.login_link_visible(), "User still appears authenticated after logout"