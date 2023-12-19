from classes.Vector import Vector

def main():
    """
    Main function for testing dot product.
    """
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print("u:", u)
    print("v:", v)
    print("dot(u, v)")
    print("Function output:",u.dot(v))
    print("Expected output: 0.0")
    print("-" * 40)

    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print("u:", u)
    print("v:", v)
    print("dot(u, v)")
    print("Function output:",u.dot(v))
    print("Expected output: 2.0")
    print("-" * 40)

    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print("u:", u)
    print("v:", v)
    print("dot(u, v)")
    print("Function output:",u.dot(v))
    print("Expected output: 9.0")

if __name__ == "__main__":
    main()
