from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


DRIVER_PATH = "C:\\Python\\Webdriver\\chromedriver_win32\\chromedriver.exe"


def test_vowels_form_new_text_4button():
    #chrome_driver = webdriver.Chrome(DRIVER_PATH)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.get("https://rioran.github.io/ru_vowels_filter/main.html")
    driver.maximize_window()
    sleep(2)
    #title = "Sample page - Filter for vowels"
    #assert title == chrome_driver.title
    driver.find_element(By.ID, "text_input").click()
    sleep(2)
    driver.find_element(By.ID, "text_input").clear()
    sleep(2)
    driver.find_element(By.ID, "text_input").send_keys("Белеет парус одинокой")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "html").click()
    sleep(2)
    #print("\n\nOUTPUT_STR:", output_str, "\n\n")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    sleep(2)

    driver.quit()