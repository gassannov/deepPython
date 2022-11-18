#include <stdlib.h>
#include <stdio.h>

#include <Python.h>

double get_matrix_item(PyObject* matrix, int index1, int index2){
    PyObject *row = PyList_GetItem(matrix, index1);
    PyObject *column = PyList_GetItem(row, index2);
    return PyFloat_AsDouble(column);
}

PyObject* matmul(PyObject* matrix1, PyObject* matrix2){
    long row_num1 = PyList_Size(matrix1);
    long row_num2 = PyList_Size(matrix2);
    long column_num1 = PyList_Size(PyList_GetItem(matrix1, 0));
    long column_num2 = PyList_Size(PyList_GetItem(matrix2, 0));
    if (column_num1 != row_num2) return NULL;

    PyObject* result_matrix = PyList_New(row_num1);
    for (int i = 0; i < row_num1; ++i) {
        PyObject* row = PyList_New(column_num2);
        for (int j = 0; j < column_num2; ++j) {
            int sum = 0;
            for (int k = 0; k < row_num2; ++k) {
                sum += get_matrix_item(matrix1, i, k) * get_matrix_item(matrix2, k, j);
            }
            PyList_SetItem(row, j, PyFloat_FromDouble(sum));
        }
        PyList_SetItem(result_matrix, i, row);
    }
    return result_matrix;
}

PyObject* cutils_matmul(PyObject* self, PyObject* args)
{
    PyObject* matrix1 = NULL;
    PyObject* matrix2 = NULL;
    if (!PyArg_ParseTuple(args, "OO", &matrix1, &matrix2))
    {
        printf("ERROR: Failed to parse argument");
        return NULL;
    }

    PyObject* result_matrix = matmul(matrix1, matrix2);
    return result_matrix;
}

static PyMethodDef methods[] = {
    { "matmul", cutils_matmul, METH_VARARGS, "matmul of matrix"},
    { NULL, NULL, 0, NULL}
};

static struct PyModuleDef cutils_module = {
    PyModuleDef_HEAD_INIT, "cutils",
    NULL, -1, methods
};

PyMODINIT_FUNC PyInit_cutils(void) {
    return PyModule_Create( &cutils_module );
}