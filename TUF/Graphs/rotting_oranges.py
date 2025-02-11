"""You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1."""

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        
        # Step 1: Count fresh oranges and enqueue rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # Directions for adjacent cells (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Step 2: BFS Traversal
        while q and fresh > 0:
            for _ in range(len(q)):  # Process all rotten oranges at the current time step
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2  # Mark fresh orange as rotten
                        q.append((row, col))
                        fresh -= 1  # Reduce fresh orange count
            time += 1  # Increase time for each BFS level

        # Step 3: Return time if all oranges are rotten, else return -1
        return time if fresh == 0 else -1