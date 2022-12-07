import allure
from utilities.utils import get_driver
from pages.main_page import MainPage
from pages.notebooks_page import NotebookPage
from pages.filtered_notebooks_page import FilteredNotebookPage
from pages.cart_page import CartPage
from pages.ordering_page import OrderingPage
from pages.ordering_page_logistics import OrderingPageLogistics


@allure.description('Test Buy Notebook')
def test_buy_notebook(set_up) -> None:
    """Функция по запуску теста - покупка ноутбука"""
    driver = get_driver()

    main_page = MainPage(driver)
    main_page.go_to_notebooks_page()

    notebook_page = NotebookPage(driver)
    notebook_page.select_notebook_filters()

    filtered_notebook_page = FilteredNotebookPage(driver)
    filtered_notebook_page.add_to_cart_notebook()

    cart_page = CartPage(driver)
    cart_page.confirm_order()

    ordering_page = OrderingPage(driver)
    ordering_page.ordering()

    ordering_page_logistics = OrderingPageLogistics(driver)
    ordering_page_logistics.ordering_logistics()

    driver.quit()
