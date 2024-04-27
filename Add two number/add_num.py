# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if not l1:
                return l2
            if not l2:
                return l1

            head = l1
            prev = l1
            carry = 0
            while l1 or l2:          #l1 is none and l2 is not none
                
                #add the value of current node and carry
                sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
                carry = sum_//10   #update the carry
                sum_ = sum_%10     #get the last digit
                if l1:             #if l1 exist then move to next
                    l1.val = sum_  #set the new value
                    prev = l1      #move to next one
                    l1 = l1.next
                else:
                    newNode = ListNode(sum_, None)  #create a new node with the left number's remaining part
                    prev.next = newNode             #connect it to previous one
                    prev = prev.next                #move to next one

                if l2:
                    l2 = l2.next

            if carry == 1:          #if there are still some numbers need to be added
                newNode = ListNode(carry, None)   #create a new node with carry
                prev.next = newNode               #connect it to previous one
                prev = prev.next                  #move to next one

            return head             #return the linkedlist which store the result