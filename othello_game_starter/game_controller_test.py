from game_controller import GameController


def test_game_controller():
    game_controller = GameController(800, 800, 100, 4, False)
    game_controller.board.init_board()

    assert game_controller.HEIGHT is 800
    assert game_controller.WIDTH is 800
    assert game_controller.MARGIN is 100
    assert game_controller.DIMENSION is 4
    assert game_controller.DOUBLE_COMP is False
    assert game_controller.game_over is False
    assert game_controller.prompt is True

    # start_game() contains graphical functionality

    # check_game_over() contains graphical functionality

    # end_game() is graphical functionality

    # play_game() contains graphical functionality

    game_controller.board.init_colors()
    game_controller.score_game()
    assert game_controller.player1.score is 2
    assert game_controller.player2.score is 2

    # end_turn() contains graphical functionality

    game_controller.switch_player()
    assert game_controller.player1.active is False
    assert game_controller.player2.active is True
    game_controller.switch_player()

    # update_display() is a graphical functionality

    # display_circle() is a graphical functionality

    # display_score() is a graphical functionality

    # display_turn() is a graphical functionality

    game_controller.board.set_disk_color(1, 1, True)
    game_controller.board.set_disk_color(2, 2, True)
    game_controller.player1.legal_moves()
    game_controller.player2.legal_moves()
    game_controller.update_skips()
    game_controller.player1.skip is True
    game_controller.player2.skip is True

    # click_mouse() contains graphical functionality
