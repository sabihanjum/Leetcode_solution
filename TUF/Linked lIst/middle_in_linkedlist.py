"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, both pointing to the head of the linked list
        slow, fast = head, head

        # Move fast by two steps and slow by one step in each iteration
        # When fast reaches the end, slow will be at the middle
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

        # When the loop finishes, slow will be pointing to the middle node
        return slow
