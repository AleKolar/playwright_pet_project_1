from playwright.sync_api import Page

from src.UI.browser.browser import Browser
from src.UI.page_elements.Link import Link
from src.UI.page_elements.button import Button
from src.UI.page_elements.element import Element
from src.UI.page_elements.text import Text
from src.helper.urls import BASE_URL, CART_URL


class BasePage:
    """Логика для тестов на главной странице"""

    def __init__(self, page: Page):
        self.page = page
        self.url = BASE_URL
        self.browser = Browser(page)
        self.text_monitor = Text(page, strategy="by_text", value="Monitors", allure_name="Monitors")
        self.text_apple_monitor = Text(page, strategy="by_text", value="Apple monitor 24", allure_name="Apple monitor 24")
        self.element_card = Element(page, strategy="locator", selector=".card-block", allure_name="Карточка товара")
        self.text_card = Text(page, strategy="locator", selector="#cartur", allure_name="Корзина")
        self.text_title = Text(page, strategy="by_text", value="CATEGORIES", allure_name="Категории")
        self.link_phones = Link(page, strategy="by_role", role="link", value="Phones", allure_name="Phones")
        self.phone_card = Link(page, strategy="by_role", role="link", value="Samsung galaxy s6", allure_name="Samsung galaxy s6")
        self.all_phone_cards = Element(page, strategy="locator", selector="#tbodyid .card-block:visible", allure_name="Карточки телефонов")

    def open(self):
        """Открывает страницу по URL"""
        return self.browser.go_to_url(self.url)

    def monitors(self):
        """Кликает на мониторы"""
        # self.page.get_by_text(text="Monitors").click()
        # self.page.get_by_text(text="Apple monitor 24").wait_for(state="visible")
        self.text_monitor.click()
        self.text_apple_monitor.check_visibility()


    def check_cart(self, numb_of_cards: int):
        """Проверяет количество карточек с товаром
        :param numb_of_cards: количество карточек"""
        # monitor = self.page.locator(".card-block")
        # cnt = monitor.count()
        cnt = self.element_card.get_element().count()
        assert cnt == numb_of_cards

    def go_to_cart(self):
        """Переход на страницу корзины"""
        self.text_card.click()
        assert CART_URL in self.page.url

    def check_title(self):
        """Проверяем наличие заголовка"""
        self.text_title.check_visibility()

    def check_button_is_enabled(self):
        """Проверяем, что кнопка активна"""
        self.link_phones.check_enabled()

    def check_phones_category(self):
        """Проверяет, что открыта категория Phones"""
        self.phone_card.check_visibility()

    def phones(self):
        """Открывает категорию Phones"""
        self.link_phones.click()
        self.phone_card.check_visibility()








