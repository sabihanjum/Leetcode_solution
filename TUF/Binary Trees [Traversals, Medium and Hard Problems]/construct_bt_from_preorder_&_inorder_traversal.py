"""Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree."""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: If either preorder or inorder list is empty, return None
        if not preorder or not inorder:
            return None

        # The first element in preorder traversal is the root of the tree
        root = TreeNode(preorder[0])

        # Find the index of the root in the inorder traversal
        # Elements to the left of this index in inorder are in the left subtree
        # Elements to the right of this index in inorder are in the right subtree
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree
        # The next 'mid' elements in preorder correspond to the left subtree
        # The first 'mid' elements in inorder correspond to the left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Recursively build the right subtree
        # The elements after 'mid' in preorder correspond to the right subtree
        # The elements after 'mid' in inorder correspond to the right subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Return the constructed tree
        return root
