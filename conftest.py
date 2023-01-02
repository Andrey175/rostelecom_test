import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


@pytest.fixture(autouse=True)
def inter_authorization():
    pytest.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get("https://b2c.passport.rt.ru")
    WebDriverWait(pytest.driver, 10).until(es.presence_of_element_located((By.ID, "app-header")))
    pytest.driver.set_window_size(1550, 878)
    pytest.driver.implicitly_wait(15)

    yield

    pytest.driver.quit()
