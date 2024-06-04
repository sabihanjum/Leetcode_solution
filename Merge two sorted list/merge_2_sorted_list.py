class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        curr = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next            
            curr = curr.next

        if l1 is not None:
            curr.next = l1
        else:
            curr.next = l2

        return prehead.next