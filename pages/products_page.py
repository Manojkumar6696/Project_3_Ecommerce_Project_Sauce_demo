from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # Increased wait time

    def select_random_products(self, count=4):
        products = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
        if not products:
            print("No products found on the page.")
            self.driver.save_screenshot('no_products.png')
            return []

        selected = []
        if len(products) < count:
            count = len(products)
        selected_products = random.sample(products, count)
        for index, product in enumerate(selected_products):
            try:
                name = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
                price = product.find_element(By.CLASS_NAME, 'inventory_item_price').text
                add_button = product.find_element(By.TAG_NAME, 'button')
                # Wait for button to be clickable
                self.wait.until(EC.element_to_be_clickable(add_button))
                add_button.click()
                # Wait for cart badge update
                badge_locator = (By.CLASS_NAME, 'shopping_cart_badge')
                self.wait.until(EC.text_to_be_present_in_element(badge_locator, str(index + 1)))
                print(f"Added product: {name} at {price}")
                selected.append((name, price))
            except Exception as e:
                print(f"Error adding product: {e}")
                self.driver.save_screenshot(f'add_product_error_{index}.png')
        return selected

    def go_to_cart(self):
        try:
            cart_link = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link')))
            cart_link.click()
        except Exception as e:
            print("Failed to click cart link:", e)
            self.driver.save_screenshot('click_cart_error.png')

    def open_menu(self):
        try:
            menu_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn')))
            menu_button.click()
        except Exception as e:
            print("Failed to open menu:", e)
            self.driver.save_screenshot('menu_error.png')

    def reset_app_state(self):
        self.open_menu()
        try:
            reset_link = self.wait.until(EC.element_to_be_clickable((By.ID, 'reset_sidebar_link')))
            reset_link.click()
        except Exception as e:
            print("Failed to reset app state:", e)
            self.driver.save_screenshot('reset_error.png')