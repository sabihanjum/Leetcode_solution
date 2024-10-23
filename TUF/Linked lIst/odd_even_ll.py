"""Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity."""

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, return the head as is
        if not head or not head.next:
            return head

        # Initialize pointers for odd and even indexed nodes
        oddptr = current = head          # Pointer for the last odd node
        evenptr = evenhead = head.next  # Pointer for the first even node

        i = 1  # Initialize index counter
        while current:
            # For odd indexed nodes (starting from the third node)
            if i > 2 and i % 2 != 0:
                oddptr.next = current  # Link current odd node
                oddptr = oddptr.next    # Move odd pointer forward
            # For even indexed nodes (starting from the third node)
            elif i > 2 and i % 2 == 0:
                evenptr.next = current  # Link current even node
                evenptr = evenptr.next    # Move even pointer forward
            
            current = current.next  # Move to the next node in the original list
            i += 1  # Increment the index

        # Terminate the even list
        evenptr.next = None
        # Connect the end of the odd list to the head of the even list
        oddptr.next = evenhead

        # Return the modified list starting from the head
        return head
