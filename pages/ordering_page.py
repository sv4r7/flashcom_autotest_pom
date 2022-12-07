from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from base.base_class import Base
from utilities.logger import Logger
from utilities.utils import check_exist_by_path


class OrderingPage(Base):
    """Класс страницы оформления заказа интернет-магазина"""

    TEST_WORDS: str = 'Оформление заказа'
    INDIVIDUAL_RADIO_BTN_TEXT: str = 'Физическое лицо'
    USER_NAME_ERROR_TEXT: str = 'Укажите имя получателя заказа'
    USER_PHONE_ERROR_TEXT: str = 'Введите корректный номер телефона'
    USER_EMAIL_ERROR_TEXT: str = 'Введите корректный email'
    USER_NAME: str = 'Elena'
    USER_PHONE: str = '89037771717'
    USER_EMAIL: str = 'elena@troya.gr'

    # Locators

    test_words_path: str = '//h1[@class="page__title"]'
    individual_radio_btn_path: str = ('//*[@id="checkout-1"]/fieldset[1]'
                                      '/div/div/fieldset[1]/div/div[1]/label')
    user_name_input_path: str = '//input[@id="customer-name"]'
    user_name_error_text_path: str = '//label[@id="customer-name-error"]'
    user_phone_input_path: str = '//input[@id="customer-phone"]'
    user_phone_error_text_path: str = '//label[@id="customer-phone-error"]'
    user_email_input_path: str = '//input[@id="customer-email"]'
    user_email_error_text_path: str = '//label[@id="customer-email-error"]'
    submit_btn_path: str = '//*[@id="checkout-1"]/div/div/div/div/input'

    # Getters

    def get_test_words(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.test_words_path))
        )

    def get_individual_radio_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.individual_radio_btn_path))
        )

    def get_user_name_input(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.user_name_input_path))
        )

    def get_user_phone_input(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.user_phone_input_path))
        )

    def get_user_email_input(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.user_email_input_path))
        )

    def get_user_name_error(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.user_name_error_text_path))
        )

    def get_user_phone_error(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.user_phone_error_text_path))
        )

    def get_user_email_error(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.user_email_error_text_path))
        )

    def get_submit_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.submit_btn_path))
        )

    # Actions

    def click_individual_radio_btn(self) -> None:
        self.get_individual_radio_btn().click()
        print('Click Individual Radio Btn')

    def input_user_name(self) -> None:
        self.get_user_name_input().send_keys(self.USER_NAME)
        print('Input User Name')

    def input_user_phone(self) -> None:
        self.get_user_phone_input().send_keys(self.USER_PHONE)
        print('Input User Phone')

    def input_user_email(self) -> None:
        self.get_user_email_input().send_keys(self.USER_EMAIL)
        print('Input User Email')

    def click_submit_btn(self) -> None:
        self.get_submit_btn().click()
        print('Click Submit Btn')

    def user_information_input(self) -> None:
        self.input_user_name()
        self.input_user_phone()
        self.input_user_email()

    def check_input_errors(self) -> None:
        if check_exist_by_path(self.driver, self.user_name_error_text_path):
            try:
                self.assert_word(self.get_user_name_error(),
                                 self.USER_NAME_ERROR_TEXT,
                                 'User Name Error Value')
            except AssertionError:
                print('Check User Name Input')
        elif check_exist_by_path(self.driver, self.user_phone_error_text_path):
            try:
                self.assert_word(self.get_user_phone_error(),
                                 self.USER_PHONE_ERROR_TEXT,
                                 'User Phone Error Value')
            except AssertionError:
                print('Check User Phone Input')
        elif check_exist_by_path(self.driver, self.user_email_error_text_path):
            try:
                self.assert_word(self.get_user_email_error(),
                                 self.USER_EMAIL_ERROR_TEXT,
                                 'User Email Error Value')
            except AssertionError:
                print('Check User Email Input')

    # Methods

    def ordering(self) -> None:
        Logger.add_start_step(method='ordering')
        self.get_current_url()
        self.assert_word(self.get_test_words(),
                         self.TEST_WORDS,
                         'Ordering Test Word Value')
        self.click_individual_radio_btn()
        self.assert_word(self.get_individual_radio_btn(),
                         self.INDIVIDUAL_RADIO_BTN_TEXT,
                         'Individual Radio Btn Value')
        self.user_information_input()
        self.click_submit_btn()
        self.check_input_errors()
        Logger.add_end_step(url=self.driver.current_url, method='ordering')
