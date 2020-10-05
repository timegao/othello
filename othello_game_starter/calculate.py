from collections import defaultdict
import copy


class Calculate:
    '''Calculates legal moves for both players'''
    '''Calculates coordinate for computer to place disk'''

    @staticmethod
    def legal_moves(player):
        '''Populates self.moves dictionary with valid moves'''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                      (1, 1), (-1, -1), (-1, 1), (1, -1)]
        player.moves = defaultdict(set)  # resets a player's moves
        player.board.init_colors()
        if None in player.board.colors.keys():  # iterates through no colors
            for disk in player.board.colors[None]:
                for d in directions:  # see list of tuples aboves
                    for tuple in Calculate.check_line(player, disk[0],
                                                      disk[1], d[0], d[1]):
                        player.moves[(disk[0], disk[1])].add(tuple)

    @staticmethod
    def check_line(player, col, row, col_delta, row_delta):
        '''Appends tuples to set of disks to flip'''
        # Checks different directions of empty squares, and if same color is
        # found, adds coordinates to a list. continuing down the same direction
        # if the direction ends in a different color, return the list.
        # Otherwise, return an empty list and check another direction.
        #
        # 'b' is black, 'w' is white, 'n' is none, player is 'b' color,
        # direction is (0, 1) which is the same as going right on a row
        #
        #    0   1   2   3
        # 0 'n' 'w' 'b' 'n'
        # 1
        # 2
        # 3
        # -> (0, 0) returns [(1, 0)] because a 'w' is encountered then 'b'
        #
        #    0   1   2   3
        # 0 'n' 'w' 'w' 'w'
        # 1
        # 2
        # 3
        # -> (0, 0) returns [] because no same color('b') is encountered
        #
        #    0   1   2   3
        # 0 'n' 'b' 'w' 'w'
        # 1
        # 2
        # 3
        # -> (0, 0) returns [] because the first color encountered is 'b'
        # -> The same is true if the first color encountered is 'n'
        #
        lst = []
        new_col = col + col_delta
        new_row = row + row_delta
        # checks if new location is within the board
        while (new_col < player.board.cols and new_col >= 0 and
               new_row < player.board.rows and new_row >= 0):
            new_color = player.board.disks[new_row][new_col].color
            if new_color is None:  # returns [] when None
                break
            elif new_color is player.color:  # returns list when same color
                return lst
            elif new_color == (not player.color):  # appends to list when diff
                lst.append((new_col, new_row))
            new_col += col_delta  # continue down the same direction if
            new_row += row_delta  # different color is encountered
        return []

    @staticmethod
    def minmax_move(game_controller, player):
        '''Finds move for computer that minimizes other player's moves'''
        # First checks if a corner square is available and captures it.
        # Then iterates through available legal moves and checks whether
        # Each of them enables the opponent to capture a corner square. If it
        # does, marks it as a bad move. Of the moves that are not bad moves,
        # Calculates the number of legal moves that it would give the opponent
        # If said move is taken and returns the move that gives the opponent
        # The least number of legal moves.
        width = game_controller.DIMENSION - 1
        height = game_controller.DIMENSION - 1
        corners = [(0, 0), (0, height), (width, 0), (width, height)]
        good_moves = []
        for move in player.moves.keys():
            if move in corners:
                return move
            else:
                new_controller = copy.deepcopy(game_controller)
                Calculate.add_move(move[0], move[1], new_controller)
                bad_move = False  # a move is bad if it enables a corner
                for tries in new_controller.player1.moves.keys():
                    if tries in corners:
                        bad_move = True
                if not bad_move:
                    good_moves.append((move[0], move[1],
                                       len(new_controller.player1.moves)))
        if len(good_moves) == 0:  # edge case when all moves are bad moves
            return player.moves.keys()[0]
        else:  # pick the move that gives player1 the least options
            return sorted(good_moves, key=lambda x: x[2], reverse=False)[0]

    @staticmethod
    def weighted_move(game_controller, player):
        moves = []
        for move in player.moves.keys():
            flips = len(player.moves[move])
            weight = Calculate.weigh(move[0], move[1], game_controller)
            moves.append((weight, flips, move))
        chosen_move = sorted(moves)[-1][-1]
        return chosen_move

    @staticmethod
    def weigh(col, row, game_controller):
        weight = 0
        width = game_controller.DIMENSION - 1
        height = game_controller.DIMENSION - 1
        corners = [(0, 0), (0, height), (width, 0), (width, height)]
        if (col, row) in corners:
            weight += 4
        if Calculate.is_edge(col, row, game_controller):
            weight += 2
        new_controller = copy.deepcopy(game_controller)
        Calculate.add_move(col, row, new_controller)
        for move in new_controller.player1.moves.keys():
            if move in corners:
                weight -= 3
            if Calculate.is_edge(move[0], move[1], new_controller):
                weight -= 1
        return weight

    @staticmethod
    def is_edge(col, row, game_controller):
        return ((row == 0 or row == game_controller.board.DIMENSION - 1)
                or (col == 0 or col == game_controller.board.DIMENSION - 1))

    @staticmethod
    def add_move(col, row, game_controller):
        '''Given the col row coordinates, clicks mouse within square'''
        mouseX = (int((col + 0.5) * game_controller.board.SIZE +
                      game_controller.board.MARGIN))
        mouseY = (int((row + 0.5) * game_controller.board.SIZE +
                      game_controller.board.MARGIN))
        game_controller.click_mouse(mouseX, mouseY)

    @staticmethod
    def greedy_move(game_controller, player):
        '''Calculates the move that flips the most disks'''
        best_move, tiles = "", 0
        for move in player.moves.keys():
            if len(player.moves[move]) > tiles:
                best_move = move
        return best_move
