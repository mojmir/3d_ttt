from interface.point import Point
import random


class Field(object):
    """
    Represents playing field.

    Attributes:
        matrix: 3D list of points representing stones
        full: boolean, is matrix full filled
        solved: there is already winner

    Methods:
        add_stone: add stone of selected value if possible in matrix
        create matrix: return 3D list filled with zero value points, plain field
        guess_point:
        check_winner: check if there is a winner after the last move
        display:
    """

    def __init__(self, dimension_x, dimension_y, dimension_z):
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.dimension_z = dimension_z
        self.matrix = self.create_matrix(dimension_x, dimension_y, dimension_z)
        self.last_move = None

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
        self.last_move = (i, j, k)

    def guess_stone(self, value):
        #TODO store list of empty points and pick random from them
        while True:
            x = random.randrange(0, self.dimension_x)
            y = random.randrange(0, self.dimension_y)
            z = random.randrange(0, self.dimension_z)
            empty = self.empty_position(x, y, z)
            if empty:
                self.add_stone(x, y, z, value)
                return True

    def valid_position(self, i, j, k):
        """
        Check if position is valid.

        Returns:
            bool: True if position is valid
        """
        if i < self.dimension_x and j < self.dimension_y and k < self.dimension_z:
            if i >= 0 and j >= 0 and k >= 0:
                return True
        else:
            return False

    def empty_position(self, i, j, k):
        """
        Check if position is valid and empty.

        Returns:
            bool: True if position is empty
        """
        if self.valid_position(i, j, k):
            empty = (self.matrix[i][j][k].value == 0)
            return empty
        else:
            raise ValueError("Point outside of field boundaries")

    def check_winner(self, n):
        """
        Check if there is a winner after the last move.

        Args:
           n (int): number of stones in line required to win

        Returns:
            int: value of winner stone, 0 if now winner was found
        """
        dimensions = (self.dimension_x, self.dimension_y, self.dimension_z)
        x, y, z = self.last_move
        memory = (self.matrix[x][y][z]).value  # Extra () brackets
        directions = ((1, 0, 0),    #Should be stored in settings or new object constants
                       (0, 1, 0),
                       (0, 0, 1),
                       (1, 1, 0),
                       (1, -1, 0),
                       (1, 0, 1),
                       (1, 0, -1),
                       (0, 1, 1),
                       (0, 1, -1),
                       (1, 1, 1),
                       (1, 1, -1),
                       (1, -1, 1),
                       (-1, 1, 1))
        for aDirection in directions:
            position = list(self.last_move)  # Self last position can be created as list
            count = 0
            value = memory
            while memory == value:
                position = [position[i] + aDirection[i] for i in range(3)]  # Klobuk dole toto je super
                count += 1
                if count == n:
                    return memory  # return the winner
                flag = False
                for i in range(3):
                    if (position[i] == dimensions[i]) or (position[i] == -1):
                        flag = True
                if flag:
                    break
                i, j, k = position
                value = (self.matrix[i][j][k]).value

            #Da sa to zosit dokopy pod jeden for cyklus
            position = list(self.last_move)
            value = memory
            count -= 1
            while memory == value:
                position = [position[i] - aDirection[i] for i in range(3)]
                count += 1
                if count == n:
                    return memory #return the winner
                flag = False
                for i in range(3):
                    if (position[i] == dimensions[i]) or (position[i] == -1):
                        flag = True
                if flag:
                    break
                i, j, k = position
                value = (self.matrix[i][j][k]).value

        return 0

    def __str__(self):
        """
        Create simple display text
        """
        text = ""
        for k in range(self.dimension_x):
            text += "X = " + str(k) + '\n'
            for j in range(self.dimension_y):
                text += str(self.matrix[k][j]) + '\n'
        return text

