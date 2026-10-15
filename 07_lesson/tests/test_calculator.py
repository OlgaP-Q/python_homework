import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calculator_page import CalculatorPage


class TestCalculator:
    @pytest.fixture
    def driver(self):
        options = Options()
        options.add_argument("--remote-allow-origins=*")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_addition_with_delay(self, driver):
        calculator_page = CalculatorPage(driver)
        calculator_page.open()
        calculator_page.set_delay("45")
        calculator_page.perform_addition(7, 8)
        calculator_page.click_equals()
        result = calculator_page.get_result_after_wait("15")
        assert result == "15", f"Ожидался '15', получен '{result}'"
