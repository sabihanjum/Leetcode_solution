"""Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list."""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the head of the list is None
        if not head:
            return None  # No cycle possible in an empty list

        # Initialize two pointers for the Floyd's Cycle Detection algorithm
        slow, fast = head, head
        
        # Loop until fast pointer reaches the end of the list
        while fast and fast.next:  # Ensure fast and fast.next are not None
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next     # Move fast pointer two steps
            
            # Check if the two pointers meet, indicating a cycle
            if fast == slow:
                break  # Cycle detected
        
        # If fast pointer reached the end, there is no cycle
        if not fast or not fast.next:
            return None  # No cycle detected

        # Initialize a second pointer to find the entry point of the cycle
        slow2 = head
        
        # Move both pointers until they meet; this will be the cycle's start
        while slow2 != slow:  # Continue until both pointers meet
            slow = slow.next   # Move slow pointer one step
            slow2 = slow2.next  # Move slow2 pointer one step
        
        return slow  # Return the node where the cycle begins
