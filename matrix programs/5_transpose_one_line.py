
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

for row in transpose_matrix:
    print(row)