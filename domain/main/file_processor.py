import json

from consumer.main.file_handler import get_file_input_info, create_output_file, write_output_file, close_output_file
from loguru import logger

from domain.main.operations import create_canvas, create_line, create_rectangle, fill_area, write_data


def execute_consumer():
    lines = get_file_input_info()
    matrix = None
    file = create_output_file()
    for line in lines:
        if line[0] == 'C':
            logger.debug('Creating canvas')
            matrix = create_canvas(int(line.split()[1]), int(line.split()[2]))
            write_output_file(file, write_data(matrix))
        elif line[0] == 'L':
            logger.debug('Created line')
            matrix = create_line(matrix, int(line.split()[2]) - 1, int(line.split()[1]) - 1, int(line.split()[4]) - 1,
                                 int(line.split()[3]) - 1, True)
            write_output_file(file, write_data(matrix))
        elif line[0] == 'R':
            logger.debug('Created Rectangle')
            matrix = create_rectangle(matrix, int(line.split()[2]) - 1, int(line.split()[1]) - 1,
                                      int(line.split()[4]) - 1,
                                      int(line.split()[3]) - 1)
            write_output_file(file, write_data(matrix))
        elif line[0] == 'B':
            logger.debug('Created Filled area')
            matrix = fill_area(matrix, int(line.split()[1]) - 1, int(line.split()[2]) - 1, line.split()[3])
            write_output_file(file, write_data(matrix))
    close_output_file(file)
