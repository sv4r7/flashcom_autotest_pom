from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from base.base_class import Base
from utilities.logger import Logger


class OrderingPageLogistics(Base):
    """Класс страницы оформления доставки заказа"""

    TEST_WORDS: str = 'Оформление заказа'
    TEST_URL: str = 'https://flashcom.ru/order/index.php?CurrentStep=2'

    # Locators

    test_words_path: str = '//h1[@class="page__title"]'

    # Getters

    def get_test_words(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.test_words_path))
        )

    # Methods

    def ordering_logistics(self) -> None:
        Logger.add_start_step(method='ordering_logistics')
        self.get_current_url()
        self.assert_word(self.get_test_words(),
                         self.TEST_WORDS,
                         'Ordering Test Word Value')
        self.assert_url(self.TEST_URL, 'Ordering Page Logistics')
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='ordering_logistics')
