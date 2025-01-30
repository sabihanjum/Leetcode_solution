"""You're given a binary tree. Your task is to find the size of the largest subtree within this binary tree that also satisfies the properties of a Binary Search Tree (BST). The size of a subtree is defined as the number of nodes it contains.

Note: A subtree of the binary tree is considered a BST if for every node in that subtree, the left child is less than the node, and the right child is greater than the node, without any duplicate values in the subtree."""

class Solution:
    def largestBst(self, root):
        if not root:
            return 0

        stack = []
        node = root
        last = None
        # Dictionary to store (min, max, size) for each node
        info = {}
        max_bst_size = 0

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                # If right child exists and traversing node from left child, then move right
                if peek.right and last != peek.right:
                    node = peek.right
                else:
                    stack.pop()
                    # Process the node
                    left_info = info.get(peek.left, [float('inf'), float('-inf'), 0])
                    right_info = info.get(peek.right, [float('inf'), float('-inf'), 0])

                    if left_info[1] < peek.data < right_info[0]:
                        current_min = min(left_info[0], peek.data)
                        current_max = max(right_info[1], peek.data)
                        current_size = left_info[2] + right_info[2] + 1
                        info[peek] = [current_min, current_max, current_size]
                        max_bst_size = max(max_bst_size, current_size)
                    else:
                        # Not a BST
                        info[peek] = [float('-inf'), float('inf'), max(left_info[2], right_info[2])]
                    last = peek
        return max_bst_size