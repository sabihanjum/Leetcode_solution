"""You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves."""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                not grid[r][c] or (r, c) in visit):
                return 0
            visit.add((r,c))
            res = 1
            direct = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in direct:
                res += dfs(r + dr, c + dc)
            return res

        visit = set()
        land, borderLand = 0, 0
        for r in  range(ROWS):
            for c in range(COLS):
                land += grid[r][c]
                if (grid[r][c] and (r, c) not in visit and
                    (c in [0, COLS - 1] or r in [0, ROWS - 1])):
                    borderLand += dfs(r, c)
        return land - borderLand