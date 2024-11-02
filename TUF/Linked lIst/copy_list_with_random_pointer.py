"""A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # If the input list is empty, return None
        if not head:
            return None

        # Dictionary to map original nodes to their copies
        old_to_new = {}

        # First pass: Create a copy of each node and store it in the dictionary
        curr = head
        while curr:
            node = Node(x=curr.val)  # Create a new node with the same value as the current node
            old_to_new[curr] = node  # Map the original node to the copied node
            curr = curr.next

        # Second pass: Assign next and random pointers for each copied node
        curr = head
        while curr:
            new_node = old_to_new[curr]  # Get the copied node for the current node
            new_node.next = old_to_new.get(curr.next)  # Assign the next pointer for the copied node
            new_node.random = old_to_new.get(curr.random)  # Assign the random pointer for the copied node
            curr = curr.next

        # Return the head of the copied list
        return old_to_new[head]
