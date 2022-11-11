//
// Created by Марат Гасанов on 01.11.2022.
//

#ifndef LIBC_MATRIX_H
#define LIBC_MATRIX_H

typedef struct Matrix{
    int** matrix;
    int row_num;
    int column_num;
} Matrix;

Matrix* create_matrix(int row_num, int column_num);
Matrix* mul_matrix(Matrix* matrix1, Matrix* matrix2);
Matrix* create_matrix_(int** m, int row_num, int column_num);


#endif //LIBC_MATRIX_H
