from game_controller import GameController
from calculate import Calculate


def test_calculate():
    game_controller = GameController(800, 800, 100, 4, False)
    game_controller.board.init_board()
    Calculate.legal_moves(game_controller.player1)
    assert len(game_controller.player1.moves) is 4
    assert (0, 1) in game_controller.player1.moves.keys()
    assert (1, 0) in game_controller.player1.moves.keys()

    game_controller.player1.place_disk(1, 0)
    game_controller.player1.flip_disk(1, 0)
    Calculate.legal_moves(game_controller.player2)
    assert Calculate.minmax_move(game_controller,
                                 game_controller.player2) == (0, 0)
    assert Calculate.greedy_move(game_controller,
                                 game_controller.player2) == (0, 2)

    # add_move() contains graphical functionality
