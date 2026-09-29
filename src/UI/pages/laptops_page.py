from src.UI.pages.base_pages import BasePage


class LaptopsPage(BasePage):
    """Логика для тестов на вкладке 'Tablets'"""


    def laptops(self):
        """Открывает категорию Laptops"""
        self.link_laptops.click()
        self.laptop_card.check_visibility()


    def count_of_laptops(self, numb_of_laptops):
        cnt = self.all_laptops_cards.get_element().count()

        print(f"Количество ноутбуков на странице: {cnt}")

        assert cnt == numb_of_laptops, f"Количество планшетов на странице: {cnt}, ожидалось: {numb_of_laptops}"