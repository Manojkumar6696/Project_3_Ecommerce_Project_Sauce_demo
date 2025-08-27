from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_user_details(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element(By.ID, 'continue').click()

    def finish_order(self):
        self.driver.find_element(By.ID, 'finish').click()

    def get_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'complete-header'))
        ).text