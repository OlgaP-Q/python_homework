import allure
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для страницы медленного калькулятора."""

    @allure.title("Сложение 7 + 8 с задержкой 45 секунд")
    @allure.description(
        "Проверка, что калькулятор корректно складывает два числа "
        "после установленной задержки"
    )
    def test_addition_with_delay(self, driver) -> None:
        """Проверка сложения двух чисел с задержкой.

        :param driver: фикстура WebDriver
        :return: None
        """
        calculator_page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calculator_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calculator_page.set_delay("45")

        with allure.step("Ввести выражение 7 + 8"):
            calculator_page.perform_addition(7, 8)

        with allure.step("Нажать '='"):
            calculator_page.click_equals()

        with allure.step("Проверить результат: ожидается '15'"):
            result = calculator_page.get_result_after_wait("15")
            assert result == "15", (
                f"Ожидался '15', получен '{result}'"
            )
