"""You are given an array nodes. It contains 7 integers, which represents the value of nodes of the binary tree in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].

Your task to construct a binary tree by creating nodes for the remaining 6 nodes."""

class Node:
    # Constructor to create a new node with given data
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child
        self.right = None  # Right child

class Solution:
    def createTree(self, root, l):
        """
        Creates a binary tree from a given root node and a list of values `l`.
        
        Args:
        root: The root node of the tree.
        l: A list of values to add to the binary tree.

        Returns:
        The root of the updated binary tree.
        """

        # If the root is None, return None
        if not root:
            return None

        # Initialize a queue to perform level-order tree construction
        queue = []

        # If the list is empty, no tree modification is needed
        if not l:
            return root

        # Start by adding the root to the queue
        queue.append(root)

        # Traverse the list of values and build the tree
        for i in range(1, len(l)):
            # Get the current node at the front of the queue
            curr = queue[0]

            # Assign the value to the left child if it doesn't exist
            if curr.left is None:
                curr.left = Node(l[i])
                queue.append(curr.left)
            # Otherwise, assign the value to the right child
            elif curr.right is None:
                curr.right = Node(l[i])
                queue.append(curr.right)

            # If both left and right children are filled, remove the node from the queue
            if curr.left and curr.right:
                queue.pop(0)

        # Return the root of the updated tree
        return root
class Node:
    # Constructor to create a new node with given data
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child
        self.right = None  # Right child

class Solution:
    def createTree(self, nodes):
        """
        Creates a binary tree from a given list of values `nodes`.
        
        Args:
        nodes: A list of values to add to the binary tree.

        Returns:
        The root of the updated binary tree.
        """

        # If the list is empty, return None
        if not nodes:
            return None

        # Create the root node
        root = Node(nodes[0])

        # Initialize a queue to perform level-order tree construction
        queue = [root]

        # Traverse the list of values and build the tree
        i = 1
        while i < len(nodes):
            # Get the current node at the front of the queue
            curr = queue.pop(0)

            # Assign the value to the left child if it doesn't exist
            if i < len(nodes):
                curr.left = Node(nodes[i])
                queue.append(curr.left)
                i += 1

            # Assign the value to the right child if it doesn't exist
            if i < len(nodes):
                curr.right = Node(nodes[i])
                queue.append(curr.right)
                i += 1

        # Return the root of the updated tree
        return root