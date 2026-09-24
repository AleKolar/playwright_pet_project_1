from playwright.sync_api import Page

from src.UI.browser.browser import Browser
from src.UI.page_elements.Link import Link
from src.UI.page_elements.element import Element
from src.UI.page_elements.text import Text
from src.helper.urls import BASE_URL


class PhonesPage:
    """Логика для тестов на вкладке 'Phones'"""
    def __init__(self, page: Page):
        self.page = page
        self.url = BASE_URL
        self.browser = Browser(page)
        self.text_title = Text(page, strategy="by_text", value="CATEGORIES", allure_name="Категории")
        self.link_phones = Link(page, strategy="by_role", role="link", value="Phones", allure_name="Phones")
        self.phone_card = Link(page, strategy="by_role", role="link", value="Samsung galaxy s6", allure_name="Samsung galaxy s6")
        self.all_phone_cards = Element(page, strategy="locator", selector="#tbodyid .card-block:visible", allure_name="Карточки телефонов")

    def check_button_is_enabled(self):
        """Проверяем, что кнопка активна"""
        self.link_phones.check_enabled()

    def phones(self):
        """Открывает категорию Phones"""
        self.link_phones.click()
        self.phone_card.check_visibility()

    def check_phones_category(self):
        """Проверяет, что открыта категория Phones"""
        self.phone_card.check_visibility()

    def count_of_phones(self, numb_of_phones):
        cnt = self.all_phone_cards.get_element().count()
        assert cnt == numb_of_phones, f"Количество телефонов на странице: {cnt}, ожидалось: {numb_of_phones}"