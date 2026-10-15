import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("SauceDemo")
@allure.severity(allure.severity_level.CRITICAL)
class TestSauceDemo:
    """Тесты для интернет-магазина saucedemo.com."""

    @allure.title("Полный сценарий покупки трёх товаров")
    @allure.description(
        "Авторизация, добавление трёх товаров в корзину, "
        "оформление заказа и проверка итоговой суммы"
    )
    def test_purchase_flow(self, firefox_driver) -> None:
        """Проверка полного сценария покупки.

        :param firefox_driver: фикстура Firefox WebDriver
        :return: None
        """
        login_page = LoginPage(firefox_driver)
        inventory_page = InventoryPage(firefox_driver)
        cart_page = CartPage(firefox_driver)
        checkout_page = CheckoutPage(firefox_driver)

        with allure.step("Открыть сайт и авторизоваться"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара в корзину"):
            inventory_page.add_backpack_to_cart()
            inventory_page.add_bolt_t_shirt_to_cart()
            inventory_page.add_onesie_to_cart()

        with allure.step("Проверить, что в корзине 3 товара"):
            assert inventory_page.get_cart_count() == 3, (
                "Ожидалось 3 товара в бейдже корзины"
            )

        with allure.step("Перейти в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Проверить количество позиций в корзине"):
            assert cart_page.get_cart_items_count() == 3, (
                "Ожидалось 3 позиции в корзине"
            )

        with allure.step("Нажать кнопку Checkout"):
            cart_page.click_checkout()

        with allure.step("Заполнить форму оформления заказа"):
            checkout_page.fill_checkout_info(
                "Иван", "Иванов", "123456"
            )
            checkout_page.click_continue()

        with allure.step(
            "Проверить итоговую сумму: ожидается $58.29"
        ):
            total = checkout_page.get_total_value()
            expected_total = 58.29
            assert total == expected_total, (
                f"Ожидалась сумма ${expected_total}, "
                f"получена ${total}"
            )
