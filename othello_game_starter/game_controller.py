from player import Player
from human import Human
from comp import Comp
from board import Board
from input import Input
from calculate import Calculate
import time


class GameController:
    '''Creates a game controller to start game'''

    def __init__(self, WIDTH, HEIGHT, MARGIN, DIMENSION, DOUBLE_COMP):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MARGIN = MARGIN
        self.DOUBLE_COMP = DOUBLE_COMP
        self.CENTER = self.WIDTH // 2 + self.MARGIN
        self.DIMENSION = DIMENSION
        self.SPACING = 2  # spacing to display score and turn
        self.board = Board(WIDTH, HEIGHT, MARGIN, DIMENSION)
        # self.player1 = Human(self.board, True)
        self.player1 = (Comp(self.board, True, self) if self.DOUBLE_COMP else
                        Human(self.board, True))
        self.player2 = Comp(self.board, False, self)
        self.game_over = False
        self.prompt = True
        self.timer = 0

    def start_game(self):
        '''Setup board in setup()'''
        self.board.init_board()
        self.player1.legal_moves()
        self.score_game()
        self.update_display()

    def check_game_over(self):
        '''Checks if game is over when all pieces on board have colors'''
        if (self.player1.skip and self.player2.skip and self.prompt):
            self.update_display()
            self.game_over = True
            self.end_game()
            self.prompt = False

    def end_game(self):
        '''Displays score of the players when game is over'''
        Input.end_prompt(self.player1.score, self.player2.score)

    def try_click(self):
        '''Checks if it's the computer's turn and if timer is 0'''
        if self.DOUBLE_COMP:
            if self.player1.active:
                self.player1.minimax_move()
            else:
                self.player2.minimax_move()
        elif self.player2.active and self.timer == 0:
            self.timer = 1
            while self.timer:
                time.sleep(1)
                self.timer -= 1
            self.player2.weighted_move()

    def play_game(self, player1, player2, col, row):
        '''Helper function for player to play game'''
        if len(player1.moves[(col, row)]) > 0:
            player1.place_disk(col, row)
            player1.flip_disk(col, row)
            self.board.init_colors()
            self.score_game()
            self.end_turn(player2)
            if player2.skip:
                self.end_turn(player1)
                if player1.skip:
                    self.end_turn(player2)

    def score_game(self):
        '''Scores points for both players'''
        self.player1.score_points()
        self.player2.score_points()

    def end_turn(self, player):
        '''Cleanup step for ending a player's turn'''
        self.switch_player()
        player.legal_moves()
        self.update_display()
        self.update_skips()

    def switch_player(self):
        '''Switches the players' active status'''
        self.player1.active = not self.player1.active
        self.player2.active = not self.player2.active

    def update_display(self):
        '''Updates board in draw()'''
        background("#006600")
        self.board.display_board()
        self.display_circle()
        self.display_score()
        self.display_turn()

    def display_circle(self):
        '''Displays circles to be highlighted for active player'''
        if self.player1.active:
            self.player1.high_disk()
        else:
            self.player2.high_disk()

    def display_score(self):
        '''Displays the score of each player on the top of the window'''
        fill(0)
        textAlign(CENTER)
        textSize(self.board.MARGIN // self.SPACING)
        s = ("BLACK: " + str(self.player1.score)
             + " - WHITE: " + str(self.player2.score))
        text(s, self.CENTER, self.MARGIN // self.SPACING)

    def display_turn(self):
        '''Display whose turns it is on the bottom of the window'''
        fill(0)
        textAlign(CENTER)
        textSize(self.board.MARGIN // self.SPACING)
        if self.player1.active:
            s = "Player one's turn!"
        else:
            s = "Player two's turn!"
        text(s, self.CENTER,
             self.HEIGHT + self.MARGIN + self.MARGIN // self.SPACING)

    def update_skips(self):
        '''Checks if either player or both player have moves left'''
        self.player1.check_moves()
        self.player2.check_moves()

    def click_mouse(self, mouseX, mouseY):
        '''Registers mouse click for player to place disk'''
        col = (mouseX - self.MARGIN) // self.board.SIZE
        row = (mouseY - self.MARGIN) // self.board.SIZE
        if self.board.disks[row][col].color is None:
            if self.player1.active:
                self.play_game(self.player1, self.player2, col, row)
            else:
                self.play_game(self.player2, self.player1, col, row)
