
def vertical_concatenate(matrix1, matrix2):
    result_matrix = []

    for row in matrix1:
        result_matrix.append(row)

    for row in matrix2:
        result_matrix.append(row)
    return result_matrix

matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8, 9],
           [10, 11, 12]]

concatenated_matrix = vertical_concatenate(matrix1, matrix2)

for row in concatenated_matrix:
    print(row)