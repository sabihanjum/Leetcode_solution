"""Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”"""

class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode',
    ) -> 'TreeNode':
        # Base case: if the root is None or matches one of the target nodes (p or q),
        # we return the root as it may be an ancestor.
        if not root or root == p or root == q:
            return root

        # Recursively search for p and q in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Recursively search for p and q in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None, it means p and q are found in
        # different subtrees. Thus, the current root is their lowest common ancestor.
        if left and right:
            return root

        # If one of left or right is not None, return it (either p or q is found,
        # or the lowest common ancestor has already been determined in a subtree).
        return left or right
