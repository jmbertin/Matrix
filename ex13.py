from classes.Matrix import Matrix

def main():
    """
    Main function to test the rank function
    """
    matrix = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
    print("matrix = ", matrix)
    print("matrix.rank()")
    print("Function output:",matrix.rank())
    print("Expected output: 3")

    print("-"*40)

    matrix = Matrix([[ 1., 2., 0., 0.],[ 2., 4., 0., 0.],[-1., 2., 1., 1.]])
    print("matrix = ", matrix)
    print("matrix.rank()")
    print("Function output:",matrix.rank())
    print("Expected output: 2")

    print("-"*40)

    matrix = Matrix([[ 8., 5., -2.],[ 4., 7., 20.],[ 7., 6., 1.],[21., 18., 7.]])
    print("matrix = ", matrix)
    print("matrix.rank()")
    print("Function output:",matrix.rank())
    print("Expected output: 3")

if __name__ == '__main__':
    main()
