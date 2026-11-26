# Шаги:
# Откройте страницу https://httpbin.qa-territory.online.
# Найдите и кликните на ссылку HTML Form.
# Проверьте, что URL изменился на /forms/post.
# Вернитесь назад на главную страницу.
# Проверьте, что вернулись на исходный URL.

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_back_and_url():
    driver = webdriver.Chrome()
    try:
        # Переход на страницу
        driver.get("https://httpbin.qa-territory.online/")
        # Нахождение ссылки
        html_form = driver.find_element(By.LINK_TEXT, "HTML Form")
        # Клик по ссылке
        html_form.click()
        # Проверен переход URL на /forms/post.
        expected_url = "https://httpbin.qa-territory.online/forms/post"
        assert driver.current_url == expected_url
        # Возврат на главную страницу через driver.back()
        driver.back()
        # Проверка исходного URL после возврата
        expected_url = "https://httpbin.qa-territory.online/"
        assert driver.current_url == expected_url, (
            f"Ожидался URL {expected_url}, но получен {driver.current_url}"
        )
    finally:
        driver.quit()
