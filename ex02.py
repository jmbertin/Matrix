from classes.Matrix import Matrix
from classes.Vector import Vector

def main():
    """
    Main function, to test the lerp functions.
    """
    a1 = Vector([0.])
    a2 = Vector([1.])
    print("a1:", a1)
    print("a2:", a2)
    print("lerp_vector(a1, a2, 0.0)")
    print("Function output:", Vector.lerp_vector(a1, a2, 0.0))
    print("Expected output: [0.0]")
    print("lerp_vector(a1, a2, 1.0)")
    print("Function output:", Vector.lerp_vector(a1, a2, 1.0))
    print("Expected output: [1.0]")
    print("lerp_vector(a1, a2, 0.5)")
    print("Function output:", Vector.lerp_vector(a1, a2, 0.5))
    print("Expected output: [0.5]")
    print("-" * 40)

    e1 = Vector([2., 1.])
    e2 = Vector([4., 2.])
    print("e1:", e1)
    print("e2:", e2)
    print("lerp_vector(e1, e2, 0.3)")
    print("Function output:", Vector.lerp_vector(e1, e2, 0.3))
    print("Expected output: [2.6, 1.3]")
    print("-" * 40)

    m1 = Matrix([[2., 1.], [3., 4.]])
    m2 = Matrix([[20., 10.], [30., 40.]])
    print("m1:", m1)
    print("m2:", m2)
    print("lerp_matrix(m1, m2, 0.5)")
    print("Function output:", Matrix.lerp_matrix(m1, m2, 0.5))
    print("Expected output: [[11.0, 5.5], [16.5, 22.0]]")

if __name__ == "__main__":
    main()
