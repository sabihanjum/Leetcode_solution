"""Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.

Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group."""

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        def dfs(i):
            visited[i] = True
            for j in range(len(adj)):
                if adj[i][j] == 1 and not visited[j]:
                    dfs(j)

        provinces = 0
        visited = [False] * len(adj)

        for i in range(len(adj)):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces