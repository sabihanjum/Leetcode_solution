"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells."""

import string

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # Helper function to check if placing a character 'c' at (row, col) is valid
        def isValid(row: int, col: int, c: str) -> bool:
            # Check the column for any duplicate
            for i in range(9):
                if board[i][col] == c:
                    return False
            # Check the row for any duplicate
            for i in range(9):
                if board[row][i] == c:
                    return False
            # Check the 3x3 subgrid for any duplicate
            for i in range(3):
                for j in range(3):
                    if board[3 * (row // 3) + i][3 * (col // 3) + j] == c:
                        return False
            return True

        # Recursive function to try and solve the Sudoku by filling the board
        def solve(s: int) -> bool:
            # If s == 81, it means we've filled all 81 cells correctly, so return True
            if s == 81:
                return True

            # Calculate the row (i) and column (j) from the linear index (s)
            i = s // 9
            j = s % 9

            # If the current cell is already filled, skip it and move to the next one
            if board[i][j] != '.':
                return solve(s + 1)

            # Try placing digits 1-9 (excluding 0) into the current empty cell
            for c in string.digits[1:]:
                # Check if placing the digit 'c' at (i, j) is valid
                if isValid(i, j, c):
                    # Place the digit 'c' and recursively try to solve the rest
                    board[i][j] = c
                    if solve(s + 1):
                        return True
                    # If not valid, backtrack and remove the digit
                    board[i][j] = '.'

            # If no valid digit can be placed, return False to trigger backtracking
            return False

        # Start solving the Sudoku from the first cell
        solve(0)
