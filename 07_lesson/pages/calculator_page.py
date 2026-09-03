from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.ID, "delay")
    EQUALS_BUTTON = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")
    CLEAR_BUTTON = (By.XPATH, "//span[text()='C']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, seconds):
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def click_equals(self):
        self.click_button("=")

    def perform_addition(self, num1, num2):
        self.click_button(str(num1))
        self.click_button("+")
        self.click_button(str(num2))

    def perform_subtraction(self, num1, num2):
        self.click_button(str(num1))
        self.click_button("-")
        self.click_button(str(num2))

    def get_result_after_wait(self, expected_result):
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT_SCREEN, expected_result
            )
        )
        return self.driver.find_element(*self.RESULT_SCREEN).text
