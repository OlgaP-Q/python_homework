import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture
def driver():
    """Фикстура Chrome WebDriver.

    :return: экземпляр Chrome WebDriver
    """
    options = ChromeOptions()
    options.add_argument("--remote-allow-origins=*")
    drv = webdriver.Chrome(options=options)
    drv.maximize_window()
    yield drv
    drv.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура Firefox WebDriver с настройками Snap.

    :return: экземпляр Firefox WebDriver
    """
    snap_tmp_dir = os.path.expanduser(
        '~/snap/firefox/common/selenium_tmp'
    )
    os.makedirs(snap_tmp_dir, exist_ok=True)
    os.environ['TMPDIR'] = snap_tmp_dir

    options = FirefoxOptions()
    options.binary_location = (
        '/snap/firefox/current/usr/lib/firefox/firefox'
    )

    drv = webdriver.Firefox(options=options)
    drv.maximize_window()

    yield drv
    drv.quit()
