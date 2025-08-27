import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.menu_page import MenuPage

class TestSortAndReset(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.products = ProductsPage(self.driver)
        self.menu = MenuPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_sort_and_reset(self):
        # Login
        self.login_page.login('standard_user', 'secret_sauce')
        self.assertIn('inventory.html', self.driver.current_url)

        # TODO: Implement sorting tests as needed, e.g., by selecting sorting options

        # Reset app state
        self.products.reset_app_state()

        # Add assertions here to verify reset if necessary

if __name__ == '__main__':
    unittest.main()