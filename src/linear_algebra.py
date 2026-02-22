import numpy as np


def matrix_multiplication(A, B):
    return np.dot(A, B)


def main():
    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[2, 0],
                  [1, 2]])

    result = matrix_multiplication(A, B)

    print("Matrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nResult A x B:")
    print(result)


if __name__ == "__main__":
    main()
