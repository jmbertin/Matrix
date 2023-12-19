from classes.Matrix import Matrix
from classes.Vector import Vector

def main():
    """
    Main function for testing matrix operations.
    """
    u = Matrix([[1., 0.], [0., 1.]])
    v = Vector([4., 2.])
    print("u = ", u)
    print("v = ", v)
    print("u.mul_vec(v)")
    print("Function output:", u.mul_vec(v))
    print("Expected output: [[4., 2.]]")

    print("-"*40)

    u = Matrix([[2., 0.], [0., 2.]])
    v = Vector([4., 2.])
    print("u = ", u)
    print("v = ", v)
    print("u.mul_vec(v)")
    print("Function output:", u.mul_vec(v))
    print("Expected output: [8., 4.]")

    print("-"*40)

    u = Matrix([[2., -2.], [-2., 2.]])
    v = Vector([4., 2.])
    print("u = ", u)
    print("v = ", v)
    print("u.mul_vec(v)")
    print("Function output:", u.mul_vec(v))
    print("Expected output: [4., -4.]")

    print("-"*40)

    u = Matrix([[1., 0.], [0., 1.]])
    v = Matrix([[1., 0.], [0., 1.]])
    print("u = ", u)
    print("v = ", v)
    print("u.mul_mat(v)")
    print("Function output:", u.mul_mat(v))
    print("Expected output: [[1., 0.], [0., 1.]]")

    print("-"*40)

    u = Matrix([[1., 0.], [0., 1.]])
    v = Matrix([[2., 1.], [4., 2.]])
    print("u = ", u)
    print("v = ", v)
    print("u.mul_mat(v)")
    print("Function output:", u.mul_mat(v))
    print("Expected output: [[2., 1.], [4., 2.]]")

    print("-"*40)

    u = Matrix([[3., -5.], [6., 8.]])
    v = Matrix([[2., 1.], [4., 2.]])
    print("u = ", u)
    print("v = ", v)
    print("u.mul_mat(v)")
    print("Function output:", u.mul_mat(v))
    print("Expected output: [[-14., -7.], [44., 22.]]")


if __name__ == "__main__":
    main()
