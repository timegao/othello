from disk import Disk
from board import Board
from calculate import Calculate
from collections import defaultdict


class Player():
    '''Player superclass for Human and Comp classes to inherit'''

    def __init__(self, board, color):
        self.board = board
        self.color = color  # Black is True, White is False
        self.active = self.color
        self.score = 0
        self.skip = False
        self.moves = defaultdict(set)

    def place_disk(self, col, row):
        '''Passes col, row, and color to board to set color and score points'''
        self.board.set_disk_color(col, row, self.color)

    def flip_disk(self, col, row):
        '''Passes col and row from self.moves to board to flip'''
        for tup in self.moves[(col, row)]:
            self.board.set_disk_color(tup[0], tup[1], self.color)

    def high_disk(self):
        '''Passes col and row to board to highlight'''
        for key in self.moves.keys():
            if len(self.moves[key]) > 0:
                self.board.light_disk(key[0], key[1])

    def check_moves(self):
        '''Checks if a player has any legal move'''
        skip_turn = True
        for key in self.moves.keys():
            if len(self.moves[key]) > 0:
                skip_turn = False  # if legal move found, skip is False
        self.skip = skip_turn

    def score_points(self):
        '''Score the player's point according to their colored disk on board'''
        self.score = len(self.board.colors[self.color])

    def legal_moves(self):
        '''Calculate class calculates the legal moves'''
        Calculate.legal_moves(self)
