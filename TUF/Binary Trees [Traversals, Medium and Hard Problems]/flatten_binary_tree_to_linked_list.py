"""Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree."""

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
    # Base case: If the root is None, there's nothing to flatten.
        if not root:
            return

        # Recursively flatten the left subtree.
        self.flatten(root.left)
        # Recursively flatten the right subtree.
        self.flatten(root.right)

        # Save the flattened left and right subtrees.
        left = root.left  # This will now be a "linked list" representation of the left subtree.
        right = root.right  # This will now be a "linked list" representation of the right subtree.

        # Attach the flattened left subtree to the right of the current node.
        root.left = None  # Set the left child to None as per problem requirements.
        root.right = left  # Move the flattened left subtree to the right.

        # Traverse to the end of the newly attached right subtree (previously the left subtree).
        rightmost = root
        while rightmost.right:
            rightmost = rightmost.right

        # Attach the original right subtree to the end of the newly attached right subtree.
        rightmost.right = right
