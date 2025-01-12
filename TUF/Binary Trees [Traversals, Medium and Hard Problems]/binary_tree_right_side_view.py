"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom."""

import collections

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # If the root is None, return an empty list as there is no tree to traverse
        if not root:
            return []

        ans = []  # List to store the right side view of the tree
        q = collections.deque([root])  # Queue for level-order traversal (BFS)

        while q:
            size = len(q)  # Number of nodes in the current level
            for i in range(size):  # Iterate through all nodes at this level
                root = q.popleft()  # Get the next node in the queue
                # If this is the last node of the current level, add its value to the result
                if i == size - 1:
                    ans.append(root.val)
                # Add the left child to the queue if it exists
                if root.left:
                    q.append(root.left)
                # Add the right child to the queue if it exists
                if root.right:
                    q.append(root.right)

        return ans  # Return the list of values visible from the right side
