def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[i].append(value)

    return matrix
rezul1 = print(get_matrix(2, 2, 10))
rezul2 = print(get_matrix(3, 5, 42))
rezul3 = print(get_matrix(4, 2, 13))
