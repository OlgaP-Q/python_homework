from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация Page Object.

        :param driver: экземпляр Selenium WebDriver
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def fill_checkout_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Заполнить форму оформления заказа.

        :param first_name: имя
        :param last_name: фамилия
        :param postal_code: почтовый индекс
        :return: None
        """
        first_name_field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_INPUT)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE_INPUT)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_continue(self) -> None:
        """Нажать кнопку Continue.

        :return: None
        """
        continue_button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()

    def get_total(self) -> str:
        """Получить текст итоговой суммы.

        :return: текст вида 'Total: $58.29' (str)
        """
        total_element: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL)
        )
        return total_element.text

    def get_total_value(self) -> float:
        """Получить числовое значение итоговой суммы.

        :return: итоговая сумма (float)
        """
        total_text: str = self.get_total()
        return float(total_text.replace("Total: $", ""))
