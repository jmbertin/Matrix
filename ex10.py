from classes.Matrix import Matrix


def main():
    """
    Main function to test the row_echelon function.
    """
    A = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
    print("u = ", A)
    print("u.row_echelon()")
    print("Function output:",A.row_echelon())
    print("Expected output: [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]")
    print("----------------------------------------")
    A = Matrix([[1., 2.], [3., 4.]])
    print("u = ", A)
    print("u.row_echelon()")
    print("Function output:",A.row_echelon())
    print("Expected output: [[1.0, 0.0], [0.0, 1.0]]")
    print("----------------------------------------")
    A = Matrix([[1., 2.], [2., 4.]])
    print("u = ", A)
    print("u.row_echelon()")
    print("Function output:",A.row_echelon())
    print("Expected output: [[1.0, 2.0], [0.0, 0.0]]")
    print("----------------------------------------")
    A = Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])
    print("u = ", A)
    print("u.row_echelon()")
    print("Function output:",A.row_echelon())
    print("Expected output: [[1.0, 0.625, 0.0, 0.0, -12.1666667], [0.0, 0.0, 1.0, 0.0, -3.6666667], [0.0, 0.0, 0.0, 1.0, 29.5]]")

if __name__ == '__main__':
    main()
