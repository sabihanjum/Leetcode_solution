"""Given a doubly linked list. Your task is to reverse the doubly linked list and return its head."""

class Solution:
    def reverseDLL(self, head):
        # Return head of reversed doubly linked list
        
        # Check if the head is None (empty list), return None if so
        if head is None:
            return None
        
        # Initialize the 'current' pointer to the head of the list
        current = head
        
        # Traverse to the end of the list (the last node)
        while current.next is not None:
            current = current.next
        
        # 'current' now points to the last node of the list
        # We'll collect the data in reverse order
        output = []  # List to store the values in reverse
        
        # Traverse backward using the 'prev' pointers
        while current is not None:
            output.append(current.data)  # Add current node's data to the list
            current = current.prev  # Move to the previous node
        
        # Print the reversed data as a space-separated string
        print(" ".join(map(str, output)))
