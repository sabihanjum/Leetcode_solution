"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed."""

class Solution:
    # Function to reverse nodes in groups of k
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases and ease reversal connections
        dummy = ListNode(0, head)
        groupPrev = dummy  # This marks the end of the previous reversed group

        # Loop to reverse nodes in k-group until the end of the list is reached
        while True:
            # Find the kth node from the current group starting point
            kth = self.getKth(groupPrev, k)
            if not kth:  # If less than k nodes remain, no more reversal
                break
            groupNext = kth.next  # The node after the kth node for linkage

            # Initialize pointers to reverse the current k-group
            prev, curr = kth.next, groupPrev.next  # prev is set to groupNext

            # Reverse the k-group
            while curr != groupNext:
                tmp = curr.next  # Store next node
                curr.next = prev  # Reverse current node's pointer
                prev = curr  # Move prev to current node
                curr = tmp  # Move to next node in the group
            
            # After reversing, connect the previous group with the new start of the group
            tmp = groupPrev.next  # Temporary marker to reassign groupPrev later
            groupPrev.next = kth  # Connect previous group end to kth (new group head)
            groupPrev = tmp  # Update groupPrev to the end of the newly reversed group

        # Return the new head of the list (dummy.next points to the head of the first reversed group)
        return dummy.next

    # Helper function to find the kth node from the current node
    def getKth(self, curr, k):
        # Traverse k nodes ahead, or until the end of the list
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr  # Returns the kth node or None if there are fewer than k nodes left
