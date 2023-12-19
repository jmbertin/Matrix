from classes.Vector import Vector
from classes.tools import custom_round

def main():
    """
    Main function for testing angle_cos.
    """
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print("u = ", u)
    print("v = ", v)
    print("u.angle_cos(v)")
    print("Function output:",u.angle_cos(v))
    print("Expected output: 1.0")
    print("-"*40)

    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print("u = ", u)
    print("v = ", v)
    print("u.angle_cos(v)")
    print("Function output:",u.angle_cos(v))
    print("Expected output: 0.0")
    print("-"*40)

    u = Vector([-1., 1.])
    v = Vector([1., -1.])
    print("u = ", u)
    print("v = ", v)
    print("u.angle_cos(v)")
    print("Function output:",u.angle_cos(v))
    print("Expected output: -1.0")
    print("-"*40)

    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print("u = ", u)
    print("v = ", v)
    print("u.angle_cos(v)")
    print("Function output:",u.angle_cos(v))
    print("Expected output: 1.0")
    print("-"*40)

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print("u = ", u)
    print("v = ", v)
    print("u.angle_cos(v)")
    print("Function output:",u.angle_cos(v))
    print("Expected output: 0.974631846")

if __name__ == "__main__":
    main()
