#! /usr/bin/env python
import cutils


def matmul(matrix1, matrix2):
    res = cutils.matmul(matrix1, matrix2)
    return res


if __name__ == "__main__":
    print(matmul([[1, 2], [1, 2]], [[1, 2], [1, 2]]))
