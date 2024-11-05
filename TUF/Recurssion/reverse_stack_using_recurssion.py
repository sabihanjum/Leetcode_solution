"""You are given a stack St. You have to reverse the stack using recursion."""

from typing import List

class Solution:
    def reverse(self, St: List[str]) -> None:  # Adding type hint for clarity
        # Initialize two pointers, i at the beginning and j at the end of the list
        i, j = 0, len(St) - 1

        # Loop until the two pointers meet in the middle
        while i < j:
            # Swap the elements at indices i and j
            St[i], St[j] = St[j], St[i]
            # Move the left pointer to the right
            i += 1
            # Move the right pointer to the left
            j -= 1
