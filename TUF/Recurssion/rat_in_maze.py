"""Consider a rat placed at (0, 0) in a square matrix mat of order n* n. It has to reach the destination at 
(n - 1, n - 1). Find all possible paths that the rat can take to reach from source to destination. The directions
in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix 
represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that
rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any
other cell. In case of no path, return an empty list. The driver will output "-1" automatically."""

from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # Helper function for recursive DFS traversal
        def fun(x, y, s):
            # If we reach the bottom-right cell, add the path to the answer list
            if x == n - 1 and y == n - 1:
                ans.append(s)
                return
            
            # Boundary and obstacle check: if out of bounds or on a blocked cell, stop recursion
            if x >= n or y >= n or x < 0 or y < 0 or m[x][y] == 0:
                return 
            
            # Mark the cell as visited by setting it to 0 (avoiding revisits)
            m[x][y] = 0
            
            # Explore all four possible directions and accumulate the path in string `s`
            fun(x + 1, y, s + "D")  # Move Down
            fun(x - 1, y, s + "U")  # Move Up
            fun(x, y + 1, s + "R")  # Move Right
            fun(x, y - 1, s + "L")  # Move Left
            
            # Unmark the cell after exploring all paths, for other potential paths
            m[x][y] = 1

        ans = []  # List to store all valid paths
        n = len(m)  # Size of the matrix

        # Edge case: if start or end cell is blocked, return "-1"
        if m[0][0] != 1 or m[-1][-1] != 1:
            return ["-1"]

        # Start DFS from the top-left corner (0,0)
        fun(0, 0, "")
        
        # Return all paths found, or "-1" if no path exists
        if ans:
            return ans 
        return ["-1"]
