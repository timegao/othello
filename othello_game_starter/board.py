from disk import Disk
from collections import defaultdict


class Board:
    '''Creates a board to put tiles and pieces onto'''

    def __init__(self, WIDTH, HEIGHT, MARGIN, DIMENSION):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MARGIN = MARGIN
        self.DIMENSION = DIMENSION
        self.SIZE = self.WIDTH // self.DIMENSION
        self.cols = self.WIDTH // self.SIZE
        self.rows = self.HEIGHT // self.SIZE
        self.disks = [[Disk(y, x, None, self.SIZE, self.MARGIN)
                      for y in range(self.cols)]
                      for x in range(self.rows)]  # all disks on board

    def display_board(self):
        '''Display all the disks on the board with the lines'''
        strokeWeight(2)  # draw all vertical/horizontal lines
        for coor in range(self.DIMENSION + 1):
            line(coor * self.SIZE + self.MARGIN, self.MARGIN,
                 coor * self.SIZE + self.MARGIN, self.HEIGHT + self.MARGIN)
            line(self.MARGIN, coor * self.SIZE + self.MARGIN,
                 self.WIDTH + self.MARGIN, coor * self.SIZE + self.MARGIN)
        for row in range(self.rows):  # displays all disks on board
            for col in range(self.cols):
                self.disks[row][col].display()

    def init_board(self):
        '''Changes initial 4 disks to black/white colors'''
        left_col, right_col = self.cols // 2 - 1, self.cols // 2
        top_row, bot_row = self.rows // 2 - 1, self.rows // 2
        self.set_disk_color(left_col, top_row, False)
        self.set_disk_color(right_col, bot_row, False)
        self.set_disk_color(right_col, top_row, True)
        self.set_disk_color(left_col, bot_row, True)

    def init_colors(self):
        '''Updates dictionaries of each disk color'''
        self.colors = defaultdict(list)
        for row in range(self.rows):
            for col in range(self.cols):
                self.colors[self.disks[row][col].color].append((col, row))

    def set_disk_color(self, col, row, color):
        '''Given a row, col, and color, set disk to that color'''
        self.disks[row][col].color = color

    def light_disk(self, col, row):
        '''Highlights disks in disks'''
        self.disks[row][col].highlight()
