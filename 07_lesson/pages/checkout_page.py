from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Page Object для страницы оформления заказа

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_INPUT)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE_INPUT)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()

    def get_total(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        )
        return total_element.text

    def get_total_value(self):
        total_text = self.get_total()
        return float(total_text.replace("Total: $", ""))
