import allure

@allure.story("Вкладка 'Phones'")
class TestPhonesPage:
    @allure.title("Проверка, что на вкладке 'Phones' отображается 7 шт. телефонов")
    def test_phones_category(self, phones_page, base_page):
        base_page.open()
        phones_page.phones()
        phones_page.count_of_phones(7)



