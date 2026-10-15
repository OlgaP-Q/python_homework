from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CartPage:
    """Page Object для страницы корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация Page Object.

        :param driver: экземпляр Selenium WebDriver
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def click_checkout(self) -> None:
        """Нажать кнопку Checkout.

        :return: None
        """
        checkout_button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()

    def get_cart_items_count(self) -> int:
        """Получить количество позиций в корзине.

        :return: число позиций (int)
        """
        items: list[WebElement] = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
