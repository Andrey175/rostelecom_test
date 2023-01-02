import pytest
from selenium.webdriver.common.by import By
import time


def test_authorization():
    pytest.driver.find_element(By.ID, "username").clear()
    pytest.driver.find_element(By.ID, "username").send_keys('stvolika@yandex.ru')
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("abvA123o")
    pytest.driver.find_element(By.CSS_SELECTOR, ".rt-check-small-icon").click()
    pytest.driver.find_element(By.ID, "kc-login").click()
    time.sleep(2)
    assert pytest.driver.find_element(By.CLASS_NAME, "user-name__last-name").text == "Иванов"


def test_incorrect_name_authorization():
    pytest.driver.find_element(By.ID, "username").clear()
    pytest.driver.find_element(By.ID, "username").send_keys('stvo@yandex.ru')
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("abvA123o")
    pytest.driver.find_element(By.CSS_SELECTOR, ".rt-check-small-icon").click()
    pytest.driver.find_element(By.ID, "kc-login").click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


def test_incorrect_password_authorization():
    pytest.driver.find_element(By.ID, "username").clear()
    pytest.driver.find_element(By.ID, "username").send_keys('stvolika@yandex.ru')
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("abvA123orw")
    pytest.driver.find_element(By.CSS_SELECTOR, ".rt-check-small-icon").click()
    pytest.driver.find_element(By.ID, "kc-login").click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


def test_link_forgot_password():
    pytest.driver.find_element(By.ID, "forgot_password").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text == "Восстановление пароля"


def test_link_to_go_back():
    pytest.driver.find_element(By.ID, "forgot_password").click()
    pytest.driver.find_element(By.ID, "reset-back").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text == "Авторизация"


def test_correct_values_the_mail_field():
    pytest.driver.find_element(By.ID, "t-btn-tab-mail").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text == "Электронная почта"


def test_correct_values_the_login_field():
    pytest.driver.find_element(By.ID, "t-btn-tab-login").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text == "Логин"


def test_correct_values_the_ls_field():
    pytest.driver.find_element(By.ID, "t-btn-tab-ls").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text == "Лицевой счёт"


def test_correct_values_the_phone_field():
    pytest.driver.find_element(By.ID, "t-btn-tab-phone").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input__placeholder").text == "Мобильный телефон"
