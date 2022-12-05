from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from base.base_class import Base


class NotebookPage(Base):
    """Класс страницы с ноутбуками"""

    TEST_WORD: str = 'Ноутбуки'
    INPUT_RANGE_FIELD_VALUE: int = 90000
    RANGE_FIELD_VALUE: str = '90000'
    MANUFACTURER_TEST_WORD: str = 'Lenovo'
    SCREEN_TEST_VALUE: str = '14'
    PROCESSOR_TEST_VALUE: str = 'Intel Core i3'
    VIDEO_CARD_TEST_VALUE: str = 'Intel UHD Graphics'
    MEMORY_TEST_VALUE: str = '8'

    # Locators

    test_word_path: str = '//h1[@class="page__title"]'
    input_range_max_path: str = '//input[@id="range-max-1"]'
    manufacturer_test_word_path: str = '//label[@for="form-listing-13"]'
    screen_test_value_path: str = '//label[@for="form-listing-18"]'
    processor_test_value_path: str = '//label[@for="form-listing-32"]'
    video_card_test_value_path: str = '//label[@for="form-listing-53"]'
    memory_test_value_path: str = '//label[@for="form-listing-72"]'
    submit_btn_path: str = '//*[@id="form-listing-filters"]/fieldset[16]/div/div[1]/button'

    @staticmethod
    def on_click_element(driver: WebDriver, element: WebElement) -> None:
        driver.execute_script('arguments[0].click();', element)

    @staticmethod
    def scroll_into_view(driver: WebDriver, element: WebElement) -> None:
        driver.execute_script('arguments[0].scrollIntoView(true);', element)

    # Getters
    
    def get_test_word(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.test_word_path))
        )

    def get_range_field(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.input_range_max_path))
        )

    def get_manufacturer_test_word(self) -> WebElement:
        return WebDriverWait(self.driver, 10). until(
            ec.element_to_be_clickable((By.XPATH, self.manufacturer_test_word_path))
        )
    
    def get_screen_test_value(self) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.screen_test_value_path))
        )

    def get_processor_test_value(self) -> WebElement:   
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.processor_test_value_path))
        )

    def get_video_card_test_value(self) -> WebElement:   
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.video_card_test_value_path))
        )

    def get_memory_test_value(self) -> WebElement:   
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.memory_test_value_path))
        )

    def get_submit_btn(self) -> WebElement:   
        return WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, self.submit_btn_path))
        )

    # Actions

    def input_range_field(self) -> None:
        self.get_range_field().click()
        self.get_range_field().send_keys(Keys.COMMAND + 'a')
        self.get_range_field().send_keys(Keys.DELETE)
        self.get_range_field().send_keys(self.INPUT_RANGE_FIELD_VALUE)
        print('Input Range Field Value')

    def click_manufacturer_checkbox(self) -> None:
        try:
            self.scroll_into_view(self.driver, self.get_manufacturer_test_word())
            action: ActionChains = ActionChains(self.driver)
            action.move_to_element(self.get_manufacturer_test_word()).click().perform()
        except MoveTargetOutOfBoundsException:
            self.on_click_element(self.driver, self.get_manufacturer_test_word())
        print('Click Manufacturer Checkbox')

    def click_screen_checkbox(self) -> None:
        try:
            self.scroll_into_view(self.driver, self.get_screen_test_value())
            action: ActionChains = ActionChains(self.driver)
            action.move_to_element(self.get_screen_test_value()).click().perform()
        except MoveTargetOutOfBoundsException:
            self.on_click_element(self.driver, self.get_screen_test_value())
        print('Click Screen Size Checkbox')

    def click_processor_checkbox(self) -> None:
        try:
            self.scroll_into_view(self.driver, self.get_processor_test_value())
            action: ActionChains = ActionChains(self.driver)
            action.move_to_element(self.get_processor_test_value()).click().perform()
        except MoveTargetOutOfBoundsException:
            self.on_click_element(self.driver, self.get_processor_test_value())
        print('Click Processor Checkbox')

    def click_video_card_checkbox(self) -> None:
        try:
            self.scroll_into_view(self.driver, self.get_video_card_test_value())
            action: ActionChains = ActionChains(self.driver)
            action.move_to_element(self.get_video_card_test_value()).click().perform()
        except MoveTargetOutOfBoundsException:
            self.on_click_element(self.driver, self.get_video_card_test_value())
        print('Click Video Card Checkbox')

    def click_memory_checkbox(self) -> None:
        try:
            self.scroll_into_view(self.driver, self.get_memory_test_value())
            action: ActionChains = ActionChains(self.driver)
            action.move_to_element(self.get_memory_test_value()).click().perform()
        except MoveTargetOutOfBoundsException:
            self.on_click_element(self.driver, self.get_memory_test_value())
        print('Click Memory Checkbox')

    def click_submit_btn(self) -> None:
        try:
            self.get_submit_btn().click()
        except MoveTargetOutOfBoundsException:
            self.on_click_element(self.driver, self.get_submit_btn())
        print('Click Submit Btn')

    # Methods

    def select_notebook_filters(self):
        self.get_current_url()
        self.assert_word(self.get_test_word(), self.TEST_WORD)
        self.input_range_field()
        self.assert_value(self.get_range_field(), self.RANGE_FIELD_VALUE)
        self.click_manufacturer_checkbox()
        self.assert_word(self.get_manufacturer_test_word(), self.MANUFACTURER_TEST_WORD)
        self.click_screen_checkbox()
        self.assert_word(self.get_screen_test_value(), self.SCREEN_TEST_VALUE)
        self.click_processor_checkbox()
        self.assert_word(self.get_processor_test_value(), self.PROCESSOR_TEST_VALUE)
        self.click_video_card_checkbox()
        self.assert_word(self.get_video_card_test_value(), self.VIDEO_CARD_TEST_VALUE)
        self.click_memory_checkbox()
        self.assert_word(self.get_memory_test_value(), self.MEMORY_TEST_VALUE)
        self.click_submit_btn()
