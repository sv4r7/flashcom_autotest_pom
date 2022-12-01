from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from base.base_class import Base


class MainPage(Base):
    """Класс главной страницы интернет-магазина"""

    TEST_WORDS: str = 'Популярные категории'

    # Locators

    test_words_path: str = '//h2[@class="content-section__title"]'
    catalog_btn: str = '//button[@class="cd-trigger"]'
    notebooks_link: str = '//*[@id="cd"]/div/div/div/div[2]/div[1]/ul/li[2]/a'
    notebooks_filter: str = '//*[@id="cd-subcategory-4861"]/ul/li[2]/ul/li[1]/a'

    # Getters

    def get_test_words(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, self.test_words_path))
            )
    
    def get_catalog_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, self.catalog_btn))
            )
    
    def get_notebooks_link(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, self.notebooks_link))    
            )

    def get_notebooks_filter(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, self.notebooks_filter))
            )

    # Actions

    def click_catalog_btn(self) -> None:
        self.get_catalog_btn().click()
        print('Click Catalog Btn')

    def click_notebooks_link(self) -> None:
        self.get_notebooks_link().click()
        print('Click Notebooks Link')

    def click_notebooks_filter(self) -> None:
        self.get_notebooks_filter().click()
        print('Click Notebooks Filter')

    # Methods

    def go_to_notebooks_page(self) -> None:
        self.get_current_url()
        self.assert_word(self.get_test_words(), self.TEST_WORDS)
        self.click_catalog_btn()
        self.click_notebooks_link()
        self.click_notebooks_filter()
