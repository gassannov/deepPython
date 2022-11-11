//
// Created by Марат Гасанов on 01.11.2022.
//

#include "stdio.h"
#include "stdlib.h"
#include "matrix.h"



Matrix* create_matrix(int row_num, int column_num){
    int ** m = (int**)malloc(sizeof(int*)*row_num);
    for (int i = 0; i < row_num; ++i) {
        m[i] = (int*) malloc(sizeof(int)*column_num);
    }
    Matrix* matrix = (Matrix*) malloc(sizeof(Matrix));
    if(!matrix)return NULL;
    matrix->matrix = m;
    matrix->row_num = row_num;
    matrix->column_num = column_num;
    return matrix;
}

Matrix* mul_matrix(Matrix* matrix1, Matrix* matrix2){
    if (matrix1->column_num != matrix2->row_num) return NULL;
    Matrix* out_matrix = create_matrix(matrix1->row_num, matrix2->column_num);
    for (int i = 0; i < matrix1->row_num; ++i) {
        for (int j = 0; j < matrix2->column_num; ++j) {
            int sum = 0;
            for (int k = 0; k < matrix2->row_num; ++k) {
                sum += matrix1->matrix[i][k] * matrix2->matrix[k][j];
            }
            out_matrix->matrix[i][j] = sum;
        }
    }
    return out_matrix;
}

Matrix* create_matrix_(int** m, int row_num, int column_num){
    Matrix* out_matrix = create_matrix(row_num, column_num);
    for(int i = 0; i < row_num; i++){
        for (int j = 0; j < column_num; ++j) {
            out_matrix->matrix[i][j] = m[i][j];
        }
    }
    return out_matrix;
}
