import numpy as np


def matrix_info(A):
    print("Matrix:")
    print(A)

    print("\nShape:", A.shape)
    print("Determinant:", np.linalg.det(A))
    print("Rank:", np.linalg.matrix_rank(A))


def eigen_analysis(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors:")
    print(eigenvectors)


def main():
    A = np.array([[2, 1],
                  [1, 3]])

    matrix_info(A)
    eigen_analysis(A)


if __name__ == "__main__":
    main()
