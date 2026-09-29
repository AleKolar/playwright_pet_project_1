import allure

from src.UI.tests.conftest import cart_page


class TestCartPage:
    @allure.title("Проверка кнопки 'Place Order'")
    def test_check_exist_button(self, cart_page):
        cart_page.open()
        cart_page.check_exist_button()

    @allure.title("Проверка количчества мониторов в корзине")
    def test_count_of_monitors_in_cart(
            self,
            monitors_page,
            product_page,
            cart_page
    ):
        # 1. Открываем категорию Monitors
        monitors_page.open()
        monitors_page.monitors()

        # 2. Apple
        monitors_page.click_on_apple()
        product_page.add_to_cart()

        # 3. Возвращаемся к Monitors
        monitors_page.open()
        monitors_page.monitors()

        # 4. ASUS
        monitors_page.click_on_asus()
        product_page.add_to_cart()

        # 5. Открываем корзину
        cart_page.check_cart()

        # 6. Проверяем
        cart_page.count_of_items(2)


