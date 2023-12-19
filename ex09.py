from classes.Matrix import Matrix

def main():
    """
    Main function to test the transpose function.
    """
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    print("Original matrix:")
    print(A.matrix_3d(A))
    print("A.transpose()")
    print("Function output:")
    print(A.matrix_3d(A.transpose()))
    print("Expected output: \n[[1, 4],\n[2, 5],\n[3, 6]]")

    print("----------------------------------------")

    A = Matrix([[7, 8], [9, 10], [11, 12]])
    print("Original matrix:")
    print(A.matrix_3d(A))
    print("A.transpose()")
    print("Function output:")
    print(A.matrix_3d(A.transpose()))
    print("Expected output: \n[[7, 9, 11],\n[8, 10, 12]]")

    print("----------------------------------------")

    A = Matrix([[1, 2], [3, 4]])
    print("Original matrix:")
    print(A.matrix_3d(A))
    print("A.transpose()")
    print("Function output:")
    print(A.matrix_3d(A.transpose()))
    print("Expected output: \n[[1, 3],\n[2, 4]]")

if __name__ == '__main__':
    main()
