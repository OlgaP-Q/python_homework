from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CalculatorPage:
    """Page Object для страницы медленного калькулятора."""

    DELAY_INPUT = (By.ID, "delay")
    EQUALS_BUTTON = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")
    CLEAR_BUTTON = (By.XPATH, "//span[text()='C']")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация Page Object.

        :param driver: экземпляр Selenium WebDriver
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 60)

    def open(self) -> None:
        """Открыть страницу калькулятора.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, seconds: str) -> None:
        """Установить задержку вычислений.

        :param seconds: значение задержки в секундах (str)
        :return: None
        """
        delay_field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, button_text: str) -> None:
        """Нажать кнопку калькулятора по её тексту.

        :param button_text: текст кнопки (например, '7', '+', '=')
        :return: None
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def click_equals(self) -> None:
        """Нажать кнопку '='.

        :return: None
        """
        self.click_button("=")

    def perform_addition(self, num1: int, num2: int) -> None:
        """Выполнить сложение двух чисел на калькуляторе.

        :param num1: первое слагаемое
        :param num2: второе слагаемое
        :return: None
        """
        self.click_button(str(num1))
        self.click_button("+")
        self.click_button(str(num2))

    def perform_subtraction(self, num1: int, num2: int) -> None:
        """Выполнить вычитание двух чисел на калькуляторе.

        :param num1: уменьшаемое
        :param num2: вычитаемое
        :return: None
        """
        self.click_button(str(num1))
        self.click_button("-")
        self.click_button(str(num2))

    def get_result_after_wait(self, expected_result: str) -> str:
        """Дождаться появления ожидаемого результата и вернуть его.

        :param expected_result: ожидаемый текст результата
        :return: фактический текст результата (str)
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.RESULT_SCREEN, expected_result
            )
        )
        return self.driver.find_element(*self.RESULT_SCREEN).text
