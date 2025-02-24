"""Given a weighted, undirected and connected graph where you have given adjacency list adj. You have to find the shortest distance of all the vertices from the source vertex src, and return a list of integers denoting the shortest distance between each node and source vertex src.

Note: The Graph doesn't contain any negative weight edge."""

from collections import defaultdict
from heapq import heapify,heappush,heappop
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj, src):
        heap = []
        heapify(heap)
        heappush(heap,[src,0])
        dist = [float('inf')]*len(adj)
        dist[src] = 0
        
        while heap:
            x = heappop(heap)
            node = x[0]
            weight = x[1]
            
            for i in adj[node]:
                newnode = i[0]
                new_weight = i[1]
                
                if new_weight + weight <= dist[newnode]:
                    dist[newnode] = new_weight + weight
                    heappush(heap,[newnode,new_weight + weight])
        return dist