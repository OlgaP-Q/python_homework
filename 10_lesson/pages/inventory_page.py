from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class InventoryPage:
    """Page Object для главной страницы магазина."""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_T_SHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация Page Object.

        :param driver: экземпляр Selenium WebDriver
        :return: None
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self) -> None:
        """Добавить рюкзак Sauce Labs Backpack в корзину.

        :return: None
        """
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD)
        )
        button.click()

    def add_bolt_t_shirt_to_cart(self) -> None:
        """Добавить футболку Sauce Labs Bolt T-Shirt в корзину.

        :return: None
        """
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.BOLT_T_SHIRT_ADD)
        )
        button.click()

    def add_onesie_to_cart(self) -> None:
        """Добавить комбинезон Sauce Labs Onesie в корзину.

        :return: None
        """
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.ONESIE_ADD)
        )
        button.click()

    def go_to_cart(self) -> None:
        """Перейти на страницу корзины.

        :return: None
        """
        cart_link: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        )
        cart_link.click()

    def get_cart_count(self) -> int:
        """Получить количество товаров в корзине.

        :return: количество товаров (int), 0 если бейдж отсутствует
        """
        try:
            badge: WebElement = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except NoSuchElementException:
            return 0
