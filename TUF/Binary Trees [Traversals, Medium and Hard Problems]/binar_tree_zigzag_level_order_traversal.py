"""Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between)."""

import collections

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # If the root is None, return an empty list as there are no levels to traverse
        if not root:
            return []

        ans = []  # To store the final zigzag level order traversal
        dq = collections.deque([root])  # A deque to facilitate zigzag traversal
        isLeftToRight = True  # Flag to determine the direction of traversal

        while dq:
            currLevel = []  # To store the nodes' values at the current level
            for _ in range(len(dq)):  # Iterate over all nodes in the current level
                if isLeftToRight:  # If traversing left-to-right
                    node = dq.popleft()  # Remove node from the front of the deque
                    currLevel.append(node.val)  # Add its value to the current level
                    # Add left and right children to the deque if they exist
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                else:  # If traversing right-to-left
                    node = dq.pop()  # Remove node from the back of the deque
                    currLevel.append(node.val)  # Add its value to the current level
                    # Add right and left children to the front of the deque if they exist
                    if node.right:
                        dq.appendleft(node.right)
                    if node.left:
                        dq.appendleft(node.left)
            # Add the current level's values to the result list
            ans.append(currLevel)
            # Toggle the direction for the next level
            isLeftToRight = not isLeftToRight

        return ans
