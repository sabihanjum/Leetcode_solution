"""Given an integer n representing number of vertices. Find out how many undirected graphs (not necessarily connected) can be constructed out of a given n number of vertices."""

class Solution:
    def count(self, n):
        # Code here
        k=(n*(n-1))//2
        return 1<<k