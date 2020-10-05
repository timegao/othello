class Disk:
    '''Creates a disk to put on the board'''

    def __init__(self, col, row, color, SIZE, MARGIN):
        self.row = row
        self.col = col
        self.color = color  # Black is True, White is False
        self.SIZE = SIZE
        self.MARGIN = MARGIN
        self.PERCENT_SQUARE = 0.5
        self.PERCENT_CIRCLE = 0.9

    def display(self):
        '''Display disk as circle on board'''
        if self.color is not None:
            if self.color:
                fill(0)
            else:
                fill(255)
            self.make_circle()

    def highlight(self):
        '''Displays valid plays on board'''
        fill("#006600")
        self.make_circle()

    def make_circle(self):
        circle((self.col + self.PERCENT_SQUARE) * self.SIZE + self.MARGIN,
               (self.row + self.PERCENT_SQUARE) * self.SIZE + self.MARGIN,
               self.PERCENT_CIRCLE * self.SIZE)

    def __repr__(self):
        '''String representation of disk'''
        return (self.__class__.__name__ +
                "(" + str(self.row) + str(self.col) + str(self.color) + ")")
