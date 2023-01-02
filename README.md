
Тесты в папке tests:
test_authorization_rostelecom.py   --9 тестов страницы авторизации--запуск с коммандной строки--
--pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_authorization_rostelecom.py--

test_registration_rostelecom.py  --17 тестов страницы регистрации--запуск--
--pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_registration_rostelecom.py--

conftest.py   -- фикстура для запуска страницы авторизации ростелеком через браузер Chrome
