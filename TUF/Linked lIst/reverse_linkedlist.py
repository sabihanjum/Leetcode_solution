"""Given the head of a singly linked list, reverse the list, and return the reversed list."""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty (head is None), return None.
        if not head:
            return None

        # Assume newHead will eventually point to the new head of the reversed list.
        newHead = head

        # Recursive case: If there's a next node, reverse the rest of the list.
        if head.next:
            # Recur for the rest of the list and get the new head of the reversed list.
            newHead = self.reverseList(head.next)
            
            # Set the next node's next pointer to point back to the current node.
            head.next.next = head

        # Set the current node's next pointer to None, as it will become the last node.
        head.next = None

        # Return the new head of the reversed list.
        return newHead
