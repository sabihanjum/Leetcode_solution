"""Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether the graph contains any cycle or not. The Graph is represented as an adjacency list, where adj[i] contains all the vertices that are directly connected to vertex i.

NOTE: The adjacency list represents undirected edges, meaning that if there is an edge between vertex i and vertex j, both j will be adj[i] and i will be in adj[j]."""

from typing import List
from collections import deque
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False]*V
        
        def bfs(src):
            q = deque([(src,-1)])
            visited[src]=True
            while q:
                node,parent = q.popleft()
                for i in adj[node]:
                    if not visited[i]:
                        visited[i]=True
                        q.append((i,node))
                    elif i!=parent:
                        return True
            return False
        
        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True
        return False