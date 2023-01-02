import time
import pytest
from selenium.webdriver.common.by import By


def test_incorrect_name_1cyrillic():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.NAME, "firstName").clear()
    pytest.driver.find_element(By.NAME, "firstName").send_keys("a")
    pytest.driver.find_element(By.NAME, "lastName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_incorrect_name_31cyrillic():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.NAME, "firstName").clear()
    pytest.driver.find_element(By.NAME, "firstName").send_keys("aбвгдеёжзийклмнопрстуфхцчшщьъяы")
    pytest.driver.find_element(By.NAME, "lastName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_incorrect_surname_2latin():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.NAME, "lastName").clear()
    pytest.driver.find_element(By.NAME, "lastName").send_keys("Ki")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_incorrect_surname_30latin():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.NAME, "lastName").clear()
    pytest.driver.find_element(By.NAME, "lastName").send_keys("qwertyuiopasdfghjklzxcvbnmqwer")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


def test_incorrect_mail():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "address").clear()
    pytest.driver.find_element(By.ID, "address").send_keys("podyandex.ru")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


def test_incorrect_phone():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "address").clear()
    pytest.driver.find_element(By.ID, "address").send_keys("23456711133")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


def test_password_field_incorrect_4latin_and_4cyrillic():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("gNLsпгУЭ")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать только латинские буквы"


def test_password_field_incorrect_8characters_latin():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("#!$^&(%*")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать хотя бы одну заглавную букву"


def test_password_field_incorrect_uppercase_and_characters_latin():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("A1B#C%D*")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать хотя бы одну прописную букву"


def test_password_field_incorrect_8latin():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("dfghjkla")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"


def test_password_field_incorrect_1latin():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("d")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Длина пароля должна быть не менее 8 символов"


def test_password_config_incorrect_field_4_digits():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("1234")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Длина пароля должна быть не менее 8 символов"


def test_password_config_incorrect_field_9_digits():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("123456789")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать хотя бы одну заглавную букву"


def test_password_config_incorrect_8letters_cyrillic():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("абвгдежзи")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать только латинские буквы"


def test_password_config_incorrect_8uppercase_latin():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("DFGHJKLOIU")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"


def test_password_config_incorrect_8uppercase_latin_plus_character():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("DFGHJKL3")
    pytest.driver.find_element(By.NAME, "firstName").click()
    assert pytest.driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == \
           "Пароль должен содержать хотя бы одну прописную букву"


def test_registration_correct():
    pytest.driver.find_element(By.ID, "kc-register").click()
    pytest.driver.find_element(By.NAME, "firstName").clear()
    pytest.driver.find_element(By.NAME, "firstName").send_keys("Коля")
    pytest.driver.find_element(By.NAME, "lastName").clear()
    pytest.driver.find_element(By.NAME, "lastName").send_keys("Тихонов")
    pytest.driver.find_element(By.CSS_SELECTOR, ".rt-select__arrow").click()
    pytest.driver.find_element(By.CSS_SELECTOR, ".rt-select__list-item:nth-child(4)").click()
    pytest.driver.find_element(By.ID, "address").clear()
    pytest.driver.find_element(By.ID, "address").send_keys("pkmen@yex.ru")
    pytest.driver.find_element(By.ID, "password").clear()
    pytest.driver.find_element(By.ID, "password").send_keys("abvA123or")
    pytest.driver.find_element(By.CSS_SELECTOR, ".new-password-container__password .rt-base-icon").click()
    pytest.driver.find_element(By.ID, "password-confirm").clear()
    pytest.driver.find_element(By.ID, "password-confirm").send_keys("abvA123or")
    pytest.driver.find_element(By.NAME, "register").click()
    time.sleep(2)
    assert pytest.driver.find_element(By.CLASS_NAME, "card-container__title").text == "Подтверждение email"
    pytest.driver.close()
