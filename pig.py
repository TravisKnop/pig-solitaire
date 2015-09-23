import random

class Game:

    def __init__(self, player, computer, turn=0):
        self.player = player
        self.computer = computer
        self.turn = 0

    player_score = 0
    computer_score = 0

    def start_up(self):
        print("Here we go!")
        self.select_player()

    def select_player(self):
        while self.turn % 2 > 0:
            self.player.start_player_turn()
            self.player_score += self.player.score_on_turn
            self.turn += 1
            print("The score is human: {} to computer:{}\n".format(self.player_score, self.computer_score))
            self.player.score_on_turn = 0
            return self.select_player()
        while self.turn % 2 < 1:
            self.computer.start_computer_turn()
            self.computer_score += self.computer.score_on_turn
            self.turn +=1
            print("After {} rounds, the score is \n human: {} to computer:{}\n".format(int(self.turn/2-0.5), self.player_score, self.computer_score))
            self.computer.score_on_turn = 0
        if self.turn >= 14:
            self.run_game_over()
        else:
            return self.select_player()

    def run_game_over(self):
        if self.player_score > self.computer_score:
            print("YOU WON!!! \nThe final score was {} to {}".format(self.player_score, self.computer_score))
        elif self.player_score == self.computer_score:
            print("WOW!!! A tie! \n\nHow's about a rematch? Loser buys thai.\n")
        else:
            print("Ooh, tough break. I beat you {} to {}\n".format(self.player_score, self.computer_score))

        self.play_again = input("Want to play again? ")
            if self.play_again == "y":
                g.start_up()


class Player:

    def __init__(self):
        self.score_on_turn = 0
        pass

    def start_player_turn(self):
        player_command = input("It's your turn. Do you want to roll? ")
        if player_command == "y":
            self.player_roll()
        else:
            self.player_end_turn()

    def player_roll(self):
        dice_roll = random.randint(1, 6)
        if dice_roll == 1:
            self.score_on_turn = 0
            print("rolling... {}!".format(dice_roll))
            print("Oh, too bad! You get no points :-(\n")
            self.player_end_turn()
        else:
            self.score_on_turn += dice_roll
            print("rolling... {}        {} points on the table...".format(dice_roll, self.score_on_turn))
            return self.start_player_turn()

    def player_end_turn(self):
        return self.score_on_turn


class Computer:
    def __init__(self):
        self.score_on_turn = 0

    def start_computer_turn(self):
        dice_roll = random.randint(1, 6)
        if dice_roll == 1:
            self.score_on_turn = 0
            print("rolling... {}".format(dice_roll))
            print("Oh no, I busted :-(")
            self.computer_end_turn()
        else:
            self.score_on_turn += dice_roll
            print("rolling... {}       I'm looking at {} points this round!".format(dice_roll, self.score_on_turn))
            self.computer_decide()
            return self.score_on_turn

    def computer_decide(self):
        pos = random.random()
        if pos > 0.75:
            print("That's it, I'm done for this turn.\n")
            self.computer_end_turn()
        else:
            self.start_computer_turn()

    def computer_end_turn(self):
        return self.score_on_turn
