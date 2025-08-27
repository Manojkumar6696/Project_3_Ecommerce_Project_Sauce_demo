import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.menu_page import MenuPage

class TestCartAndCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.saucedemo.com/")
        self.login = LoginPage(self.driver)
        self.products = ProductsPage(self.driver)
        self.cart = CartPage(self.driver)
        self.checkout = CheckoutPage(self.driver)
        self.menu = MenuPage(self.driver)

    def tearDown(self):
         self.driver.quit()

    def test_full_purchase_flow(self):
        # Login
        self.login.login('standard_user', 'secret_sauce')
        self.assertIn('inventory.html', self.driver.current_url)

        # Select and add 4 random products
        selected_products = self.products.select_random_products(4)
        print(f"Selected products: {selected_products}")

        # Navigate to cart
        self.products.go_to_cart()

        # Save screenshot for debugging
        self.driver.save_screenshot('cart_page_debug.png')

        # Wait for cart page to load
        try:
            WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cart_item'))

            )
        except TimeoutException:
            print("Cart page did not load properly.")
            self.driver.save_screenshot('cart_load_timeout.png')
            self.fail("Cart page load timeout.")

        # Get cart items
        cart_items = self.cart.get_cart_item_details()
        print(f"Cart items: {cart_items}")

        # Assertion: cart should contain 4 items
        time.sleep(5)
        self.assertEqual(len(cart_items), 4, f"Expected 4 items in cart, but found {len(cart_items)}.")

        # Verify each selected product is in cart
        for item in selected_products:
            self.assertIn(item, cart_items)

        # Proceed to checkout
        self.cart.proceed_to_checkout()

        # Fill checkout info
        self.checkout.fill_user_details('John', 'Doe', '12345')
        self.checkout.continue_checkout()

        # Finish purchase
        self.checkout.finish_order()

        # Confirm message
        message = self.checkout.get_confirmation_message()
        print(f"Confirmation message: {message}")
        self.assertIn('Thank you for your order!', message)

if __name__ == '__main__':
    unittest.main()