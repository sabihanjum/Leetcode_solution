"""Given the head of a singly linked list, return true if it is a palindromeor false otherwise."""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # Find the middle of the linked list using two pointers (fast and slow).
        # 'fast' moves two steps at a time while 'slow' moves one step at a time.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the list starting from the middle (slow pointer).
        prev = None
        while slow:
            # Temporarily store the next node.
            tmp = slow.next
            # Reverse the pointer of the current node to point to the previous node.
            slow.next = prev
            # Move 'prev' and 'slow' one step forward.
            prev = slow
            slow = tmp

        # Compare the first half (starting from head) with the reversed second half (prev).
        left, right = head, prev
        while right:
            # If values are not the same, it's not a palindrome.
            if left.val != right.val:
                return False
            # Move both pointers forward to compare the next values.
            left = left.next
            right = right.next

        # If all values matched, it's a palindrome.
        return True
