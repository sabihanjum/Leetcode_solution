"""Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the 
linked list."""

class Solution:
    # Helper function to delete a node from a doubly linked list
    def delete(self, curr):
        # Set the previous node's next pointer to skip over 'curr'
        curr.prev.next = curr.next
        # If 'curr' is not the last node, update the next node's prev pointer
        if curr.next is not None:
            curr.next.prev = curr.prev

    # Function to remove duplicates from an unsorted doubly linked list
    def removeDuplicates(self, head):
        # If the list has only one node, no duplicates are possible; return the head
        if head.next is None:
            return head
        
        # Start from the second node, as we are comparing with the previous node
        curr = head.next
        
        # Traverse through the list
        while curr:
            # If the current node's data matches the previous node's data, it's a duplicate
            if curr.prev.data == curr.data:
                self.delete(curr)  # Call the delete function to remove the duplicate node
            # Move to the next node in the list
            curr = curr.next
        
        # Return the head of the modified list
        return head
