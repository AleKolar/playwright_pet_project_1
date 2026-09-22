import allure
from playwright.sync_api import expect


# class TestLogintPage:
#     def test_login(self, login_page):
#         login_page.open()
#         login_page.input_email()
#         login_page.input_password()
#         login_page.push_enter()
#
#         expect(login_page.page).to_have_url("https://gitep-iam.lumos-project.online/")

@allure.story("Авторизация")
class TestLogintPage:
    @allure.title("Проверка Happy Path: Авторизация с валидными данными пользователя")
    def test_login(self, login_page):
        login_page.open()
        login_page.login()
        expect(login_page.page).to_have_url("https://gitep-iam.lumos-project.online/")
        # login_page.page.pause() # Для визуального контроля/отладки
        login_page.check_element()
        

# pytest -s -v src/UI/tests/test_login.py

# pytest -s -v --alluredir=allure_result src/UI/tests/test_login.py

# pytest -s -v --alluredir=allure_result

# # Запускаем allure через Python
# python -m allure serve allure_result