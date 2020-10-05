from game_controller import GameController


def test_board():
    game_controller = GameController(800, 800, 100, 4, False)
    game_controller.board.init_board()

    assert game_controller.board.disks[1][1].color is False
    assert game_controller.board.disks[2][2].color is False
    assert game_controller.board.disks[1][2].color is True
    assert game_controller.board.disks[2][1].color is True

    # display_board() method is a graphical functionality

    game_controller.board.init_colors()
    assert len(game_controller.board.colors[True]) == 2
    assert len(game_controller.board.colors[False]) == 2

    game_controller.board.set_disk_color(2, 1, False)
    assert game_controller.board.disks[1][2].color is False
    game_controller.board.set_disk_color(0, 0, True)
    assert game_controller.board.disks[0][0].color is True
    game_controller.board.set_disk_color(0, 0, None)
    assert game_controller.board.disks[0][0].color is None

    # light_disk() method is a graphical functionality
