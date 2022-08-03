from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium import webdriver


DRIVER_PATH = "C:\\Python\\Webdriver\\chromedriver_win32\\chromedriver.exe"


def test_vowels_form_toogle():
    #chrome_driver = webdriver.Chrome(DRIVER_PATH)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
        # iPhone    11    Pro    dimensions
    set_device_metrics_override=dict({
        "width": 175,
        "height": 812,
        "deviceScaleFactor": 50,
        "mobile": True
    })
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', set_device_metrics_override)
    driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    sleep(5)

    driver.quit()