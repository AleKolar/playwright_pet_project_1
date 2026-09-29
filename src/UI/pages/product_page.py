from playwright.sync_api import Page

from src.UI.page_elements.Link import Link
from src.UI.pages.base_pages import BasePage


class ProductPage(BasePage):
    """Логика для страницы конкретного товара."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.add_to_cart_button = Link(
            page,
            strategy="by_role",
            role="link",
            value="Add to cart",
            allure_name="Add to cart"
        )

    def add_to_cart(self):
        """Добавляет текущий товар в корзину."""
        self.add_to_cart_button.click()