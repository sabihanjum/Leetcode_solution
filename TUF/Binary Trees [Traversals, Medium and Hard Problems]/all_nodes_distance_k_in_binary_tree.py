"""Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order."""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Find all nodes at distance K from the target node in a binary tree.
        """

        # Helper function to map parent pointers for each node
        def map_parents(node, parent):
            """
            Traverse the tree and store parent pointers for each node.
            Args:
                node: Current node in the tree.
                parent: Parent of the current node.
            """
            if node:
                parent_map[node] = parent  # Map the current node to its parent
                map_parents(node.left, node)  # Recursively map the left child
                map_parents(node.right, node)  # Recursively map the right child

        # Helper function to perform DFS and find nodes at a distance K
        def find_nodes_at_distance_k(node, remaining_distance):
            """
            Perform DFS to find all nodes at the given distance.
            Args:
                node: Current node in the DFS traversal.
                remaining_distance: Distance remaining to reach K.
            """
            if not node or node.val in visited:
                return  # Stop if node is None or already visited
            visited.add(node.val)  # Mark the current node as visited
            if remaining_distance == 0:
                # If the distance is 0, add the node's value to the result
                result.append(node.val)
            else:
                # Continue exploring the children and the parent node
                find_nodes_at_distance_k(node.left, remaining_distance - 1)
                find_nodes_at_distance_k(node.right, remaining_distance - 1)
                find_nodes_at_distance_k(parent_map[node], remaining_distance - 1)

        # Initialize the parent map and result list
        parent_map = {}  # To store the parent pointers of each node
        result = []  # To store the result nodes at distance K
        visited = set()  # To avoid revisiting nodes

        # Map parents for all nodes in the tree
        map_parents(root, None)

        # Start DFS from the target node
        find_nodes_at_distance_k(target, k)

        # Return the list of nodes at distance K
        return result
