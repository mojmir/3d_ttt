from interface.point import Point


class Field(object):
    """
    Represents playing field.

    Attributes:
        matrix: 3D list of points representing stones
        full: boolean, is matrix full filled
        solved: there is already winner

    Methods:
        add_stone: add point of selected value if possible in matrix
        create matrix: return 3D list filled with zero value points, plain field
        guess_point:
        check_winner:
        display:
    """

    def __init__(self, dimension_x, dimension_y, dimension_z):
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.dimension_z = dimension_z
        self.matrix = self.create_matrix(dimension_x, dimension_y, dimension_z)

    def create_matrix(self, width, length, height):
        """
        Return 3D list filled with zero value points, plain field
        """
        matrix = []
        for i in range(width):
            plain = []
            for j in range(length):
                line = []
                for k in range(height):
                    line.append(Point())
                plain.append(line)
            matrix.append(plain)
        return matrix

    def add_stone(self, i, j, k, new_value):
        """
        Add point of selected value if possible in matrix
        """
        if i in range(self.dimension_x) and j in range(self.dimension_y) and k in range(self.dimension_z):
            selected_point = self.matrix[i][j][k]
            if selected_point.value == 0:
                selected_point.value = new_value
            else:
                raise ValueError("Filling already taken point")
        else:
            raise ValueError("Adding point outside of field boundaries")

    def __str__(self):
        """
        Create simple display text
        """
        text = ""
        for k in range(self.dimension_x):
            text += str(k) + '\n'
            for j in range(self.dimension_y):
                text += str(self.matrix[k][j]) + '\n'
        return text

