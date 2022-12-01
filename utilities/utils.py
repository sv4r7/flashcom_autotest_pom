from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver


def get_driver() -> WebDriver:

    s: Service = Service('~/PycharmProjects/resource/geckodriver')
    driver: WebDriver = webdriver.Firefox(service=s)
    base_url: str = 'https://flashcom.ru/'
    driver.get(base_url)
    driver.maximize_window()
    return driver
