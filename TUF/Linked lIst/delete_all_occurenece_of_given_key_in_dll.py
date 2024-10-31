"""You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the 
given key if it is present and return the new DLL."""

class Solution:
    # Function to delete all occurrences of a given key `x` from the linked list
    def deleteAllOccurOfX(self, head, x):
        # Initialize head reference and current pointer
        h = head
        c = h
        
        # Traverse the linked list to find and remove nodes with data equal to `x`
        while c:
            # If the current node's data matches `x`, delete this node
            if c.data == x:
                # Set up pointers to previous and next nodes
                p = c.prev
                n = c.next

                # If there is a previous node, link its `next` to the current node's `next`
                if p:
                    p.next = n
                # If there is a next node, link its `prev` to the current node's `prev`
                if n:
                    n.prev = p
                
                # If `c` is the head of the list, update head to the next node
                if c == h:
                    h = n
                
                # Disconnect the current node from the list by clearing its `next` and `prev`
                c.next = None
                c.prev = None
                
                # Move to the next node to continue the traversal
                c = n
            else:
                # If data does not match `x`, proceed to the next node
                c = c.next

        # Return the updated head of the list after deletions
        return h
