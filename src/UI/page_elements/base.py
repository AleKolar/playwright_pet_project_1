from abc import ABC

import allure
from playwright.sync_api import Page, expect


class Base(ABC):
    """Базовый класс для взаимодействия с элементами"""
    def __init__(self, page: Page, strategy: str = None, selector: str = None,
                 role = None, value: str = None, id: str = None, allure_name: str = None):
        self.page = page
        self.strategy = strategy
        self.selector = selector
        self.role = role
        self.value = value
        self.id = id
        self.allure_name = allure_name

        if strategy == "locator":
            self._element = self.page.locator(self.selector)
        elif strategy == "by_role":
            self._element = self.page.get_by_role(role = self.role, name = self.value)
        elif strategy == "by_text":
            self._element = self.page.get_by_text(text = self.value)
        elif strategy == "by_placeholder":
            self._element = self.page.get_by_placeholder(text = self.value)
        elif strategy == "by_test_id":
            self._element = self.page.get_by_test_id(test_id = id)
        elif strategy == "by_label":
            self._element = self.page.get_by_label(text = self.value)
        else:
            raise ValueError("Указана неверная стратегия")

    def get_element(self):
        """Возвращает локатор элемента, когда нужно выйти из фреймворка,
        чтоб воспользоваться локатором и использовать методы Playwright напрямую,
        т.е. 'вне класса'"""
        return self._element

    def click(self):
        step_description = (f'Кликнем по элементу "{self.allure_name}"')
        with allure.step(step_description):
            self._element.click()

    def fill(self, text):
        self._element.fill(text)

    def is_visible(self):
        return self._element.is_visible()

    def check_visibility(self, visible=True):
        """Проверка, что элемент действительно виден"""
        if visible:
            status_element = "Видимый"
        else:
            status_element = "Невидимый"
        step_description = (f'Проверяем видимость {self.allure_name}: "{status_element}"')
        with allure.step(step_description):
            expect(self._element).to_be_visible(visible=visible)


    def wait_for_visibility(self):
        self.check_visibility()

    def wait_for_status(self, state, timeout_msec: int = None):
        """Ожидает указанное состояние Locator."""
        if state == "attached" and state == "visible":
            status_element = "Видимый"
        else:
            status_element = "Невидимый"
        step_description = (f'Ждём когда элемент {self.allure_name}станет'
                            f' "{status_element}"')
        with allure.step(step_description):
            self._element.wait_for(state=state, timeout=timeout_msec)

    """Можно расширить сценарии ожидания. НИЖЕ"""

    def wait_for_hidden(self):
        expect(self._element).to_be_hidden()

    def wait_for_enabled(self):
        expect(self._element).to_be_enabled()

    def wait_for_disabled(self):
        expect(self._element).to_be_disabled()

