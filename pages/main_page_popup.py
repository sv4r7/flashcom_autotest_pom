import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from base.base_class import Base
from utilities.logger import Logger


class MainPagePopup(Base):
    """Класс попапа для кнопки логина на главной странице интернет-магазина"""

    TEST_WORD_LOGIN_POPUP: str = 'Войти'
    TEST_WORD_REGISTRATION: str = 'Регистрация'

    # Locators

    main_page_login_btn: str = '/html/body/header/div[2]/div/div/div[2]/a[1]/span'
    test_word_login_popup_path: str = '//*[@id="popup-login"]/p'
    test_word_login_popup_second_check_path: str = '//*[@id="popup-undefined"]/p'
    test_word_registration_popup_path: str = '//*[@id="popup-registration"]/p'
    popup_registration_btn: str = '//a[@class="registration-trigger"]'
    popup_login_btn: str = '//a[@class="login-trigger"]'

    # Getters

    def get_main_page_login_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.main_page_login_btn))
        )

    def get_test_word_login_popup(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.test_word_login_popup_path))
        )

    def get_test_word_login_popup_second_check(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH,
                                        self.test_word_login_popup_second_check_path))
        )

    def get_test_word_registration_popup(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.test_word_registration_popup_path))
        )

    def get_popup_registration_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.popup_registration_btn))
        )

    def get_popup_login_btn(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.popup_login_btn))
        )

    # Actions

    def click_main_page_login_btn(self) -> None:
        self.get_main_page_login_btn().click()
        print('Click Main Page Login Btn')

    def click_popup_registration_btn(self) -> None:
        self.get_popup_registration_btn().click()
        print('Click Popup Registration Btn')

    def click_popup_login_btn(self) -> None:
        self.get_popup_login_btn().click()
        print('Click Popup Login Btn')

    def check_test_words(self) -> None:
        try:
            self.assert_word(self.get_test_word_login_popup(),
                             self.TEST_WORD_LOGIN_POPUP,
                             'Login Popup Test Word')
        except AssertionError:
            print('Login Popup Assertion Error')
            self.get_screenshot()
        try:
            self.click_popup_registration_btn()
            self.assert_word(self.get_test_word_registration_popup(),
                             self.TEST_WORD_REGISTRATION,
                             'Registration Popup Test Word')
        except AssertionError:
            print('Registration Popup Assertion Error')
            self.get_screenshot()
        try:
            self.click_popup_login_btn()
            self.assert_word(self.get_test_word_login_popup_second_check(),
                             self.TEST_WORD_LOGIN_POPUP,
                             'Login Popup Test Word')
        except AssertionError:
            print('Login Popup Assertion Error')
            self.get_screenshot()

    # Methods

    def check_popup(self) -> None:
        with allure.step('Check Popup'):
            Logger.add_start_step(method='check_popup')
            self.get_current_url()
            self.click_main_page_login_btn()
            self.check_test_words()
            Logger.add_end_step(url=self.driver.current_url, method='check_popup')
