from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#finish h4"), "Hello World!")
        )

        # Получаем текст элемента
        hello_text_element = driver.find_element(By.CSS_SELECTOR, "#finish h4")
        actual_text = hello_text_element.text

        driver.save_screenshot("dynamic_loading_screenshot.png")

        assert actual_text == "Hello World!", \
            f"Expected text 'Hello World!', but got '{actual_text}'"

        print("Test passed successfully!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()
