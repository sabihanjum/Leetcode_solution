"""Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer."""

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        queue = deque([(root, 0)])
        max_width = 0
        while queue:
            level_length = len(queue)
            _, level_start = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right, 2*index+1))    
            max_width = max(max_width, index - level_start + 1)
        return max_width