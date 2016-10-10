import setting
from interface.field import Field
import re


class Game(object):
    def __init__(self):
        self.solver_turn = True
        self.field = self.create_game()
        print(self.solver_turn)
        self.winner = None
        self.turn()
        self.turn()
        self.turn()
        self.turn()


    def create_game(self):
        while True:
            user_input = input(setting.welcome_text)
            if user_input in setting.yes:
                self.solver_turn = True
                break
            elif user_input in setting.no:
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

    def prompt_coordinates(self):
        while True:
            user_input = input(":")
            valid_input = re.match('^\d*,\d*,\d*$', user_input)
            if valid_input:
                list_of_dimensions = user_input.split(",")
                return list_of_dimensions
            else:
                print(setting.wrong_dimension)

    def end_game(self):
        pass

    def user_turn(self):
        print(setting.player_question)
        coordinates = self.prompt_coordinates()
        x = coordinates[0]
        y = coordinates[1]
        z = coordinates[2]
        #TODO try using SET instead of list
        if self.field.valid_position(x,y,z):
            if self.field.empty_position(x,y,z):
                self.field.add_stone(x,y,z)
            else:
                print(setting.position_occupied)
                self.user_turn()
        else:
            print(setting.outside_of_field)
            self.user_turn()


    def turn(self):
        if self.solver_turn:
            self.field.guess_stone(2)
            #todo: replace 2 with player value or something like that
            self.solver_turn = False
        else:
            self.user_turn()
            self.solver_turn = True

Game()