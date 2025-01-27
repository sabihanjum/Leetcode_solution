"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”"""

class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two nodes, p and q, in a Binary Search Tree (BST).

        The LCA of two nodes in a BST is defined as the deepest node that is an ancestor
        of both p and q. 

        Args:
        root (TreeNode): The root node of the BST.
        p (TreeNode): The first target node.
        q (TreeNode): The second target node.

        Returns:
        TreeNode: The lowest common ancestor of p and q.
        """
        # If both p and q are smaller than root, their LCA lies in the left subtree.
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both p and q are greater than root, their LCA lies in the right subtree.
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If neither of the above conditions is true, root is the LCA.
        # This happens when p and q lie on different sides of root or one of them is root.
        return root
