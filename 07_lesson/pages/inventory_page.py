from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class InventoryPage:
    # Page Object для главной страницы магазина

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_T_SHIRT_ADD = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD = (By.ID, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        button = self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD))
        button.click()

    def add_bolt_t_shirt_to_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.BOLT_T_SHIRT_ADD)
        )
        button.click()

    def add_onesie_to_cart(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ONESIE_ADD))
        button.click()

    def go_to_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        cart_link.click()

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except NoSuchElementException:
            # Если элемента с количеством нет, значит корзина пуста
            return 0
