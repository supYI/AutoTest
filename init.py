import os
import logging

# 获取脚本所在目录
project_dir = os.path.dirname(os.path.abspath(__file__))


def logging_info(message):
    # create logger
    logger = logging.getLogger('info')
    logger.setLevel(logging.INFO)

    # create console handler and set level to info
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # create file handler and set level to debug
    fileHandler = logging.FileHandler('D:\\Appium\\AppiumTest.log', mode='w+')
    fileHandler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s : %(message)s')

    # add formatter to console & file handler
    console.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # add console & handler to logger
    if not logger.handlers:
        logger.addHandler(console)
        logger.addHandler(fileHandler)

    logger.info(message)

    # 清除句柄，防止重复打印
    # logger.removeHandler(console)
    # logger.removeHandler(fileHandler)


def logging_error(message):
    # create logger
    logger = logging.getLogger('error')
    logger.setLevel(logging.ERROR)

    # create console handler and set level to ERROR
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)

    # create file handler and set level to debug
    fileHandler = logging.FileHandler('D:\\Appium\\AppiumTest.log', mode='w+')
    fileHandler.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s : %(message)s')

    # add formatter to console & file handler
    console.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    # add console handler to logger
    if not logger.handlers:
        logger.addHandler(console)
        logger.addHandler(fileHandler)

    logger.error(message)

    # logger.removeHandler(console)
    # logger.removeHandler(fileHandler)


# logging_info('hello')
# logging_info('world')
# logging_info('hello')
# logging_info('world')