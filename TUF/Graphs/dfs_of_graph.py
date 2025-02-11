"""Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Traversal (DFS) starting from vertex 0, visiting vertices from left to right as per the adjacency list, and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the adjacency list."""

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        visited=[0]*len(adj)
        output=[]
        stack=[0]
        while stack:
            v=stack.pop()
            if visited[v]==0:
                visited[v]=1
                output.append(v)
                for x in reversed(adj[v]):
                    if visited[x]==0:
                        stack.append(x)
        return output