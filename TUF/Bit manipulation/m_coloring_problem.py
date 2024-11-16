"""You are given an undirected graph consisting of v vertices and a list of edges, along with an integer m. 
Your task is to determine whether it is possible to color the graph using at most m different colors such that 
no two adjacent vertices share the same color. Return true if the graph can be colored with at most m colors, 
otherwise return false.

Note: The graph is indexed with 0-based indexing."""

class Solution:
    def graphColoring(self, v, edges, m):
        """
        v: Number of vertices in the graph
        edges: List of edges (pairs of vertices)
        m: Maximum number of colors allowed
        """
        # Step 1: Build the adjacency list to represent the graph
        adj_list = [[] for i in range(v)]  # Adjacency list for v vertices
        colors = [0] * v  # Array to store colors assigned to each vertex
        
        # Populate the adjacency list from the edges
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])  # Graph is undirected

        # Helper function to check if a given color can be assigned to a node
        def is_possible_color(node, color):
            """
            Check if we can assign 'color' to 'node' without conflicts.
            """
            for neighbor in adj_list[node]:  # Iterate through all neighbors of the node
                if colors[neighbor] == color:  # If a neighbor has the same color, conflict
                    return False
            return True  # No conflicts, the color can be assigned

        # Recursive function to solve the graph coloring problem
        def solve(node, graph):
            """
            Attempt to assign colors starting from 'node'.
            """
            # Base case: If all nodes are processed, return True
            if node == v:
                return True

            # Try assigning each color from 1 to m
            for color in range(1, m + 1):
                # Check if the color can be assigned to the current node
                if is_possible_color(node, color):
                    colors[node] = color  # Assign the color
                    # Recursively attempt to color the rest of the graph
                    if solve(node + 1, graph):
                        return True
                    # Backtrack if coloring the remaining graph fails
                    colors[node] = 0

            # If no color can be assigned, return False
            return False

        # Start the coloring process from node 0
        return solve(0, adj_list)


