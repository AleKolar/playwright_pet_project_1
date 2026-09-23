from pathlib import Path

import pytest

from src.UI.browser.browser_launcher import BrowserLauncher
from src.UI.pages.base_pages import BasePage
from src.UI.pages.cart_page import CartPage
from src.UI.pages.login_page import LoginPage


# @pytest.fixture
# def browser():
#     """Создаёт объект Playwright Page, а затем pytest автоматически передаёт этот Page в тесты"""
#     playwright =  sync_playwright().start()
#     browser = playwright.chromium.launch(channel="chrome", headless=False)
#     context = browser.new_context(viewport={"width": 800, "height": 600})
#     page = context.new_page()
#     yield page
#     # Закрываем всё в правильном порядке
#     context.close()
#     browser.close()
#     playwright.stop()

config_yaml_page = Path(__file__).parent.parent / "config_browser.yaml"

@pytest.fixture
def browser():
    brwsr = BrowserLauncher(config_yaml_page)
    new_page = brwsr.create_page() # Например можно передать куки

    yield new_page

    brwsr.close()

# @pytest.fixture
# def page():
#     """Создаёт объект Playwright Page и передаёт его в тест.
#     Здесь возникает вопрос, какие именно объекты Playwright являются context manager
#     в твоей установленной версии. Поэтому самый надёжный и при этом чистый вариант
#     для conftest.py — оставить browser/context с явным закрытием"""
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(
#             channel="chrome",
#             headless=False,
#             slow_mo=500
#         )
#         context = browser.new_context(viewport={"width": 800, "height": 600})
#
#         page = context.new_page()
#
#         yield page
#
#         context.close()
#         browser.close()

@pytest.fixture()
def base_page(browser):
    return BasePage(browser)

@pytest.fixture()
def cart_page(browser):
    return CartPage(browser)

@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)
