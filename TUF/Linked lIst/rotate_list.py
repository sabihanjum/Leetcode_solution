"""Given the head of a linked list, rotate the list to the right by k places."""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If the head is None, there is nothing to rotate, so return None
        if not head:
            return head

        # Step 1: Calculate the length of the linked list and get the tail
        length, tail = 1, head
        while tail.next:  # Traverse to the end of the list
            tail = tail.next
            length += 1  # Increment length for each node

        # Step 2: Find the effective rotation count
        k = k % length  # Normalize k to avoid unnecessary rotations
        if k == 0:  # If k is 0, no rotation is needed
            return head

        # Step 3: Move to the pivot point for rotation
        cur = head
        for i in range(length - k - 1):  # Find the node before the new head
            cur = cur.next
        
        # Step 4: Perform the rotation
        newHead = cur.next  # The new head is the next node
        cur.next = None  # Break the link to the new head
        tail.next = head  # Connect the old tail to the old head
        return newHead  # Return the new head of the rotated list
