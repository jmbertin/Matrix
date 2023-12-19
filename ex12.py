from classes.Matrix import Matrix

def main():
    """
    Main function to test reverse matrix
    """
    matrix = Matrix([[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]])
    print("matrix = ", matrix)
    print("matrix.inverse()")
    print("Function output:",matrix.inverse())
    print("Expected output: [[1., 0., 0.],[0., 1., 0.],[0., 0., 1.]]")

    print("-"*40)

    matrix = Matrix([[2., 0., 0.],[0., 2., 0.],[0., 0., 2.]])
    print("matrix = ", matrix)
    print("matrix.inverse()")
    print("Function output:",matrix.inverse())
    print("Expected output: [[0.5, 0.0, 0.0],[0.0, 0.5, 0.0],[0.0, 0.0, 0.5]]")

    print("-"*40)

    matrix = Matrix([[8., 5., -2.],[4., 7., 20.],[7., 6., 1.]])
    print("matrix = ", matrix)
    print("matrix.inverse()")
    print("Function output:",matrix.inverse())
    print("Expected output: [[0.649425287, 0.097701149, -0.655172414], [-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]]")

if __name__ == '__main__':
    main()
