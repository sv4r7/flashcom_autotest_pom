import datetime as dt
import os


class Logger:
    DATE_NOW: dt = dt.datetime.now()
    FORMAT: str = '%Y-%m-%d_%H-%M-%S'

    file_name = f'/Users/5v4r7/PycharmProjects/flashcom_autotest_pom/logs/log_{DATE_NOW.strftime(FORMAT)}.log '

    @classmethod
    def write_log_to_file(cls, data: str) -> None:
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str) -> None:
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Start time: {str(dt.datetime.now())}\n'
        data_to_add += f'Start name method: {method}\n'
        data_to_add += '\n'

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str) -> None:

        data_to_add = f'End time: {str(dt.datetime.now())}\n'
        data_to_add += f'End name method: {method}\n'
        data_to_add += f'URL: {url}\n'
        data_to_add += f'\n-----\n'

        cls.write_log_to_file(data_to_add)
