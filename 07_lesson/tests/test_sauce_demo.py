import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def firefox_driver():
    # Фикстура для Firefox драйвера с настройками Snap
    # Настройка временной папки для Snap Firefox
    snap_tmp_dir = os.path.expanduser('~/snap/firefox/common/selenium_tmp')
    os.makedirs(snap_tmp_dir, exist_ok=True)
    os.environ['TMPDIR'] = snap_tmp_dir

    options = Options()
    options.binary_location = '/usr/bin/firefox'

    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


class TestSauceDemo:

    def test_purchase_flow(self, firefox_driver):
        # Создаем объекты страниц
        login_page = LoginPage(firefox_driver)
        inventory_page = InventoryPage(firefox_driver)
        cart_page = CartPage(firefox_driver)
        checkout_page = CheckoutPage(firefox_driver)

        # Шаг 1: Открыть сайт и авторизоваться
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Шаг 2: Добавить товары в корзину
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bolt_t_shirt_to_cart()
        inventory_page.add_onesie_to_cart()

        # Проверяем, что в корзине 3 товара
        assert inventory_page.get_cart_count() == 3

        # Шаг 3: Перейти в корзину
        inventory_page.go_to_cart()

        # Проверяем, что в корзине 3 товара
        assert cart_page.get_cart_items_count() == 3

        # Шаг 4: Нажать Checkout
        cart_page.click_checkout()

        # Шаг 5: Заполнить форму данными
        checkout_page.fill_checkout_info(
            "Иван", "Иванов", "123456"
        )
        checkout_page.click_continue()

        # Шаг 6: Проверить итоговую сумму
        total = checkout_page.get_total_value()
        expected_total = 58.29

        assert total == expected_total, \
            f"Ожидалась сумма ${expected_total}, получена ${total}"
