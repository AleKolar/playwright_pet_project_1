import allure


class TestCartPage:
    @allure.title("Проверка кнопки 'Place Order'")
    def test_check_exist_button(self, cart_page):
        cart_page.open()
        cart_page.check_exist_button()

