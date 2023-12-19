from classes.Matrix import Matrix

def main():
    """
    Main function for testing matrix determinant.
    """
    matrix = Matrix([[1, -1], [-1, 1]])
    print("matrix = ", matrix)
    print("matrix.determinant()")
    print("Function output:",matrix.determinant())
    print("Expected output: 0.0")

    print("-"*40)

    matrix = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    print("matrix = ", matrix)
    print("matrix.determinant()")
    print("Function output:",matrix.determinant())
    print("Expected output: 8.0")

    print("-"*40)

    matrix = Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
    print("matrix = ", matrix)
    print("matrix.determinant()")
    print("Function output:",matrix.determinant())
    print("Expected output: -174.0")

    print("-"*40)

    matrix = Matrix([[8., 5., -2., 4.], [4., 2.5, 20., 4.], [8., 5., 1., 4.], [28., -4., 17., 1.]])
    print("matrix = ", matrix)
    print("matrix.determinant()")
    print("Function output:",matrix.determinant())
    print("Expected output: 1032.0")

    print("-"*40)

    try:
        matrix = Matrix([[1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.], [11., 12., 13., 14., 15.], [16., 17., 18., 19., 20.], [21., 22., 23., 24., 25.]])
        print("matrix = ", matrix)
        print("matrix.determinant()")
        print("Function output:",matrix.determinant())
        print("Expected output: 0.0")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
