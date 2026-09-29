from playwright.sync_api import Page

from src.UI.page_elements.button import Button
from src.UI.page_elements.element import Element
from src.UI.pages.base_pages import BasePage
from src.helper.urls import BASE_URL, CART_URL


class CartPage(BasePage):
    """Логика для тестов на странице корзины"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = BASE_URL + CART_URL
        self.button_is_exist = Button(page, strategy="by_role", role="button", value="Place Order", allure_name="Place Order")
        self.cart_items = Element(page, strategy="locator", selector="#tbodyid tr", allure_name="Товары в корзине")

    def check_exist_button(self):
        """Проверяет, что мы на странице корзины
        # Вариант: self.page.get_by_role("button", name="Place Order")
        # expect(self.page.get_by_role("button").filter(has_text="Place Order")).to_be_visible(visible=True)
        # expect(self.button_is_exist).to_be_visible(visible=True)"""
        self.button_is_exist.check_visibility()

    def check_cart(self):
        self.go_to_cart()
        self.check_exist_button()

    def count_of_items(self, expected_count: int):
        """Проверяет количество товаров в корзине."""

        actual_count = self.cart_items.get_element().count()

        assert actual_count == expected_count, (
            f"Количество товаров в корзине: {actual_count}, "
            f"ожидалось: {expected_count}"
        )




