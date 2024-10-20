"""Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false."""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, both starting at the head of the linked list.
        slow, fast = head, head

        # Traverse the list as long as the fast pointer and fast.next are not None.
        # This ensures that fast can move two steps ahead safely.
        while fast and fast.next:
            # Move the slow pointer one step forward.
            slow = slow.next
            
            # Move the fast pointer two steps forward.
            fast = fast.next.next
            
            # If at any point slow and fast pointers meet, it means there is a cycle in the list.
            if slow == fast:
                return True

        # If the loop terminates, meaning the fast pointer reached the end of the list (None),
        # there's no cycle in the list, so return False.
        return False
