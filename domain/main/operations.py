import numpy as np
from loguru import logger


def create_canvas(w, h):
    matrix = np.array([[' ' for x in range(int(w))] for y in range(int(h))])
    return matrix


def create_line(mat, x0, y0, x1, y1, write=False):
    if not (0 <= x0 < mat.shape[0] and 0 <= x1 < mat.shape[0] and
            0 <= y0 < mat.shape[1] and 0 <= y1 < mat.shape[1]):
        raise ValueError('Invalid coordinates.')
    if (x0, y0) == (x1, y1):
        mat[x0, y0] = 'x'
        return mat
    # Swap axes if Y slope is smaller than X slope
    transpose = abs(x1 - x0) < abs(y1 - y0)
    if transpose:
        mat = mat.T
        x0, y0, x1, y1 = y0, x0, y1, x1
    # Swap line direction to go left-to-right if necessary
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0
    # Write line ends
    mat[x0, y0] = 'x'
    mat[x1, y1] = 'x'
    # Compute intermediate coordinates using line equation
    x = np.arange(x0 + 1, x1)
    y = np.round(((y1 - y0) / (x1 - x0)) * (x - x0) + y0).astype(x.dtype)
    # Write intermediate coordinates
    mat[x, y] = 'x'
    # write_data(mat if not transpose else mat.T) if write else logger.info('no need to print')
    return mat if not transpose else mat.T


def create_rectangle(mat, x1, y1, x2, y2):
    upper_left_x = x1
    upper_left_y = y1

    upper_rigth_x = x1
    upper_rigth_y = y2

    lower_rigth_x = x2
    lower_rigth_y = y2

    lower_left_x = x2
    lower_left_y = y1

    create_line(mat, upper_left_x, upper_left_y, upper_rigth_x, upper_rigth_y)
    create_line(mat, upper_rigth_x, upper_rigth_y, lower_rigth_x, lower_rigth_y)
    create_line(mat, lower_rigth_x, lower_rigth_y, lower_left_x, lower_left_y)
    create_line(mat, lower_left_x, lower_left_y, upper_left_x, upper_left_y, True)
    return mat


def fill_area_util(matrix, x, y, prevC, newC):
    rows = len(matrix)
    columns = len(matrix[0])

    if x < 0 or x >= columns or y < 0 or y >= rows or matrix.item((y, x)) != prevC or matrix.item((y, x)) == newC:
        return matrix
    matrix[y, x] = newC
    # Recur for north, east, south and west
    fill_area_util(matrix, x + 1, y, prevC, newC)
    fill_area_util(matrix, x - 1, y, prevC, newC)
    fill_area_util(matrix, x, y + 1, prevC, newC)
    fill_area_util(matrix, x, y - 1, prevC, newC)


def fill_area(mat, x, y, newC):
    prevC = mat.item((y, x))

    fill_area_util(mat, x, y, prevC, newC)

    return mat


def write_data(matrix):
    matrix_writeen = ''
    rows = len(matrix)
    columns = len(matrix[0])
    matrix_writeen += top_bottom_wrappers(columns)
    for x in range(0, rows):
        matrix_writeen += '|'
        matrix_writeen += str(matrix[x]).replace('\n', '').replace('[', '').replace(']', '').replace(',', '').replace(
            "'", '')
            # .replace('0', ' ')
        matrix_writeen += '|'
        matrix_writeen += '\n'
    matrix_writeen += top_bottom_wrappers(columns)
    return matrix_writeen


def top_bottom_wrappers(columns):
    val = ' '
    for x in range(0, columns):
        val += '- '
    val += '\n'
    return val
