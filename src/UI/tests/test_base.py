import allure


@allure.story("Главная страница")
class TestBasePage:
    @allure.title("Проверка заголовка 'CATEGORIES'")
    def test_check_title(self, base_page):
        base_page.open()
        base_page.check_title()

    @allure.title("Проверка перехода в ккорзину")
    def test_go_to_cart(self, base_page):
        base_page.open()
        base_page.go_to_cart()

    @allure.title("Проверка, что кнопка 'Phones' активна")
    def test_button_is_enabled(self, base_page):
        base_page.open()
        base_page.check_button_is_enabled()

    # @allure.title("Проверка перехода в категорию 'Phones'")
    # def test_phones_category(self, base_page):
    #     base_page.open()
    #     base_page.phones()


# pytest -s -v src/UI/tests/test_base.py











