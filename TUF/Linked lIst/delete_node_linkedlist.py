"""There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node
should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Store the reference to the next node in the list
        next = node.next
        
        # Copy the value from the next node to the current node
        # This effectively replaces the current node's value with the next node's value
        node.val = next.val
        
        # Update the current node's next pointer to skip the next node
        # This makes the current node point to the node after the next one
        node.next = next.next
        
        # The next node is now "deleted" from the list as it is no longer referenced
