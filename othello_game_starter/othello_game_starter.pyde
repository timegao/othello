from game_controller import GameController
from player import Player
import time


# ANY OF THE FIELDS BELOW CAN BE MODIFIED! (ABOVE BELOW)
WIDTH = 800 # WIDTH OF THE BOARD
HEIGHT = 800  # HEIGHT OF THE BOARD
MARGIN = 100  # MARGINS OF THE BOARD
DIMENSION = 8  # DIMENSIONS OF THE BOARD
DOUBLE_COMP = False  # SET TO TRUE TO WATCH COMPUTERS PLAY EACH OTHER!
# ANY OF THE FIELDS ABOVE CAN BE MODIFIED! (BELOW ABOVE)


game_controller = GameController(WIDTH, HEIGHT, MARGIN, DIMENSION, DOUBLE_COMP)


def setup():
    size(WIDTH + 2 * MARGIN, HEIGHT + 2 * MARGIN)
    game_controller.start_game()

def draw():
    game_controller.check_game_over()
    if game_controller.game_over is False:
        game_controller.try_click()

def mouseClicked():
    game_controller.click_mouse(mouseX, mouseY)
