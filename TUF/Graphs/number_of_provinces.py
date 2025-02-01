"""There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces."""

class UnionFind:
    def __init__(self, n: int):
        """
        Initializes the Union-Find (Disjoint Set) data structure.
        
        Parameters:
        - n (int): Number of elements (nodes) in the set.
        
        Attributes:
        - count: Keeps track of the number of disjoint sets.
        - id: Stores the parent of each node, initially pointing to itself.
        - rank: Used to optimize union operations (prevents tree from growing too tall).
        """
        self.count = n  # Initially, each node is its own component
        self.id = list(range(n))  # Parent pointers for each node
        self.rank = [0] * n  # Rank (tree height) for each node

    def unionByRank(self, u: int, v: int) -> None:
        """
        Merges the sets containing u and v using union by rank.
        
        Parameters:
        - u (int): First node.
        - v (int): Second node.
        """
        # Find root representatives of both nodes
        i = self._find(u)
        j = self._find(v)
        
        # If they already belong to the same set, return
        if i == j:
            return

        # Merge the smaller tree into the larger tree
        if self.rank[i] < self.rank[j]:
            self.id[i] = j  # Attach tree with lower rank to higher rank tree
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
        else:
            self.id[i] = j  # Merge and increase the rank
            self.rank[j] += 1

        # Reduce the number of disjoint sets
        self.count -= 1

    def _find(self, u: int) -> int:
        """
        Finds the representative (root) of the set containing u.
        Implements path compression to flatten the tree structure for efficiency.
        
        Parameters:
        - u (int): The node whose representative is to be found.
        
        Returns:
        - int: The representative (root) of the set containing u.
        """
        if self.id[u] != u:
            self.id[u] = self._find(self.id[u])  # Path compression
        return self.id[u]


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        Finds the number of provinces (connected components) in a graph represented by an adjacency matrix.
        
        Parameters:
        - isConnected (list[list[int]]): A square matrix representing direct connections between nodes.
        
        Returns:
        - int: The number of provinces (disjoint connected components).
        """
        n = len(isConnected)
        uf = UnionFind(n)  # Initialize Union-Find data structure

        # Iterate over the upper triangle of the matrix (to avoid duplicate edges)
        for i in range(n):
            for j in range(i + 1, n):  # Start from i+1 to avoid self-loops
                if isConnected[i][j] == 1:
                    uf.unionByRank(i, j)  # Merge connected components

        return uf.count  # The remaining disjoint sets represent the number of provinces
