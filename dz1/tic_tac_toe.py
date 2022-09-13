class TicTacToeGame:
    def __init__(self):
        self.game_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cross_position = []
        self.nought_position = []
        self.WINNER_POSITIONS = [[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8],
                                 [0, 3, 6],
                                 [1, 4, 7],
                                 [2, 5, 8],
                                 [0, 4, 8],
                                 [2, 4, 6], ]
        self.curr_move = 1  # 1-cross, 2-naught

    def show_board(self):
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                if self.game_board[index] == 0:
                    print("□", end=" ")
                elif self.game_board[index] == 1:
                    print("X", end=" ")
                elif self.game_board[index] == 2:
                    print("0", end=" ")
            print()

    def check_win(self):
        for position in self.WINNER_POSITIONS:
            if set(self.cross_position) & set(position) == set(position):
                return 1
            if set(self.nought_position) & set(position) == set(position):
                return 2
        return 0

    def make_move(self, move_number, move_position):
        if move_number == 1:
            self.cross_position.append(move_position - 1)
        elif move_number == 2:
            self.nought_position.append(move_position - 1)
        else:
            return
        self.game_board[move_position - 1] = move_number

    def validate_input(self, move_position):
        if not move_position.isnumeric():
            return False
        move_position = int(move_position)
        if move_position < 1 or move_position > 9:
            return False
        if self.game_board[move_position] != 0:
            return False
        return int(move_position)

    def start_game(self):
        win_game = 0
        i = 0
        self.show_board()
        while win_game == 0:
            move = input("ход: ")
            valid_move = self.validate_input(move)
            if valid_move:
                self.make_move(self.curr_move, valid_move)
                self.curr_move %= 2
                self.curr_move += 1
            else:
                continue
            win_game = self.check_win()
            self.show_board()

        if win_game == 1:
            print("Поздравляем игрока -Х-")

        elif win_game == 2:
            print("Поздравляем игрока -0-")


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
