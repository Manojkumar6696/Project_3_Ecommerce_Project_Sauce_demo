from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_cart_item_details(self):
        items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        details = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(By.CLASS_NAME, 'inventory_item_price').text
            details.append((name, price))
        return details

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()