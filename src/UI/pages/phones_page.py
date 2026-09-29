from src.UI.pages.base_pages import BasePage


class PhonesPage(BasePage):
    """Логика для тестов на вкладке 'Phones'"""

    def phones(self):
        """Открывает категорию Phones"""
        self.link_phones.click()
        self.phone_card.check_visibility()

    def count_of_phones(self, numb_of_phones: int):
        cnt = self.all_phone_cards.get_element().count()
        assert cnt == numb_of_phones, f"Количество телефонов на странице: {cnt}, ожидалось: {numb_of_phones}"