from playwright.sync_api import Page

from src.UI.page_elements.button import Button
from src.UI.page_elements.input import Input
from src.UI.pages.base_pages import BasePage
from src.helper.email_password import EMAIL, PASSWORD
from src.helper.urls import LOGIN_URL


class LoginPage(BasePage):
    """Логика для страницы Login."""

    def __init__(self, page: Page):
        super().__init__(page)

        self.url = LOGIN_URL

        self.email_input = Input(page, strategy="by_placeholder", value="Введите свою почту", allure_name="Поле для ввода почты")

        self.password_input = Input(page, strategy="by_placeholder", value="Введите пароль", allure_name="Поле для ввода пароля")

        self.login_button = Button(page, strategy="by_role", role="button", value="Войти", allure_name="Войти")

        self.button_is_visible = Button(page, strategy="by_role", role="button", value="Delete project", allure_name="Delete project")

    # def input_email(self):
    #     self.email_input.fill_and_check(text=EMAIL)
    #
    # def input_password(self):
    #     self.password_input.fill_and_check(text=PASSWORD)
    #
    # def push_enter(self):
    #     self.login_button.click()

    def login(self):
        self.email_input.fill_and_check(text=EMAIL)
        self.password_input.fill_and_check(text=PASSWORD)
        self.login_button.click()

    def check_element(self):
        self.button_is_visible.check_visibility()



