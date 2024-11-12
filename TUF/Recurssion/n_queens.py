"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively."""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Sets to track columns and diagonals where queens are placed
        col = set()        # Columns where queens are placed
        posDiag = set()    # Positive diagonals (r + c)
        negDiag = set()    # Negative diagonals (r - c)

        res = []           # Final result to store valid board configurations
        board = [["."] * n for _ in range(n)]  # Initialize n x n board with "."

        # Helper function for backtracking
        def backtrack(r):
            # If we've placed queens in all rows, add the current board configuration to results
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try placing a queen in each column of the current row
            for c in range(n):
                # Check if the current cell (r, c) is under attack
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place the queen and mark the column and diagonals
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to the next row
                backtrack(r + 1)

                # Remove the queen and unmark the column and diagonals (backtracking)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        # Start backtracking from the first row
        backtrack(0)
        return res
