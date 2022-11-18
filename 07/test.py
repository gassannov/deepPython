import unittest
import matrix_c
import matrix_p
import cutils

MATRICES_A = [
    [[1, 2], [1, 2]],
    [[3, 3], [3, 3]],
    [[1, 1, 1], [1, 1, 1]]
]

MATRICES_B = [
    [[3, 2], [3, 2]],
    [[2, 2], [2, 2]],
    [[1, 1], [1, 1], [1, 1]],
    [[1, 1]]
]

MATRICES_RESULT = [
    [[9, 6], [9, 6]],
    [[12, 12], [12, 12]],
    [[3, 3], [3, 3]],
    [[1, 1], [1, 2]],
    None
]


class TestMatrix(unittest.TestCase):
    def test_main(self):
        for matrix_a, matrix_b, matrix_result in zip(MATRICES_A, MATRICES_B, MATRICES_RESULT):
            self.assertListEqual(matrix_p.mul_matrix(matrix_a, matrix_b), matrix_result)
            self.assertListEqual(matrix_c.mul_matrix(matrix_a, matrix_b), matrix_result)
            self.assertListEqual(cutils.matmul(matrix_a, matrix_b), matrix_result)
