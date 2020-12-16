import inspect

import pytest
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestBase:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # define the file handler name
        file_handler = logging.FileHandler(logger_name + ".log", 'w', 'utf-8')

        # define the log format
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # set the format to file
        file_handler.setFormatter(log_format)

        # add handler
        logger.addHandler(file_handler)

        # set the level
        logger.setLevel(logging.INFO)

        return logger

    def explicit_wait_for_link_text(self, link_text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, link_text)))




