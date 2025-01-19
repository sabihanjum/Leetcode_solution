"""Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree."""

class Solution:
    def buildTree(
        self,
        inorder: list[int],        # The inorder traversal of the tree
        postorder: list[int],      # The postorder traversal of the tree
    ) -> TreeNode | None:
        # Create a mapping from value to its index in the inorder traversal for quick lookup
        inToIndex = {num: i for i, num in enumerate(inorder)}

        def build(
            inStart: int,          # Start index in the inorder list
            inEnd: int,            # End index in the inorder list
            postStart: int,        # Start index in the postorder list
            postEnd: int,          # End index in the postorder list
        ) -> TreeNode | None:
            # Base case: if the start index is greater than the end index, return None
            if inStart > inEnd:
                return None

            # The root value is the last element in the current postorder segment
            rootVal = postorder[postEnd]
            # Find the index of the root value in the inorder list
            rootInIndex = inToIndex[rootVal]
            # Calculate the size of the left subtree
            leftSize = rootInIndex - inStart

            # Create the root node
            root = TreeNode(rootVal)
            # Recursively build the left subtree
            root.left = build(inStart, rootInIndex - 1, postStart, postStart + leftSize - 1)
            # Recursively build the right subtree
            root.right = build(rootInIndex + 1, inEnd, postStart + leftSize, postEnd - 1)
            return root

        # Call the helper function with the full range of inorder and postorder lists
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
