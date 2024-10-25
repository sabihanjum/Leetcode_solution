"""Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0."""

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        # Set up two pointers, first and second, both starting at the head.
        first = head
        second = head
        
        # Traverse the linked list using the two pointers.
        # 'first' moves two steps at a time, 'second' moves one step at a time.
        while first is not None and first.next is not None:
            second = second.next
            first = first.next.next
            
            # If 'first' and 'second' meet, there is a loop in the list.
            if first == second:
                # Initialize size counter to count the nodes in the loop.
                size = 1
                curr = second.next
                
                # Traverse the loop until we return to the starting node.
                while curr != second:
                    size += 1
                    curr = curr.next
                
                # Return the length of the loop.
                return size
        
        # If no loop is detected, return 0.
        return 0
