"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it."""

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # Continue merging until only one list remains
        while len(lists) > 1:
            mergedLists = []

            # Merge lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # Corrected from "list[i]" to "lists[i]"
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))  # Merge two lists

            # Replace the old list with the newly merged lists
            lists = mergedLists

        # Return the final merged list
        return lists[0]

    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify list merging
        tail = dummy  # Tail pointer to build the merged list

        # Merge the two lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach the remaining nodes, if any
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the head of the merged list
        return dummy.next
