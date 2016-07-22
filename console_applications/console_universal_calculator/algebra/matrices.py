import numpy as np
import math
"""
Matrix 2x2
| a b |
| c d |


Matrix 3x3
| a b c |
| d e f |
| g h i |
"""


class Matrix():
    def __init__(self, rows, columns, ident):

        self.rows = rows
        self.columns = columns
        self.ident = ident

        #Matrix Storage
        self.matrix = np.array([])

    def set_id(self, value):
        self.ident = value

    def fill_matrix(self):
        columns = self.columns
        rows = self.rows

        int_mat = np.array([[0 for c in range(0, columns)] for r in range(0, rows)])

        #Convert to float numpy array]
        float_mat = int_mat.astype(float)
        self.matrix = float_mat

        for row in range(0, rows):
            for element in range(0, columns):
                self.matrix[row][element] = float(eval(input("Enter element " + str(element + 1) + " of row " + str(row + 1) + " of Matrix " + self.ident + ": ")))

    def add(self, mat_b):
        return self.matrix + mat_b.matrix

    def multiply_scalar(self, scalar):
        return self.matrix * scalar

    def multiply(self, mat_b):
        return np.dot(self.matrix, mat_b.matrix)

    def determinant(self):
        return np.linalg.det(self.matrix)

    def inverse(self):
        return np.linalg.inv(self.matrix)

    def transpose(self):
        return self.matrix.transpose()
