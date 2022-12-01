import datetime as dt


class Base:

    FORMAT: str = '%Y.%m.%d.%H.%M.%S'
    LOCAL_SCREENSHOT_PATH: str = '/Users/5v4r7/PycharmProjects/flashcom_autotest_pom/screen'

    """Базовый класс - родитель"""
    def __init__(self, driver) -> None:
        self.driver = driver

    """Метод по получению текущего url"""
    def get_current_url(self) -> None:
        current_url: str = self.driver.current_url
        print(f'Current url {current_url}')

    """Метод по сравнению значений"""
    def assert_word(self, word, result: str) -> None:
        word_value: str = word.text
        assert word_value == result
        print('Expected Word Value - Correct Result')

    """Метод по получению скриншота"""
    def get_screenshot(self) -> None:
        now_date: str = dt.datetime.utcnow().strftime(self.FORMAT)
        name_screenshot: str = f'screenshot {now_date}.png'
        self.driver.save_screenshot(f'{self.LOCAL_SCREENSHOT_PATH}/{name_screenshot}')

    """Метод по сравнению url"""
    def assert_url(self, result) -> None:
        current_url: str = self.driver.current_url
        assert current_url == result
        print('Expected Url Value - Correct Result')

