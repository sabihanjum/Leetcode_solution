"""Given a Doubly Linked list and a position. The task is to delete a node from a given position (position starts from 1) in a doubly linked list and return the head of the doubly Linked list."""
class Solution:
    def delete_node(self, head, x):
        # If the head is None, the list is empty; return None
        if head is None:
            return

        # If the node to be deleted is the first node
        if x == 1:
            # Set the previous pointer of the next node to None (if it exists)
            if head.next:
                head.next.prev = None
            return head.next  # Return the new head (the second node)

        # Initialize a temporary pointer to traverse the list
        temp = head
        
        # Traverse to the (x-1)th node
        for i in range(1, x):
            if temp is None:
                return head  # If x is out of bounds, return the original list
            temp = temp.next  # Move to the next node

        # If temp is None, it means x was out of bounds, return the original list
        if temp is None:
            return head

        # Adjust pointers to remove the node at position x
        if temp.next:
            temp.next.prev = temp.prev  # Link the next node back to the previous node
        if temp.prev:
            temp.prev.next = temp.next  # Link the previous node forward to the next node

        return head  # Return the head of the modified list
