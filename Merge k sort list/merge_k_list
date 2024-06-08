# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If the input list is empty or None, return None
        if not lists or len(lists) == 0:
            return None

        # Continue merging lists until only one list remains
        while len(lists) > 1:
            mergeLists = []

            # Iterate through the lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the pairs and add the merged list to mergeLists
                mergeLists.append(self.mergeTwoLists(l1, l2))
            # Update lists to be the newly merged lists
            lists = mergeLists
        
        # Return the final merged list
        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode(0)
        tail = dummy

        # While neither list is empty, compare the heads and append the smaller one
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # If there are remaining elements in l1 or l2, append them
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        # Return the merged list, starting from the node after the dummy
        return dummy.next
