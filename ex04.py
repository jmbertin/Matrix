from classes.Vector import Vector

def main():
    """
    Main function for testing norm_1, norm and norm_inf.
    """
    u = Vector([0., 0., 0.])
    print("u = ", u)
    print("u.norm_1(), u.norm(), u.norm_inf()")
    print("Function output:",u.norm_1(), u.norm(), u.norm_inf())
    print("Expected output: 0.0 0 0.0")
    print("-"*40)

    u = Vector([1., 2., 3.])
    print("u = ", u)
    print("u.norm_1(), u.norm(), u.norm_inf()")
    print("Function output:",u.norm_1(), u.norm(), u.norm_inf())
    print("Expected output: 6.0 3.74165738 3.0")
    print("-"*40)

    u = Vector([-1., -2.])
    print("u = ", u)
    print("u.norm_1(), u.norm(), u.norm_inf()")
    print("Function output:",u.norm_1(), u.norm(), u.norm_inf())
    print("Expected output: 3.0 2.236067977 2.0")

if __name__ == "__main__":
    main()
