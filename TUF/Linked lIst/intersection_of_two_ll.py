"""Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize two pointers, one for each list
        l1, l2 = headA, headB
        
        # Traverse the lists until the two pointers meet
        while l1 != l2:
            # Move to the next node in list A, or switch to list B if at the end of list A
            l1 = l1.next if l1 else headB
            # Move to the next node in list B, or switch to list A if at the end of list B
            l2 = l2.next if l2 else headA
        
        # If l1 and l2 meet, it will be at the intersection node; otherwise, both will be None
        return l1
