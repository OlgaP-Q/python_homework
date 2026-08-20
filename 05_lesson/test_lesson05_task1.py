from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Находим поле ввода по атрибуту name и вводим имя
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Olga")

    # Находим кнопку Submit по тексту и нажимаем
    submit_button = driver.find_element \
    (By.XPATH, "//button[contains(text(), 'Submit')]")
    submit_button.click()
    # Проверяем, что URL изменился
    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    # Для наглядности можно вывести текущий URL
    print(f"Текущий URL: {driver.current_url}")

    driver.quit()
