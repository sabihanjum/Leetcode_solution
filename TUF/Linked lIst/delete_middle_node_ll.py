"""You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively."""

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a temporary node pointing to the head to handle edge cases
        temp = ListNode(next=head)
        
        # Initialize two pointers, p1 and p2, both starting at the temp node
        p1 = p2 = temp
        
        # Use the two-pointer technique to find the middle of the linked list
        # p1 moves one step at a time, p2 moves two steps
        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next          # p1 moves one step
            p2 = p2.next.next     # p2 moves two steps
        
        # p1 now points to the node before the middle node, so skip the middle node
        p1.next = p1.next.next
        
        # Return the updated list, skipping the temporary head node
        return temp.next
