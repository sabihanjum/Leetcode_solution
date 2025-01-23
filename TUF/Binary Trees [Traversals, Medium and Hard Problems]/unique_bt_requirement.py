"""Geek wants to know the traversals required to construct a unique binary tree. Given a pair of traversal, return true if it is possible to construct unique binary tree from the given traversals otherwise return false.

Each traversal is represented with an integer: preorder - 1, inorder - 2, postorder - 3.  """

class Solution:
    def isPossible(self, a, b):
        return (a+b)%2