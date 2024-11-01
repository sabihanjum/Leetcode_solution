"""Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target."""

class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        # Initialize tail to point to the last node in the doubly linked list
        tail = head
        while tail.next:  # Traverse to the end of the list to find the tail
            tail = tail.next

        # Initialize an empty list to store the result pairs
        res = []
        # Set two pointers: one starting from the head, and the other from the tail
        start, end = head, tail

        # Use a two-pointer approach to find pairs with the given sum
        while start != end and end.next != start:
            # Calculate the current sum of the two pointer nodes
            current_sum = start.data + end.data
            
            # If the current sum matches the target, add the pair to the result list
            if current_sum == target:
                res.append([start.data, end.data])
                # Move the start pointer forward and the end pointer backward
                start = start.next
                end = end.prev
            # If the current sum is greater than the target, move the end pointer backward
            elif current_sum > target:
                end = end.prev
            # If the current sum is less than the target, move the start pointer forward
            else:
                start = start.next

        # Return the list of pairs that sum up to the target
        return res
