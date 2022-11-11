import random
import matrix_c
import matrix_p
import time
import cutils


def print_matrix(matrix):
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=' ')
        print()


def make_random_matrix(num_rows, num_columns):
    matrix = [[0] * num_columns] * num_rows
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = random.randint(random_low, random_high)
    return matrix


if __name__ == '__main__':
    num_rows, num_columns = 3, 3
    random_low, random_high = 1, 4
    matrix_number = 1000

    matrices = [make_random_matrix(num_rows, num_columns) for i in range(matrix_number)]
    matrix_out = matrices[0]
    start_time = time.time()
    for i in range(1, matrix_number):
        matrix_out = matrix_p.mul_matrix(matrix_out, matrices[i])
    end_time = time.time()
    print(f'in python time = {end_time - start_time}')

    matrix_out = matrices[0]
    start_time = time.time()
    for i in range(1, matrix_number):
        matrix_out = matrix_c.mul_matrix(matrix_out, matrices[i])
    end_time = time.time()
    print(f'in cffi time = {end_time - start_time}')

    matrix_out = matrices[0]
    start_time = time.time()
    for i in range(1, matrix_number):
        matrix_out = cutils.matmul(matrix_out, matrices[i])
    end_time = time.time()
    print(f'in capi time = {end_time - start_time}')


