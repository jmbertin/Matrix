from classes.Vector import Vector

def main():
    """
    Main function, to test the linear_combination function.
    """
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    print("e1:", e1)
    print("e2:", e2)
    print("e3:", e3)
    print("linear_combination([e1, e2, e3], [10., -2., 0.5])")
    print("Function output:", Vector.linear_combination([e1, e2, e3], [10., -2., 0.5]))
    print("Expected output: [10.0, -2.0, 0.5]")
    print("-" * 40)
    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    print("v1:", v1)
    print("v2:", v2)
    print("linear_combination([v1, v2], [10., -2.])")
    print("Function output:", Vector.linear_combination([v1, v2], [10., -2.]))
    print("Expected output: [10.0, 0.0, 230.0]")

if __name__ == "__main__":
    main()
