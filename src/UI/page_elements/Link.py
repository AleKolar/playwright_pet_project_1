import allure
from playwright.sync_api import expect

from src.UI.page_elements.base import Base


class Link(Base):
    """Предоставляет методы для работы с Link"""
    pass

    def check_enabled(self):
        """Проверяет, что элемент доступен для взаимодействия"""
        with allure.step(f'Проверяем доступность "{self.allure_name}"'):
            expect(self._element).to_be_enabled()
