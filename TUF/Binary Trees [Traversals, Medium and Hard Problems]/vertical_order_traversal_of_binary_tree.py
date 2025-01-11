"""Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree."""

import collections

class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        ans = []  # To store the final vertical order traversal
        xToNodes = collections.defaultdict(list)  # Dictionary to group nodes by their x-coordinates

        # Depth-first search (DFS) function to traverse the tree
        def dfs(node: TreeNode | None, x: int, y: int) -> None:
            if not node:  # Base case: If the node is None, return
                return
            # Append a tuple (-y, node.val) to the list for the current x-coordinate
            # -y ensures that nodes at the same x-coordinate are sorted by their y-coordinate (descending order)
            xToNodes[x].append((-y, node.val))
            # Recur for the left child with x-1 and y-1
            dfs(node.left, x - 1, y - 1)
            # Recur for the right child with x+1 and y-1
            dfs(node.right, x + 1, y - 1)

        # Start the DFS traversal from the root node at position (0, 0)
        dfs(root, 0, 0)

        # Process the nodes grouped by x-coordinates
        for _, nodes in sorted(xToNodes.items(), key=lambda x: x[0]):  # Sort by x-coordinates
            # Sort nodes for the current x-coordinate by y (descending) and then by value (ascending)
            ans.append([val for _, val in sorted(nodes)])

        return ans
