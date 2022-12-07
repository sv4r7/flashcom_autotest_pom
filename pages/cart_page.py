from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from base.base_class import Base
from utilities.logger import Logger
from utilities.utils import strip_price, get_overall_price, get_test_price


class CartPage(Base):
    """Класс корзины интернет-магазина"""

    TEST_WORD: str = 'Корзина'
    NOTEBOOK_VENDOR_CODE: str = 'Артикул 359808'
    NOTEBOOK_PRICE: str = '84 920 ₽'
    OVERALL_PRICE: str = '84 920 ₽'

    # Locators

    test_word_path: str = '//h1[@class="page__title"]'
    vendor_code_path: str = '/html/body/main/article/section/div/div/form/fieldset/table/tbody/tr/td[1]/a/span[1]'
    notebook_price_path: str = '//div[@class="cart-row__price"]'
    price_overall_path: str = '/html/body/main/article/section/div/div/form/fieldset/table/tfoot/tr/td[3]'
    submit_btn_path: str = '/html/body/main/article/section/div/div/form/div[2]/div/button'

    # Getters

    def get_test_word(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.test_word_path))
        )

    def get_vendor_code(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.vendor_code_path))
        )

    def get_notebook_price(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.notebook_price_path))
        )

    def get_overall_cart_price(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.price_overall_path))
        )

    def get_submit_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.submit_btn_path))
        )

    # Actions

    def click_submit_btn(self) -> None:
        self.get_submit_btn().click()
        print('Click Submit Btn')

    def check_price(self) -> str:
        stripped_price: str = strip_price(self.get_notebook_price().text)
        overall_price: str = get_overall_price(stripped_price)
        total: str = get_test_price(overall_price)
        return total

    # Methods

    def confirm_order(self) -> None:
        Logger.add_start_step(method='confirm_order')
        self.get_current_url()
        self.assert_word(self.get_test_word(),
                         self.TEST_WORD,
                         'Basket Test Word Value')
        self.assert_word(self.get_vendor_code(),
                         self.NOTEBOOK_VENDOR_CODE,
                         'Basket Vendor Code Value')
        self.assert_word(self.get_notebook_price(),
                         self.NOTEBOOK_PRICE,
                         'Basket Price Value')
        self.assert_func(self.check_price(),
                         self.OVERALL_PRICE,
                         'Basket Overall Price Value')
        self.assert_func(self.check_price(),
                         self.get_overall_cart_price().text,
                         'Basket Overall Price Value - Value From Site')
        self.click_submit_btn()
        Logger.add_end_step(url=self.driver.current_url, method='confirm_order')
