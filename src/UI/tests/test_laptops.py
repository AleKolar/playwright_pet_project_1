import allure

@allure.story("Вкладка 'Laptops'")
class TestLaptopsPage:
    @allure.title("Проверка, что на вкладке 'Laptops' отображается 6 шт. планшетов")
    def test_laptops_category(self, laptops_page):
        laptops_page.open()
        laptops_page.laptops()
        laptops_page.count_of_laptops(6)

# pytest -s -v src/UI/tests/test_laptops.py


