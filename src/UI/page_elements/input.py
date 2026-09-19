import allure

from src.UI.page_elements.base import Base


class Input(Base):
    """Предоставляет методы для работы с полями ввода"""
    def clear(self):
        """Очищает поле ввода"""
        with allure.step(f'Очистим поле ввода {self.allure_name}'):
            self._element.clear()

    def get_value(self):
        """Метод для получения текущего значение поля"""
        return self._element.input_value()

    def fill_and_check(self, text: str, delay: int | float = None):
        """Метод для ввода текста"""
        with allure.step(f'Введем {text} в поле ввода {self.allure_name}'):
            if delay:
                self._element.type(text, delay=delay)
            else:
                self.fill(text)





