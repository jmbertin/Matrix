from classes.Matrix import Matrix

def main():
    """
    Main function to test the trace function.
    """
    u = Matrix([[1., 0.], [0., 1.]])
    print("u = ", u)
    print("u.trace()")
    print("Function output:", u.trace())
    print("Expected output: 2.0")

    print("-"*40)

    u = Matrix([[2., -5., 0.], [4., 3., 7.], [-2., 3., 4.]])
    print("u = ", u)
    print("u.trace()")
    print("Function output:", u.trace())
    print("Expected output: 9.0")

    print("-"*40)

    u = Matrix([[-2., -8., 4.], [1., -23., 4.], [0., 6., 4.]])
    print("u = ", u)
    print("u.trace()")
    print("Function output:", u.trace())
    print("Expected output: -21.0")

if __name__ == '__main__':
    main()

