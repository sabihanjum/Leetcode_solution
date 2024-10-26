"""Given the head of a linked list, return the list after sorting it in ascending order"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split the list into two halves
        mid = self.getMid(head)
        right = mid.next
        mid.next = None  # End the left half here

        # Recursive sorting on each half
        left = self.sortList(head)
        right = self.sortList(right)

        # Merge the sorted halves
        return self.merge(left, right)

    def getMid(self, head):
        # Find the middle of the linked list using the slow-fast pointer technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        # Merge two sorted linked lists
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach any remaining elements
        tail.next = list1 if list1 else list2

        return dummy.next
