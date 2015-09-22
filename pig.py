import random

class Game:

    def __init__(self):
        self.turn = 0
        self.computer_score = computer_score():
        self.player_score = player_score():


    def select_player(self):
        if self.turn % 2 > 0:
            self.player_input()
        if self.turn % 2 <= 0:
            self.get_computer_roll()

    def generate_roll(self):
        self.dice_roll = random.randint(6)
        if self.dice_roll == 6:
            self.points_on_turn = 0
            self.run_end_turn()
            return self.points_on_turn
        else:
            self.points_on_turn += self.dice_roll
            return self.points_on_turn

    def run_end_turn(self):
        self.total_score += self.points_on_turn
        self.turn += 1
        if self.turn >= 14:
            self.run_game_over()
        else:
            print("You scored {} points that turn!".format(player_points))
            print("Total Score: {}.".format(player_points))
            return self.points_on_turn


class Player:

    def __init__(self, game):
        self.game = game

    def player_input(self):
        points_on_turn =
        self.player_input = input("Would you like to bank these points? Or roll again?")
        if self.player_input == "bank":
            self.game.run_end_turn()
        elif self.player_input == "roll":
            self.game.generate_roll()
        else:
            print("Sorry, please enter 'bank' or 'roll'!")
            return self.player_input

    def player_score(self):
        self.player_points += self.points_on_turn
        return self.player_points



class Computer:
    def __init__(self, game):
        self.game = game
        pass

    def get_computer_roll(self):
        points_on_turn = 0
        self.computer_roll = self.game.generate_roll()
        print("I rolled a {}".format(self.computer_roll))
        rn = random.random()
        if rn <=0.75:
            print("I think I will roll again.")
            self.get_computer_roll()
            return points_on_turn
        elif rn >0.75:
            print("I think I will bank these points.")
            self.game.run_end_turn()
            return self.computer.points_on_turn

    def computer_score(self):
        self.computer_score = 0 + self.points_on_turn
        return self.computer_points

p = Player()
c = Computer()
g = Game()

print("Welcome to pig!")
p.player_input()
