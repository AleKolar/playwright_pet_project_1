from abc import ABC

from playwright.sync_api import Page, expect


class Base(ABC):
    """Базовый класс для взаимодействия с элементами"""
    def __init__(self, page: Page, stragedy: str = None, selector: str = None,
                 role = None, value: str = None, id: str = None):
        self.page = page
        self.stragedy = stragedy
        self.selector = selector
        self.role = role
        self.value = value
        self.id = id

        if stragedy == "locator":
            self._element = self.page.locator(self.selector)
        elif stragedy == "by_role":
            self._element = self.page.get_by_role(role = self.role, name = self.value)
        elif stragedy == "by_text":
            self._element = self.page.get_by_text(text = self.value)
        elif self.stragedy == "by_placeholder":
            self._element = self.page.get_by_placeholder(text = self.value)
        elif self.stragedy == "by_test_id":
            self._element = self.page.get_by_test_id(test_id = id)
        elif self.stragedy == "by_label":
            self._element = self.page.get_by_label(text = self.value)
        else:
            raise ValueError("Указана неверная стратегия")

    def get_element(self):
        """Возвращает локатор элемента"""
        return self._element

    def click(self):
        self._element.click()

    def fill(self, text):
        self._element.fill(text)

    def is_visible(self):
        return self._element.is_visible()

    def check_visibility(self, visible=True):
        """Проверка, что элемент действительно виден"""
        expect(self._element).to_be_visible(visible=visible)

    def wait_for_visibility(self):
        self.check_visibility()

    def wait_for_status(self, state, timeout_msec: int = None):
        """Ожидает указанное состояние Locator."""
        self._element.wait_for(state=state, timeout=timeout_msec)

    """Можно расширить сценарии ожидания. НИЖЕ"""

    def wait_for_hidden(self):
        expect(self._element).to_be_hidden()

    def wait_for_enabled(self):
        expect(self._element).to_be_enabled()

    def wait_for_disabled(self):
        expect(self._element).to_be_disabled()

