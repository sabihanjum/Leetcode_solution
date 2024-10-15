"""Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.
"""

class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # Create a new node with the given value x
        temp = Node(x)
        
        # If the head is None, it means the list is empty
        if head is None:
            head = temp  # Set the head to the new node
            return head  # Return the new head of the list
        else:
            curr = head  # Start with the head of the list
            
            # Traverse to the end of the linked list
            while curr.next is not None:
                curr = curr.next  # Move to the next node
            
            # Link the new node at the end of the list
            curr.next = temp
        
        return head  # Return the head of the modified list
