import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture()
def set_up():
    print('Start Test')
    s: Service = Service('~/PycharmProjects/resource/geckodriver')
    driver: WebDriver = webdriver.Firefox(service=s)
    base_url: str = 'https://flashcom.ru/'
    driver.get(base_url)
    driver.maximize_window()
    yield
    driver.quit()
    print('Finish Test')
