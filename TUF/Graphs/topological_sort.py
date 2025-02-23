"""Given an adjacency list for a Directed Acyclic Graph (DAG) where adj[u] contains a list of all vertices v such that there exists a directed edge u -> v. Return topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be 1 else 0."""

class Solution:
    def topologicalSort(self,adj):
        v = len(adj)
        
        def dfs(node):
            visit[node]=True
            for nei in adj[node]:
                if not visit[nei]:
                    dfs(nei)
            stack.append(node)
        
        visit = [False]*v
        stack = []
        for i in range(v):
            if not visit[i]:
                dfs(i)
        return stack[::-1] 