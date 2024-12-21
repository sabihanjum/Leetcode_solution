"""Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function."""

import heapq

class Solution:
    def kthSmallest(self, arr, k):
        """
        Find the k-th smallest element using a min-heap.
        
        :param arr: List[int], the input array
        :param k: int, the k-th position to find (1-based index)
        :return: int, the k-th smallest element
        """
        # Create a min-heap from the array
        heapq.heapify(arr)
        
        # Extract the smallest element k times
        for _ in range(k):
            result = heapq.heappop(arr)
        
        return result
