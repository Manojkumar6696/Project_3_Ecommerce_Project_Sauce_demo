from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_menu(self):
        menu_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))
        )
        menu_button.click()
        # Wait until menu side panel appears
        self.wait.until(
            EC.visibility_of_element_located((By.ID, 'sidenav'))
        )

    def logout(self):
        self.open_menu()
        logout_link = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
        )
        logout_link.click()