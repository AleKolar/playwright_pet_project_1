class TestBasePage:
    def test_monitor(self, base_page):
        base_page.open()
        base_page.monitors()
        base_page.check_cart(2)

    def test_go_to_cart(self, base_page):
        base_page.open()
        base_page.go_to_cart()






