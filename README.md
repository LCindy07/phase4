# Demo Web Shop UI Automation Assessment

## Project Overview
This project automates the Demo Web Shop customer journey using:

- Playwright
- Python
- Pytest

The automation covers:

1. User registration
2. User login
3. Add to cart and checkout

The product used is:

- Digital SLR Camera - Black

---

## Project Structure

```text
PythonProject/
├── pages/
│   ├── base_page.py
│   ├── register_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   └── test_checkout.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install

## Run
python -m pytest -v

##Run single
python -m pytest tests/test_registration.py -v
python -m pytest tests/test_login.py -v
python -m pytest tests/test_checkout.py -v