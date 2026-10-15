from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        # 1. Откройте страницу https://gitflic.ru/
        driver.get("https://gitflic.ru/")

        # Данные Пользователя 1
        user1_cookies = [
            {'name': 'SESSION',
             'value': 'ZmYxZTk1NWMtN2M2Ny00MmYzLTg0ZDUtNDM1OTZkNTdlNDg2',
             'domain': '.gitflic.ru'},

            {'name': 'X-CSRF-TOKEN',
             'value': '12721b29-efd9-4a0b-adc7-c38f7f8389f4',
             'domain': '.gitflic.ru'},

            {'name': 'domain_sid',
             'value': 'jwtKRR52_jUcQfug3aJ738719739449',
             'domain': '.gitflic.ru'},

            {'name': 'mdd',
             'value': '0',
             'domain': '.gitflic.ru'}
        ]

        # Данные Пользователя 2
        user2_cookies = [
            {'name': 'SESSION',
             'value': 'MDRiOWY1ZTAtYTI4Yi00ZWE4LTlmNWMtY2IxMTVmMzI0NjUx',
             'domain': '.gitflic.ru'},

            {'name': 'X-CSRF-TOKEN',
             'value': '57e81057-26eb-480c-8c2c-3cf9701633aa',
             'domain': '.gitflic.ru'},

            {'name': 'domain_sid',
             'value': 'jPut8KRIS2jR_uK1Qicuc%3A1787397199449',
             'domain': '.gitflic.ru'},

            {'name': 'mdd',
             'value': '0',
             'domain': '.gitflic.ru'}
        ]

        # 2. Установите cookie пользователя 1
        driver.delete_all_cookies()
        for cookie in user1_cookies:
            driver.add_cookie(cookie)

        # 3. Обновите страницу
        driver.refresh()

        # Ждем загрузки страницы после обновления
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 4. Перейдите на страницу пользователя 1
        driver.get("https://gitflic.ru/user/olga17670")

        # Ждем загрузки страницы профиля
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 5. Сохраните текущий URL
        url_user1 = driver.current_url
        print(f"URL пользователя 1: {url_user1}")

        # 6. Разлогиньтесь (очистите куки)
        driver.delete_all_cookies()

        # 7. Установите cookie пользователя 2
        for cookie in user2_cookies:
            driver.add_cookie(cookie)

        # 8. Обновите страницу
        driver.refresh()

        # Ждем загрузки страницы после обновления
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 9. Перейдите на страницу пользователя 2
        driver.get("https://gitflic.ru/user/helga176701")

        # Ждем загрузки страницы профиля
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # 10. Сохраните текущий URL
        url_user2 = driver.current_url
        print(f"URL пользователя 2: {url_user2}")

        # 11.URL для пользователя 1 и пользователя 2 различаются
        assert url_user1 != url_user2, \
            f"URLs should be different for different users\
            , but both are: {url_user1}"

        print("Test passed successfully! URLs are different.")

    finally:
        driver.quit()
