import random
import time
import cutils
import matrix_c
import matrix_p


def print_matrix(matrix):
    for row in range(3):
        for column in range(3):
            print(matrix[row][column], end=' ')
        print()


def make_random_matrix(num_rows, num_columns):
    matrix = [[0] * num_columns] * num_rows
    for row in range(num_rows):
        for column in range(num_columns):
            matrix[row][column] = random.randint(RANDOM_LOW, RANDOM_HIGH)
    return matrix


if __name__ == '__main__':
    NUM_ROWS, NUM_COLUMNS = 3, 3
    RANDOM_LOW, RANDOM_HIGH = 1, 4
    MATRIX_NUMBER = 1000

    matrices = [make_random_matrix(NUM_ROWS, NUM_COLUMNS)
                for i in range(MATRIX_NUMBER)]
    matrix_out = matrices[0]
    start_time = time.time()
    for i in range(1, MATRIX_NUMBER):
        matrix_out = matrix_p.mul_matrix(matrix_out, matrices[i])
    end_time = time.time()
    print(f'in python time = {end_time - start_time}')

    matrix_out = matrices[0]
    start_time = time.time()
    for i in range(1, MATRIX_NUMBER):
        matrix_out = matrix_c.mul_matrix(matrix_out, matrices[i])
    end_time = time.time()
    print(f'in cffi time = {end_time - start_time}')

    matrix_out = matrices[0]
    start_time = time.time()
    for i in range(1, MATRIX_NUMBER):
        matrix_out = cutils.matmul(matrix_out, matrices[i])
    end_time = time.time()
    print(f'in capi time = {end_time - start_time}')
