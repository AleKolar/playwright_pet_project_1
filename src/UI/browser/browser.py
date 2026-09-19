import allure
from playwright.sync_api import Page, Cookie


class Browser:
    """Метод для взаимодействия с методами браузера, вкладками и ifram'ами"""
    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url: str):
        """Переходит по указанному URL"""
        step_description = f'Переходим на страницу "{url}"'
        with allure.step(step_description):
            # Указываем wait_until, чтобы Allure видел, когда ждать полной загрузки
            return self.page.goto(url)

    def reload_page(self):
        """Обновление страницы"""
        step_description = f'Обновим страницу с URL "{self.page.url}"'
        with allure.step(step_description):
            return  self.page.reload(wait_until='domcontentloaded')

    def get_cookies(self):
        """Получает cookie страницы"""
        step_description = f'Получаем cookie страницы с URL "{self.page.url}"'
        with allure.step(step_description):
            return self.page.context.cookies()


    def add_cookies(self, cookies: Cookie):
        """Передает список cookies в хранилище браузера"""
        step_description = f'Передаем список cookie в хранилище браузера'
        with allure.step(step_description):
            return self.page.context.add_cookies(cookies)

    def close_tab(self, number: int):
        """Закрывает страницу с указанным порядковым номером"""
        step_description = f'Закрывает страницу с указанным номером "{number}"'
        with allure.step(step_description):
            all_tabs = self.page.context.pages
            all_tabs[number].close()

    def switch_to_tab(self, number: int):
        """Переходит страницу с указанным номером и закрывает предыдущие вкладки"""
        step_description = (f'Переходим на страницу с указанным номером "{number}"'
                            f', закрываем предыдущие вкладки')
        with allure.step(step_description):
            all_tabs = self.page.context.pages
            new_tab = all_tabs[number]
            new_tab.bring_to_front()
            new_tab.wait_for_load_state()
            return new_tab

    def switch_to_iframe_and_click(self, iframe_locator: str, locator_for_click: str):
        """Переходит на iframe и кликает по лакатору iframe"""
        step_description = (f'Переходим на iframe и кликаем по лакатору')
        with allure.step(step_description):
            frame = self.page.frame_locator(iframe_locator)
            frame.locator(locator_for_click).click()

    def alert_accepted(self):
        """Принимает любое диалоговое окно и нажимает 'OK'"""
        step_description = (f'Подтвердим диалоговое окно')
        with allure.step(step_description):
            self.page.on("dialog", lambda dialog: dialog.accept())

    def alert_dismiss(self):
        """Отклоняет любое диалоговое окно и нажимает 'OK'"""
        step_description = (f'Отклоним диалоговое окно')
        with allure.step(step_description):
            self.page.on("dialog", lambda dialog: dialog.dismiss())

    def evaluate_javascript(self, script: str):
        """Выполняет js на странице: Помогает провзаимодействовать с элементом с помощью js кода,
        когда не получается 'достучаться' до элемента"""
        step_description = (f'Выполним js на странице')
        with allure.step(step_description):
            self.page.evaluate(script)

    def check_download_file(self):
        """Проверяет, что файл загрузился после действия ее вызывающего"""
        with self.page.expect_download() as download_info:
            download = download_info.value
            step_description = (f'Проверим, что файл загрузился')
            with allure.step(step_description):
                assert download.path() != ""

    def press_keys(self, keys: str):
        """Выполняет нажатие клавиш/сочетания клавиш на клавиатуре"""
        step_description = (f'Нажмем клавишу/сочетание клавиш на клавиатуре "{keys}"')
        with allure.step(step_description):
            self.page.keyboard.press(keys)

