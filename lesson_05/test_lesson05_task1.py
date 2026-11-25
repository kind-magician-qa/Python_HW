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
    # Переход на страницу
    driver.get("https://httpbin.qa-territory.online/")
    # Нахождение ссылки
    html_Form = driver.find_element(By.LINK_TEXT, "HTML Form")
    # Клик по ссылке
    html_Form.click()
    # Проверен переход URL на /forms/post.
    expected_url = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url == expected_url
    # Возврат на главную страницу через driver.back()
    driver.back()
    # Проверка исходного URL после возврата
    expected_url = "https://httpbin.qa-territory.online/"
    assert driver.current_url == expected_url

    driver.quit()
