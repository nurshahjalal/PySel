import inspect
import logging


class LogGen:

    # @staticmethod
    # def logs():
    #     logging.basicConfig(filemode=".\\logs\\automation.log",
    #                         format="%(asctime)s: %(levelname)s:, %(messages)s",
    #                         datefmt="%m/%d/%Y %I:%M:%S %P")
    #
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger


    @staticmethod
    def logs():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # define the file handler name
        file_name = "..\\logs\\" + logger_name + ".log"
        # file_handler = logging.FileHandler(".\\logs\\" + logger_name + ".log", 'w', 'utf-8')
        file_handler = logging.FileHandler(file_name, 'w', 'utf-8')
        print(file_handler)

        # define the log format
        log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # set the format to file
        file_handler.setFormatter(log_format)

        # add handler
        logger.addHandler(file_handler)

        # set the level
        logger.setLevel(logging.INFO)

        return logger
