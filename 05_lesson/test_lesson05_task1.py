from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

# Открыть главную страницу
    driver.get("https://httpbin.qa-territory.online")
    main_url = driver.current_url

# Найти и кликнуть на ссылку HTML Form
    driver.find_element(By.LINK_TEXT, "HTML Form").click()

# Проверить что URL изменился на /forms/post
    expected_url = "https://httpbin.qa-territory.online/post"
    assert driver.current_url == expected_url

# Вернуться назад на главную страницу
    driver.back()

# Проверить что вернулись на исходный URL
    assert driver.current_url == main_url

    driver.quit()
