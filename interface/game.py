import setting
from interface.field import Field
import re


class Game(object):
    def __init__(self):
        self.solver_turn = True
        self.turn_counter = 0
        self.field = self.create_game()
        self.win_row = 3
        self.run()
        #TODO remake it for AI ready no-interaface run

    def run(self):
        while True:
            winner = self.turn()
            if winner:
                break

        self.end_game(winner)

    def create_game(self):
        while True:
            user_input = input(setting.welcome_text)
            if user_input in setting.yes:
                self.solver_turn = False
                break
            elif user_input in setting.no:
                self.solver_turn = True
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
            user_input = input("")
            valid_input = re.match('^\d*,\d*,\d*$', user_input)
            if valid_input:
                list_of_dimensions = user_input.split(",")
                return list_of_dimensions
            else:
                print(setting.wrong_dimension)

    def end_game(self, winner_value):
        if winner_value == 2:
            print("Solver won")
        else:
            print("You won. How amazing")

    def user_turn(self):
        print(setting.player_question)
        coordinates = self.prompt_coordinates()
        x = int(coordinates[0])
        y = int(coordinates[1])
        z = int(coordinates[2])#TODO try using SET instead of list
        if self.field.valid_position(x, y, z):
            if self.field.empty_position(x, y, z):#TODO add reasonable way to add user value
                self.field.add_stone(x, y, z, 1)
            else:
                print(setting.position_occupied)
                self.user_turn()
        else:
            print(setting.outside_of_field)
            self.user_turn()

    def turn(self):
        self.turn_counter += 1
        if self.solver_turn:
            self.field.guess_stone(2)#todo: replace 2 with player value or something like that
            self.solver_turn = False
        else:
            self.user_turn()
            self.solver_turn = True
        print("Turn" + str(self.turn_counter))
        print(self.field)

        winner = self.field.check_winner(self.win_row)
        return winner

Game()
