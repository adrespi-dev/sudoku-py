import unittest

from app.sudoku import SudokuValidator


class VerifyCalculatorTest(unittest.TestCase):
    def test_valid_full_board(self):
        board = [
            ["9","3","4","5","6","8","1","2","7"],
            ["8","2","6","7","1","4","5","9","3"],
            ["1","5","7","9","2","3","4","6","8"],
            ["2","7","8","1","5","9","3","4","6"],
            ["6","4","1","3","8","7","2","5","9"],
            ["3","9","5","6","4","2","7","8","1"],
            ["5","6","3","4","9","1","8","7","2"],
            ["7","8","9","2","3","5","6","1","4"],
            ["4","1","2","8","7","6","9","3","5"]
        ]
        result = SudokuValidator().isValidSudoku(board)
        self.assertEqual(result, True)

    def test_valid_blank_board(self):
        board = [
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."]
        ]
        result = SudokuValidator().isValidSudoku(board)
        self.assertEqual(result, True)

    def test_invalid_full_board(self):
        board = [
            ["9","3","4","5","6","8","1","2","7"],
            ["8","2","6","7","1","4","5","9","3"],
            ["1","5","7","9","2","3","4","6","8"],
            ["2","7","8","1","5","9","3","4","6"],
            ["6","4","1","5","8","7","2","5","9"],
            ["3","9","5","6","4","2","7","8","1"],
            ["5","6","3","4","9","1","8","7","2"],
            ["7","8","9","2","3","5","6","1","4"],
            ["4","1","2","8","7","6","9","3","5"]
        ]
        result = SudokuValidator().isValidSudoku(board)
        self.assertEqual(result, False)
