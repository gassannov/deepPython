import os

import cffi
import random


def mul_matrix(matrix1, matrix2):
    ffi = cffi.FFI()
    lib = ffi.dlopen(f'{os.getcwd()}/libmatrix/libmatrix.so')
    ffi.cdef('''
    typedef struct Matrix{
        int** matrix;
        int row_num;
        int column_num;
    } Matrix;

    Matrix* create_matrix(int row_num, int column_num);
    Matrix* mul_matrix(Matrix* matrix1, Matrix* matrix2);
    Matrix* create_matrix_(int** m, int row_num, int column_num);
    ''')
    arrs1 = [ffi.new('int[]', item) for item in matrix1]
    arrs2 = [ffi.new('int[]', item) for item in matrix2]
    ar1 = ffi.new('int*[]', arrs1)
    ar2 = ffi.new('int*[]', arrs2)
    matrix1_c = lib.create_matrix_(ar1, len(matrix1), len(matrix1[0]))
    matrix2_c = lib.create_matrix_(ar2, len(matrix2), len(matrix2[0]))
    matrix3_c = lib.mul_matrix(matrix1_c, matrix2_c)
    return [[matrix3_c.matrix[i][j] for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
