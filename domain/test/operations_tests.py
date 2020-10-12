import unittest
import mock
import numpy as np

from domain.main.operations import create_canvas, create_line, create_rectangle, fill_area


# fyi https://stackoverflow.com/questions/27571429/python-how-can-i-override-a-complicated-function-during-unittest


class TestMyModule(unittest.TestCase):

    @mock.patch('domain.main.operations')
    def test_1(self, mocked):
        print('test 1')
        mocked.return_value = np.array([[' ' for x in range(int(4))] for y in range(int(20))])
        val1 = str(create_canvas(4, 20))

        self.assertEqual(val1, str(np.array([[' ' for x in range(int(4))] for y in range(int(20))])))

    @mock.patch('domain.main.operations')
    def test_2(self, mocked):
        print('test 2')
        val1 = create_line(np.array([[' ' for x in range(int(4))] for y in range(int(20))]), 1, 1, 1, 2)
        canvas = np.array([[' ' for x in range(int(4))] for y in range(int(20))])
        canvas[1, 1] = 'x'
        canvas[1, 2] = 'x'
        self.assertEqual(str(val1), str(canvas))

    @mock.patch('domain.main.operations')
    def test_3(self, mocked):
        print('test 3')
        val1 = create_rectangle(np.array([[' ' for x in range(int(4))] for y in range(int(20))]), 0, 0, 2, 2)
        canvas = np.array([[' ' for x in range(int(4))] for y in range(int(20))])
        canvas[0, 0] = 'x'
        canvas[0, 1] = 'x'
        canvas[0, 2] = 'x'
        canvas[1, 0] = 'x'
        canvas[1, 2] = 'x'
        canvas[2, 0] = 'x'
        canvas[2, 1] = 'x'
        canvas[2, 2] = 'x'
        self.assertEqual(str(val1), str(canvas))

    @mock.patch('domain.main.operations')
    def test_4(self, mocked):
        print('test 4')
        val1 = fill_area(np.array([[' ' for x in range(int(4))] for y in range(int(20))]), 0, 0, 'c')
        canvas = np.array([['c' for x in range(int(4))] for y in range(int(20))])
        self.assertEqual(str(val1), str(canvas))

