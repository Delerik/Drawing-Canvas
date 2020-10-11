from domain.main.file_processor import execute_consumer
from loguru import logger


def init():
    try:
        logger.info('process start')
        execute_consumer()
    except Exception as e:
        logger.critical("error during canvas_drawer service execution")
        logger.critical(e)


if __name__ == '__main__':
    init()
