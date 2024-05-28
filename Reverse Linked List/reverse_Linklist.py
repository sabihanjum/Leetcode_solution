# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty, return None
        if not head:
            return None

        # Initialize the new head as the current head
        newHead = head
        
        # If there is a next node, proceed to reverse the rest of the list
        if head.next:
            # Recursively reverse the rest of the list starting from the next node
            newHead = self.reverseList(head.next)
            # Set the next node's next pointer to the current head to reverse the link
            head.next.next = head
        
        # Set the current node's next pointer to None to complete the reversal for this node
        head.next = None
        
        # Return the new head of the reversed list
        return newHead
