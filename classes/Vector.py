from .tools import custom_sum, custom_abs, custom_sqrt, custom_round, custom_max

class Vector:
    def __init__(self, elements):
        """
        Initialize a Vector instance.
        Parameters: elements (list): A list of numerical elements of the vector.
        """
        self.elements = elements

    def __iter__(self):
        """
        Make the Vector class iterable over its elements.
        """
        return iter(self.elements)

    # Exercice 00
    def add(self, other):
        """
        Add another vector to this vector.
        Parameters: other (Vector): Another vector to add to this one.
        Raises:     ValueError: If the vectors are not of the same size.
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be of the same size")
        self.elements = [a + b for a, b in zip(self.elements, other.elements)]

    # Exercice 00
    def sub(self, other):
        """
        Subtract another vector from this vector.
        Parameters: other (Vector): Another vector to subtract from this one.
        Raises:     ValueError: If the vectors are not of the same size.
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be of the same size")
        self.elements = [a - b for a, b in zip(self.elements, other.elements)]

    # Exercice 01
    @staticmethod
    def linear_combination(vectors, coefficients):
        """
        Compute the linear combination of vectors scaled by their respective coefficients.
        Parameters: vectors (list of Vector): List of vectors to be combined.
                    coefficients (list of numeric): List of scalar coefficients for each vector.
        Returns:    Vector: The resulting vector from the linear combination.
        Raises:     ValueError: If the lists of vectors and coefficients are not of the same length.
        """
        if len(vectors) != len(coefficients):
            raise ValueError("Vectors and coefficients must be of the same length")

        combined_vector = Vector([0] * len(vectors[0].elements))
        for vector, coefficient in zip(vectors, coefficients):
            scaled_vector = Vector([x * coefficient for x in vector.elements])
            combined_vector.add(scaled_vector)

        return combined_vector

    # Exercice 02
    @staticmethod
    def lerp_vector(u, v, t):
        """
        Linear interpolation between two vectors.
        Parameters: u (Vector): The starting vector.
                    v (Vector): The ending vector.
                    t (float): The interpolation factor between 0 and 1.
        Returns:    Vector: The interpolated vector.
        """
        if len(u.elements) != len(v.elements):
            raise ValueError("Vectors must be of the same size")

        interpolated_elements = [(1 - t) * u_elem + t * v_elem for u_elem, v_elem in zip(u.elements, v.elements)]
        interpolated_elements = [custom_round(element, 9) for element in interpolated_elements]
        return Vector(interpolated_elements)

    # Exercice 00
    def scl(self, scalar):
        """
        Scale the vector by a scalar.
        Parameters: scalar (numeric): The scalar value to multiply the vector elements.
        """
        self.elements = [a * scalar for a in self.elements]

    # Exercice 03
    def dot(self, other):
        """
        Compute the dot product of this vector with another vector.
        Parameters: other (Vector): Another vector to calculate the dot product with.
        Returns:    float: The dot product of the two vectors.
        Raises:     ValueError: If the vectors have different dimensions.
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be of the same size")

        return custom_sum(a * b for a, b in zip(self.elements, other.elements))

    # Exercice 04
    def norm_1(self):
        """
        Calculate the 1-norm (Manhattan norm) of the vector using precise summation.
        The 1-norm is defined as the sum of the absolute values of the vector elements.
        Returns: float: The 1-norm of the vector.
        """
        return custom_sum(custom_abs(x) for x in self.elements)

    # Exercice 04
    def norm(self):
        """
        Calculate the 2-norm (Euclidean norm) of the vector using custom power function.
        The 2-norm is defined as the square root of the sum of the squares of the vector elements.
        Returns: float: The 2-norm of the vector.
        """
        norm = custom_sqrt(custom_sum(pow(x, 2) for x in self.elements))
        return custom_round(norm, 9)

    # Exercice 04
    def norm_inf(self):
        """
        Calculate the infinity norm (supremum norm) of the vector using max.
        The infinity norm is defined as the maximum absolute value of the vector elements.
        Returns: float: The infinity norm of the vector.
        """
        norm = custom_max(custom_abs(x) for x in self.elements)
        return custom_round(norm, 9)

    # Exercice 05
    def angle_cos(self, v):
        """
        Calculate the cosine of the angle between two vectors.
        Parameters: v (Vector): The second vector.
        Returns:    float: The cosine of the angle between the vectors.
        Raises:     ValueError: If the vectors are of different sizes or one/both are zero vectors.
        """
        if len(self.elements) != len(v.elements):
            raise ValueError("Vectors must be of the same size")

        dot_product = self.dot(v)
        norm_self = self.norm()
        norm_v = v.norm()

        if norm_self == 0 or norm_v == 0:
            raise ValueError("One or both vectors are zero vectors")

        cosine = dot_product / (norm_self * norm_v)
        return custom_round(cosine, 9)

    # Exercice 06
    def cross_product(self, other):
        """
        Compute the cross product of this vector with another vector.
        Parameters: other (Vector): Another vector to calculate the cross product with.
        Returns:    Vector: The cross product of the two vectors.
        Raises:     ValueError: If either of the vectors is not 3-dimensional.
        """
        if len(self.elements) != 3 or len(other.elements) != 3:
            raise ValueError("Both vectors must be 3-dimensional")

        u1, u2, u3 = self.elements
        v1, v2, v3 = other.elements
        return Vector([u2 * v3 - u3 * v2, u3 * v1 - u1 * v3, u1 * v2 - u2 * v1])

    def __repr__(self):
        """
        Return a string representation of the vector.
        Returns: str: A string representation of the vector.
        """
        return f"{self.elements}"
