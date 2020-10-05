from game_controller import GameController


def test_player():
    game_controller = GameController(800, 800, 100, 4, False)
    assert game_controller.player1.color is True
    assert game_controller.player1.active is True
    assert game_controller.player1.score is 0

    game_controller.board.init_board()
    game_controller.player1.legal_moves()
    #    0  1  2  3
    # 0 'n''n''n''n'
    # 1 'n''w''b''n'
    # 2 'n''b''w''n'
    # 3 'n''n''n''n'
    game_controller.player1.place_disk(1, 0)
    #    0  1  2  3
    # 0 'n''b''n''n'
    # 1 'n''w''b''n'
    # 2 'n''b''w''n'
    # 3 'n''n''n''n'
    game_controller.player1.flip_disk(1, 0)
    #    0  1  2  3
    # 0 'n''b''n''n'
    # 1 'n''b''b''n'
    # 2 'n''b''w''n'
    # 3 'n''n''n''n'
    assert game_controller.board.disks[0][1].color is True
    game_controller.player1.place_disk(2, 3)
    #    0  1  2  3
    # 0 'n''b''n''n'
    # 1 'n''b''b''n'
    # 2 'n''b''w''n'
    # 3 'n''n''b''n'
    game_controller.player1.flip_disk(2, 3)
    #    0  1  2  3
    # 0 'n''b''n''n'
    # 1 'n''b''b''n'
    # 2 'n''b''b''n'
    # 3 'n''n''b''n'
    assert game_controller.board.disks[3][2].color is True
    print(game_controller.board.disks)

    # high_disk() method is a graphical functionality

    game_controller.player1.legal_moves()
    game_controller.player1.check_moves()
    assert game_controller.player1.skip is True
    game_controller.board.init_colors()
    game_controller.player1.score_points()
    assert game_controller.player1.score is 6
    assert game_controller.player2.score is 0
