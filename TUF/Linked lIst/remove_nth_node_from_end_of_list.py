"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        # Move `ahead` n+1 steps ahead, to maintain the correct gap
        for _ in range(n + 1):
            ahead = ahead.next

        # Move both `ahead` and `behind` one step at a time until `ahead` reaches the end
        while ahead:
            behind = behind.next  # Fixed the typo here
            ahead = ahead.next

        # Skip the node that needs to be removed
        behind.next = behind.next.next

        # Return the updated linked list, skipping the dummy node
        return dummy.next
