import pytest
import uuid
from playwright.sync_api import sync_playwright

BASE_URL = "https://demowebshop.tricentis.com"

DEFAULT_PASSWORD = "Tosca1234!"

BILLING_DATA = {
    "first_name": "Barbara",
    "last_name": "Gordon",
    "country": "Austria",
    "city": "Vienna",
    "address": "Vienna Street",
    "zip": "1234",
    "phone": "001122334455"
}

PAYMENT_DATA = {
    "card_type": "Visa",
    "cardholder": "Barbara Gordon",
    "card_number": "4485564059489345",
    "expiry_month": "04",
    "expiry_year": "2022",
    "code": "123"
}

@pytest.fixture(scope="function")
def user_data():
    return {
        "email": f"user_{uuid.uuid4().hex[:6]}@test.com",
        "password": "Tosca1234!"
    }


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")