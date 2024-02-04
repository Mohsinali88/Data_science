
def create_matrix(n):
    return [[0] * n for _ in range(n)]

n = 3
matrix = create_matrix(n)

for row in matrix:
    print(row)