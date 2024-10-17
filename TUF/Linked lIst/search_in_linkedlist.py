"""Given a linked list of n nodes and a key , the task is to check if the key is present in the linked list or not."""

class Solution:
    def searchKey(self, n, head, key):
        # Initialize traversal of the linked list starting from the head
        while head is not None:
            # Check if the current node's data matches the key
            if head.data == key:
                # If found, return True
                return True
            # Move to the next node in the list
            head = head.next
        
        # If the key is not found after traversing the entire list, return False
        return False
