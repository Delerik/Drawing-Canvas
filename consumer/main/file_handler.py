from utils.get_config_params import config
from utils.project_utils import get_root_project_path
from loguru import logger


def get_file_input_info():
    try:

        input_file = open(get_root_project_path() + '/input.txt', 'r')

        lines = input_file.readlines()
        lines = [a.replace('\n', '').replace('\n', '\r') for a in lines]
        input_file.close()
        logger.debug('Reader from file success')
        print(lines)
        return lines
    except Exception as e:
        logger.error("error during file_reader consumer call")
        logger.error(e)
        return e


def create_output_file():
    try:

        new_path = get_root_project_path() + '/output.txt'
        new_file = open(new_path, 'w')
        logger.debug('Creation of file success')
        return new_file

    except Exception as e:
        logger.error("error during file_creator consumer call")
        logger.error(e)
        return e


def close_output_file(new_file):
    try:
        new_file.close()
        logger.debug('Closing of file success')
        return None
    except Exception as e:
        logger.error("error during file_closer consumer call")
        logger.error(e)
        return e


def write_output_file(new_file, message):
    try:
        new_file.write(message)
        logger.debug('Writing of file success')
        return new_file
    except Exception as e:
        logger.error("error during file_writer consumer call")
        logger.error(e)
        return e