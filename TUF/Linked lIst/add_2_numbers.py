"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in 
reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

class Solution(object):
    # Recursive function to add two numbers represented by linked lists
    def addTwoNumbers(self, l1, l2, carry=0):
        # Base case: if both lists are empty and there's no carry, return None
        if not l1 and not l2 and not carry:
            return None

        # Initialize sum with the carry value from the previous nodes (if any)
        sum = carry
        # Add the value of l1 to sum if l1 exists
        if l1:
            sum += l1.val
            l1 = l1.next  # Move to the next node in l1
        # Add the value of l2 to sum if l2 exists
        if l2:
            sum += l2.val
            l2 = l2.next  # Move to the next node in l2

        # Create a new node with the last digit of sum (sum % 10)
        result = ListNode(sum % 10)
        # Recursively calculate the next node with the new carry (sum // 10)
        result.next = self.addTwoNumbers(l1, l2, sum // 10)
        
        return result
