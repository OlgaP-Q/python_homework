import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

snap_tmp_dir = os.path.expanduser('~/snap/firefox/common/selenium_tmp')
os.makedirs(snap_tmp_dir, exist_ok=True)
os.environ['TMPDIR'] = snap_tmp_dir


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = '/usr/bin/firefox'
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


def test_zip_code_validation(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("Test")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "summary_total_label"
        ))
    )
    total_text = total_element.text

    expected_total = "Total: $58.29"
    assert total_text == expected_total, \
        f"Ожидалось '{expected_total}', \
        но получено '{total_text}'"
