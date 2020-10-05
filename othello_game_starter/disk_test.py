from game_controller import GameController


def test_disk():
    game_controller = GameController(800, 800, 100, 4, False)
    game_controller.board.init_board()

    assert game_controller.board.disks[1][2].color is True
    assert game_controller.board.disks[1][2].row is 1
    assert game_controller.board.disks[1][2].col is 2
    assert game_controller.board.disks[3][2].color is None
    print(repr(game_controller.board.disks[2][2]))
    assert repr(game_controller.board.disks[2][2]) == "Disk(22False)"

    # display() method is a graphical functionality

    # highlight() method is a graphical functionality

    # make_circle() method is a graphical functionality
