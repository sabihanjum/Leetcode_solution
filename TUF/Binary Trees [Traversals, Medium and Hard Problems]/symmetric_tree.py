"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."""

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        # Helper function to check if two subtrees are symmetric
        def isSymmetric(p: TreeNode | None, q: TreeNode | None) -> bool:
            # If both nodes are None, they are symmetric
            if not p or not q:
                return p == q
            # Check if:
            # 1. The values of the current nodes are equal
            # 2. The left subtree of one tree is symmetric with the right subtree of the other tree
            # 3. The right subtree of one tree is symmetric with the left subtree of the other tree
            return (p.val == q.val and
                    isSymmetric(p.left, q.right) and
                    isSymmetric(p.right, q.left))

        # Start the symmetry check from the root (compare the tree with itself)
        return isSymmetric(root, root)
