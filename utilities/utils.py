import re
from typing import List
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver


def get_driver() -> WebDriver:

    s: Service = Service('~/PycharmProjects/resource/geckodriver')
    driver: WebDriver = webdriver.Firefox(service=s)
    base_url: str = 'https://flashcom.ru/'
    driver.get(base_url)
    driver.maximize_window()
    return driver


def strip_price(string: str) -> str:
    """Функция возвращает строку цены без пробелов и знака валюты"""
    pattern: str = '["₽" | " " ]'
    refactored_string: str = re.sub(pattern, '', string)
    stripped_price_string: str = ''.join(refactored_string)
    return stripped_price_string


def get_overall_price(*args: str) -> str:
    """Функция возвращает строку полученную путем сложения числовых эквивалентов цен"""
    if len(args) == 1:
        price: str = args[0]
        return price
    int_price: int = sum(list(map(lambda x: int(x), args)))
    return str(int_price)


def get_test_price(string: str) -> str:
    """Функция возвращает цену к формату, который мы получаем на сайте"""
    separator = ''
    changed_list: List[str] = list(string)
    if len(string) == 3:
        changed_list.insert(3, ' ')
        changed_list.insert(4, '₽')
    elif len(string) == 4:
        changed_list.insert(1, ' ')
        changed_list.insert(5, ' ')
        changed_list.insert(6, '₽')
    elif len(string) == 5:
        changed_list.insert(2, ' ')
        changed_list.insert(7, ' ')
        changed_list.insert(8, '₽')
    elif len(string) == 6:
        changed_list.insert(3, ' ')
        changed_list.insert(8, ' ')
        changed_list.insert(9, '₽')
    elif len(string) == 7:
        changed_list.insert(1, ' ')
        changed_list.insert(5, ' ')
        changed_list.insert(9, ' ')
        changed_list.insert(10, '₽')
    return separator.join(changed_list)


def check_exist_by_path(driver: WebDriver, path: str) -> bool:
    """Функция проверки на наличие веб-элемента в доме"""
    try:
        driver.find_element(By.XPATH, path)
    except NoSuchElementException:
        return False
    return True
