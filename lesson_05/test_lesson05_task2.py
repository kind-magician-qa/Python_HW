# Шаги:
# Откройте страницу https://httpbin.qa-territory.online/forms/post.
# Найдите поле ввода с названием custname.(By.ID, "custname")
# Введите в него ваше имя.
# Найдите кнопку Submit и нажмите на нее.
# Проверьте, что после нажатия URL изменился.


from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    try:
        # Открываем страницу.
        driver.get("https://httpbin.qa-territory.online/forms/post")
        # Находим поле ввода по custname.
        name_field = driver.find_element(By.ID, "custname")
        # Вводим данные в поле ввода.
        name_field.send_keys("Владимир Калягин")
        # Находим кнопку отправки данных Submit.
        submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
        # Кликаем по кнопке.
        submit_btn.click()
        # Проверяем, что после нажатия URL изменился.
        first_url = "https://httpbin.qa-territory.online/forms/post"
        assert driver.current_url != first_url, (
            f"Неожиданно, URL не изменился {driver.current_url}"
        )
    finally:
        driver.quit()
