"""Geek is learning data structures and is familiar with linked lists, but he's curious about how to access the previous element in a linked list in the same way that we access the next element. His teacher explains doubly linked lists to him.

Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it.

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in the node
        self.data = data         # Initialize the node's data
        self.next = None         # Initialize the next pointer to None
        self.prev = None         # Initialize the previous pointer to None"""

class Solution:
    def constructDLL(self, arr):
        # Code here to construct a doubly linked list from an array
        if not arr:                # Check if the input array is empty
            return None            # Return None if the array is empty
        
        # Create the head of the doubly linked list with the first element of the array
        head = Node(arr[0])        # Create a new node with the first array element
        head.prev = None           # The head node's previous pointer is None
        nn = head                  # Initialize a temporary node 'nn' pointing to the head
        
        # Loop through the remaining elements in the array
        for i in range(1, len(arr)):
            # Create a new node for each element in the array
            nn.next = Node(arr[i])  # Set the next pointer of the current node to a new node
            nn.next.prev = nn       # Set the previous pointer of the new node to the current node
            nn = nn.next            # Move the temporary node 'nn' to the new node
        
        return head                 # Return the head of the constructed doubly linked list
