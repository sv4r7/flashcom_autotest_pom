import allure
from utilities.utils import get_driver
from pages.main_page_popup import MainPagePopup


@allure.description('Test Check Popup')
def test_check_popup(set_up) -> None:
    """Функция по запуску теста - проверки попапа на главной странице"""
    driver = get_driver()

    main_page_popup = MainPagePopup(driver)
    main_page_popup.check_popup()

    driver.quit()
