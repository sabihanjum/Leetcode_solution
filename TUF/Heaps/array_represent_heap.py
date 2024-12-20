"""Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap."""

import heapq

class Solution:
    def isMaxHeap(self, arr, n):
        # Create a max-heap by inverting the sign of all elements in the array
        max_heap = [-x for x in arr]
        
        # Transform the list into a heap (in-place) - heapify turns the list into a heap
        heapq.heapify(max_heap)
        
        # Invert the signs back to get the original elements after heap operations
        ans = [-x for x in max_heap]
        
        # Check if the given array matches the array obtained from the max-heap
        return arr == ans
