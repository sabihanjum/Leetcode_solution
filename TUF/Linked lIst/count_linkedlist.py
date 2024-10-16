"""Given a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list."""
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # Initialize the count of nodes to 0
        count = 0
        
        # Set the current node to the head of the linked list
        current = head
        
        # Traverse the linked list until the end (when current becomes None)
        while current:
            # Increment the count for each node
            count += 1
            # Move to the next node in the list
            current = current.next
        
        # Return the total count of nodes in the linked list
        return count
