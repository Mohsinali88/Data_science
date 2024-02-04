
def get_kth_column(matrix, k):
    return [row[k] for row in matrix]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

k = 1
kth_column = get_kth_column(matrix, k)

print(kth_column)