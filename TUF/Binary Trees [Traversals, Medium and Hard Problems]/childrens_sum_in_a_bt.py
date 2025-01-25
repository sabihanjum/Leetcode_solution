"""Given a binary tree having n nodes. Check whether all of its nodes have a value equal to the sum of their child nodes. Return 1 if all the nodes in the tree satisfy the given properties, else it returns 0. For every node, the data value must be equal to the sum of the data values in the left and right children. Consider the data value 0 for a NULL child. Also, leaves are considered to follow the property."""

class Solution:
    # Function to check whether all nodes of a tree have the value 
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # Initialize a stack with the root node.
        stack = [root]
        
        # While there are nodes to process in the stack.
        while stack:
            # Get the number of nodes at the current level.
            n = len(stack)
            
            # Process each node at the current level.
            for _ in range(n):
                count = 0  # Variable to store the sum of child node values.
                node = stack.pop(0)  # Remove the current node from the stack.
                val = node.data  # Store the value of the current node.
                
                # If the current node is a leaf node, continue to the next iteration.
                if not node.left and not node.right:
                    continue
                
                # If the left child exists, add its value to 'count'
                # and push it to the stack for further processing.
                if node.left:
                    count += node.left.data
                    stack.append(node.left)
                
                # If the right child exists, add its value to 'count'
                # and push it to the stack for further processing.
                if node.right:
                    count += node.right.data
                    stack.append(node.right)
                
                # If the value of the current node does not equal the sum of its children, return 0.
                if count != val:
                    return 0
        
        # If all nodes satisfy the property, return 1.
        return 1
