"""Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere."""

from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        res = [[] for i in range(V)]
        
        for v1, v2 in edges:
            res[v1].append(v2)
            res[v2].append(v1)
        return res