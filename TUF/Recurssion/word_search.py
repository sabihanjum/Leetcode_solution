"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once."""

from typing import List, Set

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])
        
        # Set to track the current path to avoid revisiting cells
        path: Set[tuple] = set()

        # Depth-First Search (DFS) function to search for the word
        def dfs(r, c, i):
            # If we've reached the end of the word, return True
            if i == len(word):
                return True
            
            # Check if the current position is out of bounds, 
            # or the character doesn't match, or it's already in the path
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            # Add the current cell to the path
            path.add((r, c))
            
            # Explore all 4 directions: down, up, right, left
            res = (dfs(r+1, c, i+1) or  # Move down
                    dfs(r-1, c, i+1) or  # Move up
                    dfs(r, c+1, i+1) or  # Move right
                    dfs(r, c-1, i+1))    # Move left

            # Remove the cell from the path after exploring all directions
            path.remove((r, c))
            
            # Return the result of the recursive search
            return res

        # Start DFS from each cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                # If we find the word starting from any cell, return True
                if dfs(r, c, 0):
                    return True

        # If the word is not found in any path, return False
        return False
