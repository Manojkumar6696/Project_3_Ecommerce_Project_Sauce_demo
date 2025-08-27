import unittest

import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.menu_page import MenuPage

class TestLogin(unittest.TestCase):
    @allure.title("Login Test")
    @allure.description("Verify login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.menu_page = MenuPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_various_users(self):
        users = [
            {'username': 'standard_user', 'password': 'secret_sauce', 'expected_success': True},
            # Add more users if needed
        ]
        for user in users:
            self.driver.get("https://www.saucedemo.com/")
            self.login_page.login(user['username'], user['password'])
            if user['expected_success']:
                self.assertIn('inventory.html', self.driver.current_url)
                # Logout safely
                try:
                    self.menu_page.logout()
                except Exception as e:
                    print(f"Logout failed: {e}")

if __name__ == '__main__':
    unittest.main()