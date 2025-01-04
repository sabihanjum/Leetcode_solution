"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)."""

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize the result list to store each level's values
        ans = []
        
        # Use a queue to facilitate level order traversal
        # Start with the root node in the queue
        q = collections.deque([root])

        # Process nodes level by level
        while q:
            # Temporary list to store values of the current level
            currLevel = []
            
            # Iterate through all nodes at the current level
            for _ in range(len(q)):
                # Dequeue the front node
                node = q.popleft()
                
                # Add its value to the current level's list
                currLevel.append(node.val)
                
                # Enqueue the left child if it exists
                if node.left:
                    q.append(node.left)
                
                # Enqueue the right child if it exists
                if node.right:
                    q.append(node.right)
            
            # Add the current level's values to the result
            ans.append(currLevel)

        # Return the result containing values level by level
        return ans
