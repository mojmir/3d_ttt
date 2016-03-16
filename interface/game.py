import setting
from interface.field import Field
import re


class Game(object):
    def __init__(self):
        self.solver_turn = True
        self.field = self.create_game()
        print(self.solver_turn)
        self.winner = None

    def create_game(self):
        while True:
            user_input = input(setting.welcome_text)
            if user_input == setting.yes:
                self.solver_turn = True
                break
            elif user_input == setting.no:
                self.solver_turn = False
                break
            else:
                print(setting.wrong_yes_no)
        while True:
            user_input = input(setting.dimension_question)
            valid_input = re.match('^\d*,\d*,\d*$', user_input)
            if valid_input:
                list_of_dimensions = user_input.split(",")
                dimension_x = int(list_of_dimensions[0])
                dimension_z = int(list_of_dimensions[1])
                dimension_y = int(list_of_dimensions[2])
                prepared_field = Field(dimension_x, dimension_y, dimension_z)
                return prepared_field
            else:
                print(setting.wrong_dimension)

