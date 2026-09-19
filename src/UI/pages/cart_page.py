from playwright.sync_api import Page, expect

from src.UI.page_elements.button import Button
from src.UI.pages.base_pages import BasePage
from src.helper.urls import BASE_URL, CART_URL


class CartPage(BasePage):
    """Логика для тестов на странице корзины"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = BASE_URL + CART_URL
        self.button_is_exist = Button(page, strategy="by_role", role="button", value="Place Order", allure_name="Place Order")

    def check_exist_button(self):
# Вариант: self.page.get_by_role("button", name="Place Order")
# expect(self.page.get_by_role("button").filter(has_text="Place Order")).to_be_visible(visible=True)
# expect(self.button_is_exist).to_be_visible(visible=True)
        self.button_is_exist.check_visibility()
