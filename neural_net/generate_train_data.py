from interface.field import Field
import copy
import random
import math
#import pdb

def generate_X_train_data(dim_x, dim_y, dim_z, m, win_row, random_state=None):
    """
    Inputs:

    dim_x, dim_y, dim_z: dimensions of the board
    m: number of training samples to be generated

    Outputs:

    Return a list of m fields.

    Narrative:

    Construct valid matrix configurations by playing random games.
    """

    if random_state: #this serves for replicability of results (for debugging)
        random.seed(random_state)

    dimensions = (dim_x, dim_y, dim_z)
    fieldsX = []

    for i in range(0,m):
        aField = Field(dimensions)
        max_turns = random.randint(1, dim_x*dim_y*dim_z)
        turn = 1
        winner = 0
        players = [1,-1]
        while (turn <= max_turns) and (winner == 0):
            player = players[turn % 2]
            aField.guess_stone(player)
            winner = aField.check_winner(win_row)
            turn += 1
        fieldsX.append(aField)

    return fieldsX

def evaluate_rnd(fieldsX, win_row, random_state=None):
    """
    Return a list y of evaluations of all fields in fieldsX.

    Narrative:

    All fields have to be checked if the last move was made by
    the player labeled as +1. If this is not the case, the board is flipped.
    The evaluation is calculated by means of (random) games, according to the formula:

    eval = (won_count/num_games) * exp(-lost_count/sqrt(num_games))

    Note that we punish the loses by an exponential factor.
    This is just one of the ways how to evaluate the soundness of the configurations.
    Note that the evaluation is made from the point of view of the player who made
    the last move, i.e., player labeled as +1.

    """

    if random_state: #this serves for replicability of results (for debugging)
        random.seed(random_state)

    y = []

    for aField in fieldsX:

        # pdb.set_trace()

        """
        If the last move was made by player -1,
        then flip the board according to the table:

        winner  last_move  change
        +1      +1         -
        -1      -1         +1 <--> -1 (flip)
        0       -1         +1 <--> -1 (flip)
        0       +1         -
         """

        i, j, k = aField.last_move
        if aField.matrix[i][j][k].value == -1:
            flip(aField)

        winner = aField.check_winner(win_row)
        if winner == 1:
            eval = 1.0
            y.append(eval)
            continue

        won_count = 0
        lost_count = 0
        num_games = 100
        for game in range(0,num_games):

            memField = copy.deepcopy(aField) #deep copying is necessary here

            players = [-1, 1]
            turn = 0

            while winner == 0:
                player = players[turn % 2]
                if memField.empties:
                    empty_field = random.choice(memField.empties)
                    memField.add_stone(empty_field, player)
                else:
                    break
                winner = memField.check_winner(win_row)
                turn += 1

            if winner == 1:
                won_count = won_count + 1
            if winner == -1:
                lost_count = lost_count + 1
            winner = 0

        eval = won_count * math.exp(-lost_count/math.sqrt(num_games)) / num_games
        y.append(eval)

    return y

def flip(aField):
    """
    Flips the board by multiplying all the values by -1.
    """
    for i in range(aField.dimensions[0]):
        for j in range(aField.dimensions[1]):
            for k in range(aField.dimensions[2]):
                aField.matrix[i][j][k].value = - 1 * aField.matrix[i][j][k].value
    #return aField

def unfold_board(aField):
    """
    Return the board configuration as a list x
    """
    x = []
    for i in range(aField.dimensions[0]):
        for j in range(aField.dimensions[1]):
            for k in range(aField.dimensions[2]):
                x.append((aField.matrix[i][j][k]).value)
    return x


"""
An example of training data generation:

X_fields = nngen.generate_X_train_data(5,5,5,100,3,0)
y = nngen.evaluate_rnd(X_fields, 3, 0)

thefile = open('data.txt', 'w')
for i, item in enumerate(X_fields):
    aList = nngen.unfold_board(item)
    a = ''
    for q in aList:
        a += str(q) + ' '
    a += str(y[i]) + '\n'
    thefile.write(a)
thefile.close()
"""





















