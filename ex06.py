from classes.Vector import Vector

def main():
    """
    Main function for testing cross product.
    """
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print("u = ", u)
    print("v = ", v)
    print("cross_product(u, v)")
    print("Function output:", u.cross_product(v))
    print("Expected output: [0., 1., 0.]")
    print("-"*40)

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print("u = ", u)
    print("v = ", v)
    print("cross_product(u, v)")
    print("Function output:", u.cross_product(v))
    print("Expected output: [-3., 6., -3.]")
    print("-"*40)

    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print("u = ", u)
    print("v = ", v)
    print("cross_product(u, v)")
    print("Function output:", u.cross_product(v))
    print("Expected output: [17., -58., -16.]")
    print("-"*40)

if __name__ == '__main__':
    main()
