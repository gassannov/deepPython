def mul_matrix(matrix1, matrix2):
    out_matrix = [[0] * len(matrix1)] * len(matrix2[0])
    if len(matrix1[0]) != len(matrix2):
        return None

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            out_matrix[i][j] = sum
    return out_matrix
