from .Vector import Vector
from .tools import custom_sum, custom_round

class Matrix:
    def __init__(self, rows):
        """
        Initialize a Matrix instance.
        Parameters: rows (list of lists): A list of lists, where each sublist represents a row of the matrix.
        """
        self.rows = [Vector(row) for row in rows]

    # Exercice 00
    def add(self, other):
        """
        Add another matrix to this matrix.
        Parameters: other (Matrix): Another matrix to add to this one.
        Raises:     ValueError: If the matrices are not of the same size.
        """
        if len(self.rows) != len(other.rows):
            raise ValueError("Matrices must be of the same size")
        for self_row, other_row in zip(self.rows, other.rows):
            self_row.add(other_row)

    # Exercice 00
    def sub(self, other):
        """
        Subtract another matrix from this matrix.
        Parameters: other (Matrix): Another matrix to subtract from this one.
        Raises:     ValueError: If the matrices are not of the same size.
        """
        if len(self.rows) != len(other.rows):
            raise ValueError("Matrices must be of the same size")
        for self_row, other_row in zip(self.rows, other.rows):
            self_row.sub(other_row)

    # Exercice 00
    def scl(self, scalar):
        """
        Scale the matrix by a scalar.
        Parameters: scalar (numeric): The scalar value to multiply the matrix elements.
        """
        for row in self.rows:
            row.scl(scalar)

    # Exercice 02
    @staticmethod
    def lerp_matrix(u, v, t):
        """
        Linear interpolation between two matrices.
        Parameters: u (Matrix): The starting matrix.
                    v (Matrix): The ending matrix.
                    t (float): The interpolation factor between 0 and 1.
        Returns:    Matrix: The interpolated matrix.
        """
        if len(u.rows) != len(v.rows):
            raise ValueError("Matrices must have the same number of rows")

        interpolated_rows = [Vector.lerp_vector(u_row, v_row, t) for u_row, v_row in zip(u.rows, v.rows)]
        return Matrix([row.elements for row in interpolated_rows])

    # Exercice 07
    def mul_vec(self, vec):
        """
        Multiply this matrix by a vector.
        Parameters: vec (Vector): The vector to multiply by.
        Returns:    Vector: The result of the matrix-vector multiplication.
        Raises:     ValueError: If the dimensions of the matrix and vector do not align.
        """
        if len(self.rows[0].elements) != len(vec.elements):
            raise ValueError("Mismatched dimensions for matrix-vector multiplication")

        result = []
        for row in self.rows:
            row_dot_vec = custom_sum(row_elem * vec_elem for row_elem, vec_elem in zip(row.elements, vec.elements))
            result.append(row_dot_vec)

        return Vector(result)

    # Exercice 07
    def mul_mat(self, mat):
        """
        Multiply this matrix by another matrix.
        Parameters: mat (Matrix): The matrix to multiply by.
        Returns:    Matrix: The result of the matrix-matrix multiplication.
        Raises:     ValueError: If the dimensions of the matrices do not align.
        """
        if len(self.rows[0].elements) != len(mat.rows):
            raise ValueError("Mismatched dimensions for matrix-matrix multiplication")

        num_cols_self = len(self.rows[0].elements)
        mat_transposed = [[mat.rows[j].elements[i] for j in range(len(mat.rows))] for i in range(len(mat.rows[0].elements))]
        result = []
        for row in self.rows:
            new_row = []
            for col in mat_transposed:
                new_row.append(custom_sum(row.elements[i] * col[i] for i in range(num_cols_self)))
            result.append(new_row)

        return Matrix(result)

    # Exercice 08
    def trace(self):
        """
        Compute the trace of the matrix.
        Returns: The trace of the matrix.
        Raises:  ValueError: If the matrix is not square.
        """
        if len(self.rows) != len(self.rows[0].elements):
            raise ValueError("Matrix must be square to compute the trace")

        return custom_sum(self.rows[i].elements[i] for i in range(len(self.rows)))

    # Exercice 09
    def transpose(self):
        """
        Compute the transpose of the matrix.
        Returns: Matrix: The transpose of the matrix.
        """
        transposed_rows = []
        for j in range(len(self.rows[0].elements)):
            new_row = [self.rows[i].elements[j] for i in range(len(self.rows))]
            transposed_rows.append(new_row)

        return Matrix(transposed_rows)

    # Exercice 10
    def row_echelon(self):
        """
        Compute the row-echelon form of the matrix.
        Returns: Matrix: The row-echelon form of the matrix.
        """
        A = [row.elements[:] for row in self.rows]
        num_rows, num_cols = len(A), len(A[0])

        for i in range(num_rows):
            pivot_index = next((index for index, value in enumerate(A[i]) if value != 0), None)
            if pivot_index is not None:
                pivot = A[i][pivot_index]
                A[i] = [el / pivot for el in A[i]]

                for j in range(i + 1, num_rows):
                    ratio = A[j][pivot_index]
                    A[j] = [A[j][k] - ratio * A[i][k] for k in range(num_cols)]

        for i in range(num_rows - 1, -1, -1):
            pivot_index = next((idx for idx, val in enumerate(A[i]) if val != 0), None)
            if pivot_index is not None:

                for j in range(i - 1, -1, -1):
                    ratio = A[j][pivot_index]
                    A[j] = [A[j][k] - ratio * A[i][k] for k in range(num_cols)]

        return Matrix([Vector([custom_round(el, 7) for el in row]) for row in A])

    # Exercice 11
    def determinant(self):
        """
        Compute the determinant of the matrix.
        Returns: float: The determinant of the matrix.
        Raises:  ValueError: If the matrix is not square.
        """
        if len(self.rows) != len(self.rows[0].elements):
            raise ValueError("Matrix must be square")

        if len(self.rows) == 1:
            return self.rows[0].elements[0]
        if len(self.rows) == 2:
            return (self.rows[0].elements[0] * self.rows[1].elements[1]
                    - self.rows[0].elements[1] * self.rows[1].elements[0])
        if len(self.rows) == 3:
            return (self.rows[0].elements[0] * self.rows[1].elements[1] * self.rows[2].elements[2]
                    + self.rows[0].elements[1] * self.rows[1].elements[2] * self.rows[2].elements[0]
                    + self.rows[0].elements[2] * self.rows[1].elements[0] * self.rows[2].elements[1]
                    - self.rows[0].elements[2] * self.rows[1].elements[1] * self.rows[2].elements[0]
                    - self.rows[0].elements[0] * self.rows[1].elements[2] * self.rows[2].elements[1]
                    - self.rows[0].elements[1] * self.rows[1].elements[0] * self.rows[2].elements[2])

        if len(self.rows) == 4:
            det = 0
            for i in range(4):
                sub_matrix = [row.elements[:i] + row.elements[i+1:] for row in self.rows[1:]]
                sub_det = Matrix(sub_matrix).determinant()
                det += self.rows[0].elements[i] * sub_det * (-1) ** i
            return det

        else:
            raise ValueError("Error: Matrix must be 1x1, 2x2, 3x3 or 4x4")

    # Exercice 12
    def inverse(self):
        """
        Compute the inverse of the matrix.
        Returns: Matrix: The inverse of the matrix.
        Raises:  ValueError: If the matrix is not square or not invertible.
        """
        if len(self.rows) != len(self.rows[0].elements):
            raise ValueError("Matrix must be square to find its inverse")

        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is not invertible")

        if len(self.rows) == 2:
            return Matrix([[custom_round(self.rows[1].elements[1]/det, 9), custom_round(-self.rows[0].elements[1]/det, 9)],
                        [custom_round(-self.rows[1].elements[0]/det, 9), custom_round(self.rows[0].elements[0]/det, 9)]])

        identity = [[1 if i == j else 0 for j in range(len(self.rows))] for i in range(len(self.rows))]
        A = [row.elements[:] for row in self.rows]

        for i in range(len(self.rows)):
            pivot = A[i][i]
            for j in range(len(self.rows)):
                A[i][j] /= pivot
                identity[i][j] /= pivot

            for k in range(len(self.rows)):
                if k != i:
                    factor = A[k][i]
                    for j in range(len(self.rows)):
                        A[k][j] -= factor * A[i][j]
                        identity[k][j] -= factor * identity[i][j]

        rounded_identity = [[custom_round(el, 9) for el in row] for row in identity]

        return Matrix(rounded_identity)

    # Exercice 13
    def rank(self):
        """
        Compute the rank of the matrix.
        Returns: int: The rank of the matrix.
        """
        echelon_form = self.row_echelon()
        rank = 0
        for row in echelon_form.rows:
            if any(custom_round(value, 9) != 0 for value in row.elements):
                rank += 1
        return rank

    def matrix_3d(self, matrix):
        """
        Return a string representation of the matrix in a format similar to:
        [[0, 1],
        [2, 3]]
        """
        matrix_str = '[' + ',\n'.join(['[' + ', '.join(map(str, row.elements)) + ']' for row in matrix.rows]) + ']'
        return matrix_str

    def __repr__(self):
        """
        Return a string representation of the matrix.
        Returns: str: A string representation of the matrix.
        """
        return f"{[row.elements for row in self.rows]}"
