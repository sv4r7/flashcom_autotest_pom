from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from base.base_class import Base


class FilteredNotebookPage(Base):

    TEST_URL: str = ('https://flashcom.ru/market/noutbuki/Lenovo/'
                     'filter_priceTo-90000|note_diag-14|3775-Intel%20Core%20i3|1469-'
                     'Intel%20UHD%20Graphics|FILTR_OPERATIVNAYA_PAMYAT_GB-8/')
    NOTEBOOK_VENDOR_CODE: str = 'Артикул 359808'
    NOTEBOOK_PRICE: str = '83 390 ₽'

    # Locators

    vendor_code_path: str = '//*[@id="listing-grid"]/div[3]/div/span[2]'
    notebook_price_path: str = '//*[@id="listing-grid"]/div[3]/div/div[2]/div[1]/span'
    add_to_cart_btn_path: str = '//*[@id="listing-grid"]/div[3]/div/div[2]/div[2]/button'

    # Getters

    def get_vendor_code(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.vendor_code_path))
        )

    def get_notebook_price(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.notebook_price_path))
        )

    def get_add_to_cart_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.add_to_cart_btn_path))
        )

    # Actions

    def click_add_to_cart_btn(self) -> None:
        self.get_add_to_cart_btn().click()
        print('Click Add To Cart Btn')

    # Methods

    def add_to_cart_notebook(self):
        self.get_current_url()
        self.assert_url(self.TEST_URL)
        self.assert_word(self.get_vendor_code(), self.NOTEBOOK_VENDOR_CODE)
        self.assert_word(self.get_notebook_price(), self.NOTEBOOK_PRICE)
        self.click_add_to_cart_btn()
