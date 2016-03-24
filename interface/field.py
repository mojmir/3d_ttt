from interface.point import Point


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

    def check_winner(self, n): #n is the number of stones in line required to win
        """
        Check if there is a winner after the last move
        """
        dimensions = (self.dimension_x, self.dimension_y, self.dimension_z)
        x, y, z = self.last_move
        memory = (self.matrix[x][y][z]).value
        directions = ( (1,0,0),
                       (0,1,0),
                       (0,0,1),
                       (1,1,0),
                       (1,-1,0),
                       (1,0,1),
                       (1,0,-1),
                       (0,1,1),
                       (0,1,-1),
                       (1,1,1),
                       (1,1,-1),
                       (1,-1,1),
                       (-1,1,1) )
        for aDirection in directions:
            position = list(self.last_move)
            count = 0
            value = memory
            while ( memory == value ):
                position = [position[i] + aDirection[i] for i in range(3)]
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
            position = list(self.last_move)
            value = memory
            count -= 1
            while ( memory == value ):
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
        return 0 #if no winner was found

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

