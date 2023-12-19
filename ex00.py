from classes.Matrix import Matrix
from classes.Vector import Vector

def main():
    """
    Main function for testing matrix operations.
    """
    u = Vector([2, 3])
    v = Vector([5, 7])
    print("Input u:", u)
    print("Input v:", v)
    u.add(v)
    print("Operation: u.add(v)")
    print("Function output:", u)
    print("Expected output: [7, 10]")
    print("-" * 40)

    u = Vector([2, 3])
    v = Vector([5, 7])
    print("Input u:", u)
    print("Input v:", v)
    u.sub(v)
    print("Operation: u.sub(v)")
    print("Function output:", u)
    print("Expected output: [-3, -4]")
    print("-" * 40)

    u = Vector([2, 3])
    print("Input u:", u)
    u.scl(2)
    print("Operation: u.scl(2)")
    print("Function output:", u)
    print("Expected output: [4, 6]")
    print("-" * 40)

    u = Matrix([[1, 2], [3, 4]])
    v = Matrix([[7, 4], [-2, 2]])
    print("Input u:", u)
    print("Input v:", v)
    u.add(v)
    print("Operation: u.add(v)")
    print("Function output:", u)
    print("Expected output: [[8, 6], [1, 6]]")
    print("-" * 40)

    u = Matrix([[1, 2], [3, 4]])
    v = Matrix([[7, 4], [-2, 2]])
    print("Input u:", u)
    print("Input v:", v)
    u.sub(v)
    print("Operation: u.sub(v)")
    print("Function output:", u)
    print("Expected output: [[-6, -2], [5, 2]]")
    print("-" * 40)

    u = Matrix([[1, 2], [3, 4]])
    print("Input u:", u)
    u.scl(2)
    print("Operation: u.scl(2)")
    print("Function output:", u)
    print("Expected output: [[2, 4], [6, 8]]")

if __name__ == "__main__":
    main()
