from playwright.sync_api import Page

from src.UI.page_elements.Link import Link
from src.UI.page_elements.element import Element
from src.UI.page_elements.text import Text
from src.UI.pages.base_pages import BasePage


class MonitorsPage(BasePage):
    """Логика для тестов на вкладке 'Monitors'"""
    def __init__(self, page: Page):
        super().__init__(page)
        self.text_monitor = Text(page, strategy="by_text", value="Monitors", allure_name="Monitors")
        self.text_apple_monitor = Text(page, strategy="by_text", value="Apple monitor 24",
                                       allure_name="Apple monitor 24")
        self.text_asus_monitor = Text(page, strategy="by_text", value="ASUS Full HD",
                                       allure_name="ASUS Full HD")
        self.link_monitors = Link(page, strategy="by_role", role="link", value="Monitors", allure_name="Monitors")
        self.monitors_card = Link(page, strategy="by_role", role="link", value="Apple monitor 24",
                               allure_name="Apple monitor 24")
        self.all_monitors_cards = Element(page, strategy="locator", selector="#tbodyid .card-block:visible",
                                          allure_name="Карточки мониторов")


    def monitors(self):
        """Кликает на мониторы"""
        # self.page.get_by_text(text="Monitors").click()
        # self.page.get_by_text(text="Apple monitor 24").wait_for(state="visible")
        self.text_monitor.click()
        self.monitors_card.check_visibility()

    def count_of_monitors(self, numb_of_cards: int):
        """Проверяет количество карточек с товаром
        :param numb_of_cards: количество карточек"""
        # monitor = self.page.locator(".card-block")
        # cnt = monitor.count()
        cnt = self.all_monitors_cards.get_element().count()
        assert cnt == numb_of_cards, f"Количество мониторов на странице: {cnt}, ожидалось: {numb_of_cards}"

    def click_on_apple(self):
        self.text_apple_monitor.click()


    def click_on_asus(self):
        self.text_asus_monitor.click()




