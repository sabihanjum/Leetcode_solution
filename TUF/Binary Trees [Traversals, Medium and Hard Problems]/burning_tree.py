"""Given a binary tree and a node data called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.
Note: The tree contains unique values."""

class Solution:
    def ans(self, ptr, target, maxtime):
        """
        Helper function to compute the minimum time required to burn all nodes in the binary tree,
        starting from the target node.

        :param ptr: Current node being processed.
        :param target: The value of the target node where burning starts.
        :param maxtime: A list containing the maximum time required to burn the tree.
        :return: An integer indicating the distance of the current node from the target,
        or 0 if the node is not part of the burning process.
        """
        # Base case: If the current node is None, return 0.
        if ptr is None:
            return 0

        # Recursively compute distances for the left and right subtrees.
        val_1 = self.ans(ptr.left, target, maxtime)
        val_2 = self.ans(ptr.right, target, maxtime)

        # If the current node is the target node.
        if ptr.data == target:
            # Update the maximum time based on the maximum depth of the left and right subtrees.
            maxtime[0] = max(maxtime[0], max(val_1, val_2))
            # Return -1 to indicate that the current node is the target.
            return -1

        # If the target is not in the subtree rooted at the current node.
        if val_1 >= 0 and val_2 >= 0:
            # Return the maximum depth of the subtrees + 1.
            return max(val_1, val_2) + 1

        # Ensure that `val_2` is the larger of the two values (distance to target).
        if val_1 > val_2:
            val_1, val_2 = val_2, val_1

        # Update the maximum time considering the distance between the left and right subtrees.
        maxtime[0] = max(maxtime[0], val_2 - val_1)
        # Return the distance of the current node from the target node.
        return val_1 - 1

    def minTime(self, root, target):
        """
        Calculates the minimum time required to burn all nodes of a binary tree starting from the target node.

        :param root: The root of the binary tree.
        :param target: The value of the target node where the fire starts.
        :return: An integer representing the time required to burn the entire tree.
        """
        maxtime = [0]  # Using a list to allow the helper function to update its value.
        self.ans(root, target, maxtime)
        return maxtime[0]
