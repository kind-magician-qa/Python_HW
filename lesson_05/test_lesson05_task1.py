# Шаги:
# Откройте страницу https://httpbin.qa-territory.online.
# Найдите и кликните на ссылку HTML Form.
# Проверьте, что URL изменился на /forms/post.
# Вернитесь назад на главную страницу.
# Проверьте, что вернулись на исходный URL.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_back_and_url():
    driver = webdriver.Chrome()
    try:
        # Переход на страницу
        driver.get("https://httpbin.qa-territory.online/")
        # Нахождение ссылки
        html_form = driver.find_element(By.LINK_TEXT, "HTML Form")
        # Клик по ссылке
        html_form.click()
        # Явно ждём переход на /forms/post и проверяем URL
        wait = WebDriverWait(driver, 10)
        expected_url = "https://httpbin.qa-territory.online/forms/post"
        wait.until(EC.url_to_be(expected_url))
        # Возврат на главную страницу через driver.back()
        driver.back()
        # Явно ждём возврата и проверяем исходный URL
        expected_url = "https://httpbin.qa-territory.online/"
        wait.until(EC.url_to_be(expected_url))
    finally:
        driver.quit()
