import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка временной папки для Snap Firefox
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
    driver.get(
        " https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
    wait = WebDriverWait(driver, 20)

    wait.until(EC.presence_of_element_located(
        (By.NAME, "first-name"))).send_keys("Иван"
                                            )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "last-name"))).send_keys("Петров"
                                           )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "address"))).send_keys("Ленина, 55-3"
                                         )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "e-mail"))).send_keys("test@skypro.com"
                                        )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "city"))).send_keys("Москва"
                                      )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "country"))).send_keys("Россия"
                                         )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "phone"))).send_keys("+7985899998787"
                                       )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "job-position"))).send_keys("QA"
                                              )
    wait.until(EC.presence_of_element_located(
        (By.NAME, "company"))).send_keys("SkyPro"
                                         )

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_code_field.get_attribute(
        "class"), "Поле Zip code должно быть красным!"

    green_fields_ids = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        assert "alert-success" in field_classes, \
            f"Поле {field_id} должно быть зеленым! " \
            f"Классы: {field_classes}"
