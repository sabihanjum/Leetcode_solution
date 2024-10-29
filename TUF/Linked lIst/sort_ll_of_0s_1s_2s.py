"""Given a linked list where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 
2s linked list such that all zeros segregate to the head side, 2s at the end of the linked list, and 1s in the 
middle of 0s and 2s."""

class Solution:
    # Function to sort a linked list of 0s, 1s, and 2s.
    def segregate(self, head):
        # If the list is empty or contains only one element, return it as-is.
        if head is None or head.next is None:
            return head
        
        # Create dummy nodes for three separate lists: zeroHead, oneHead, and twoHead.
        zeroHead = Node(-1)  # Dummy head for list of 0s
        oneHead = Node(-1)   # Dummy head for list of 1s
        twoHead = Node(-1)   # Dummy head for list of 2s
        
        # Pointers to the current end of each list (initially pointing to dummy nodes).
        zero = zeroHead
        one = oneHead
        two = twoHead
        
        # Traverse the original list and partition nodes based on their values (0, 1, or 2).
        temp = head
        while temp is not None:
            if temp.data == 0:
                # Attach current node to the end of the 0s list.
                zero.next = temp
                zero = temp
            elif temp.data == 1:
                # Attach current node to the end of the 1s list.
                one.next = temp
                one = temp
            elif temp.data == 2:
                # Attach current node to the end of the 2s list.
                two.next = temp
                two = temp
            # Move to the next node in the original list.
            temp = temp.next    
        
        # Link the three lists together in the order of 0s -> 1s -> 2s.
        # First, link the end of the 0s list to the start of the 1s list (or 2s list if no 1s exist).
        zero.next = oneHead.next if oneHead.next else twoHead.next
        # Link the end of the 1s list to the start of the 2s list.
        one.next = twoHead.next
        # Terminate the 2s list.
        two.next = None
        
        # Set newHead to the start of the 0s list, skipping the dummy node.
        newHead = zeroHead.next
        return newHead
