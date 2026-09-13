from playwright.sync_api import expect


class TestLogintPage:
    def test_login(self, login_page):
        login_page.open()
        login_page.input_email()
        login_page.input_password()
        login_page.push_enter()

        expect(login_page.page).to_have_url("https://gitep-iam.lumos-project.online/")
        

# pytest -v src/UI/tests/test_login.py