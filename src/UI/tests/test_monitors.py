import allure


@allure.story("Главная страница")
class TestMonitorsPage:
    @allure.title("Проверка количества карточек с товаром")
    def test_monitor(self, monitors_page):
        monitors_page.open()
        monitors_page.monitors()
        monitors_page.count_of_monitors(2)


