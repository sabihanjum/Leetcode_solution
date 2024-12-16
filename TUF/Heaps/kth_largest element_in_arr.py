"""Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?"""
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Create a min-heap of size k with the first k elements of nums
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # Turn the list into a heap
        
        # Iterate through the remaining elements in nums
        for num in nums[k:]:
            # If the current number is larger than the smallest element in the heap
            if num > min_heap[0]:
                # Replace the smallest element with the current number
                heapq.heapreplace(min_heap, num)
        
        # The root of the heap (min_heap[0]) is the kth largest element
        return min_heap[0]