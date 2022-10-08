import unittest
import tic_tac_toe
import subprocess


class MyTestCase(unittest.TestCase):
    def test_input(self):
        game = tic_tac_toe.TicTacToeGame()
        self.assertEqual(game.validate_input("3"), 3)
        self.assertEqual(game.validate_input("7"), 7)
        self.assertEqual(game.validate_input("10"), False)
        self.assertEqual(game.validate_input("R10"), False)
        game.game_board = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(game.validate_input("0"), False)
        self.assertEqual(game.validate_input("2"), 2)

    def test_make_move(self):
        game = tic_tac_toe.TicTacToeGame()
        self.assertEqual(len(game.cross_position), 0)
        game.make_move(1, 1)
        self.assertEqual(game.game_board[0], 1)
        self.assertEqual(game.cross_position[0], 0)

    def test_check_win(self):
        game = tic_tac_toe.TicTacToeGame()
        game.make_move(1, 1)
        game.make_move(1, 2)
        self.assertEqual(game.check_win(), 0)
        game.make_move(1, 3)
        self.assertEqual(game.check_win(), 1)
        game = tic_tac_toe.TicTacToeGame()
        game.make_move(1, 1)
        game.make_move(1, 4)
        self.assertEqual(game.check_win(), 0)
        game.make_move(1, 7)
        self.assertEqual(game.check_win(), 1)
        game = tic_tac_toe.TicTacToeGame()
        game.make_move(2, 1)
        self.assertEqual(game.check_win(), 0)
        game.make_move(2, 4)
        game.make_move(2, 7)
        self.assertEqual(game.check_win(), 2)


if __name__ == '__main__':
    unittest.main()
