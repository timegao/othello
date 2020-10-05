from player import Player
from collections import defaultdict
from calculate import Calculate


class Comp(Player):
    '''Creates a computer player'''

    def __init__(self, board, color, game_controller):
        self.game_controller = game_controller
        self.board = board
        self.color = color  # Black is True, White is False
        self.active = self.color
        self.score = 0
        self.skip = False
        self.moves = defaultdict(set)

    def minmax_move(self):
        '''Creates coordinates for computer to pass to game_controller'''
        triple = Calculate.minmax_move(self.game_controller, self)
        Calculate.add_move(triple[0], triple[1], self.game_controller)

    def greedy_move(self):
        '''Creates coordinates for computer to pass to game_controller'''
        double = Calculate.greedy_move(self.game_controller, self)
        Calculate.add_move(double[0], double[1], self.game_controller)

    def weighted_move(self):
        '''Creates coordinates for computer to pass to game_controller'''
        double = Calculate.weighted_move(self.game_controller, self)
        print(double)
        Calculate.add_move(double[0], double[1], self.game_controller)
