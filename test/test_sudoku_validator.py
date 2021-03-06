import unittest

from app.sudoku import SudokuValidator

class SudokuValidatorTest(unittest.TestCase):
    def test_valid_board(self):
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        result = SudokuValidator().isValidSudoku(board)
        self.assertEqual(result, True)
        
    def test_invalid_line(self):
        board = [
            ["1","2","3",".",".","3",".",".","."],
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
        self.assertEqual(result, False)
        
    def test_invalid_column(self):
        board = [
            [".",".",".",".","2",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".","9",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".","3",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".","1",".",".",".","."],
            [".",".",".",".","2",".",".",".","."]
        ]
        result = SudokuValidator().isValidSudoku(board)
        self.assertEqual(result, False)
        
    def test_invalid_box(self):
        board = [
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".","3",".","6",".",".","."],
            [".",".",".",".","3",".",".",".","."],
            [".",".",".",".",".","4",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."]
        ]
        result = SudokuValidator().isValidSudoku(board)
        self.assertEqual(result, False)

