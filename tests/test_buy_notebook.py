from utilities.utils import get_driver
from pages.main_page import MainPage


def test_buy_notebook(set_up) -> None:
    """Функция по запуску теста - покупка ноутбука"""
    driver = get_driver()

    main_page = MainPage(driver)
    main_page.go_to_notebooks_page()

    driver.quit()
