from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0

        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # Initialize a set to keep track of visited cells
        visit = set()

        # Initialize the count of islands to 0
        islands = 0

        # Define a BFS function to explore the island
        def bfs(r, c):
            # Create a deque to store the cells to be visited
            q = collections.deque()
            # Add the current cell to the visited set and the queue
            visit.add((r, c))
            q.append((r, c))

            # Perform BFS traversal
            while q:
                # Get the cell from the left end of the queue
                row, col = q.popleft()
                # Define the four possible directions to explore
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Explore each direction
                for dr, dc in direction:
                    # Calculate the new coordinates
                    nr, nc = row + dr, col + dc
                    # Check if the new coordinates are within the grid boundaries
                    # and if the cell is part of the island and has not been visited yet
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == "1" and ((nr, nc) not in visit):
                        # Add the new cell to the queue and mark it as visited
                        q.append((nr, nc))
                        visit.add((nr, nc))

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell represents part of an unvisited island
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Explore the island using BFS
                    bfs(r, c)
                    # Increment the island count
                    islands += 1

        # Return the total number of islands found
        return islands
