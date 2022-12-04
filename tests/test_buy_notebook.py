from utilities.utils import get_driver
from pages.main_page import MainPage
from pages.notebooks_page import NotebookPage
from pages.filtered_notebooks_page import FilteredNotebookPage


def test_buy_notebook(set_up) -> None:
    """Функция по запуску теста - покупка ноутбука"""
    driver = get_driver()

    main_page = MainPage(driver)
    main_page.go_to_notebooks_page()

    notebook_page = NotebookPage(driver)
    notebook_page.select_notebook_filters()

    filtered_notebook_page = FilteredNotebookPage(driver)
    filtered_notebook_page.add_to_cart_notebook()

    driver.quit()
