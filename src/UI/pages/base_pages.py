from playwright.sync_api import Page

from src.UI.page_elements.element import Element
from src.UI.page_elements.text import Text
from src.helper.urls import BASE_URL, CART_URL


class BasePage:
    """Логика для тестов на главной странице"""

    def __init__(self, page: Page):
        self.page = page
        self.url = BASE_URL
        self.text_monitor = Text(page, stragedy="by_text", value="Monitors")
        self.text_apple_monitor = Text(page, stragedy="by_text", value="Apple monitor 24")
        self.element_card = Element(page, stragedy="locator", selector=".card-block")
        self.text_card = Text(page, stragedy="locator", selector="#cartur")

    def open(self):
        """Открывает страницу по URL"""
        return self.page.goto(self.url)

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
