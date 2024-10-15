"""Given an array of integer arr. Your task is to construct the linked list from arr & return the head of the linked list."""

class Node:
    def __init__(self, data):
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node (initially None)

class Solution:
    def constructLL(self, arr):
        # Initialize the head of the linked list with the first element of the array
        head = Node(arr[0])
        
        # Store the original head reference to return later
        original_head = head
        
        # Iterate through the array starting from the second element
        for i in arr[1:]:
            # Create a new node for the current element
            head.next = Node(i)
            
            # Move the head to the next node (newly created one)
            head = head.next
        
        # Return the original head of the linked list
        return original_head


