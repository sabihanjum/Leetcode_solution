"""Given a undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Traversal (BFS) starting from vertex 0, visiting vertices from left to right according to the adjacency list, and return a list containing the BFS traversal of the graph.

Note: Do traverse in the same order as they are in the adjacency list."""

from typing import List
from collections import deque

class Solution:
    def bfsOfGraph(self, v: int, adj: List[List[int]]) -> List[int]:
        visited = [False] * v  # To track visited nodes
        q = deque([0])  # Using deque for efficient O(1) popping
        ans = []
        
        visited[0] = True  # Mark the first node as visited
        
        while q:
            s = q.popleft()  # Dequeue
            ans.append(s)
            
            for neighbor in adj[s]:  # Iterate over neighbors
                if not visited[neighbor]:
                    visited[neighbor] = True  # Mark as visited
                    q.append(neighbor)  # Enqueue
        
        return ans