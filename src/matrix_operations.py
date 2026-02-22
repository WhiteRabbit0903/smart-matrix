def multiply_matrix(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum_value = 0
            for k in range(len(b)):
                sum_value += a[i][k] * b[k][j]
            row.append(sum_value)
        result.append(row)
    return result


if __name__ == "__main__":
    A = [[1, 2],
         [3, 4]]

    B = [[2, 0],
         [1, 2]]

    print("Matrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nResult A x B:")
    print(multiply_matrix(A, B))
