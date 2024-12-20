"""You are given an array arr of N integers representing a min Heap. The task is to convert it to max Heap.

A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node. """

class Solution:
    def convertMinToMaxHeap(self, N, arr):
        # Start from the last non-leaf node and move upwards to the root
        for i in range(N // 2, -1, -1):
            self.heapify_down(i, arr)
    
    def heapify_down(self, i, arr):
        # Initialize the largest as the root
        large = i
        l = 2 * i + 1  # Index of left child
        r = 2 * i + 2  # Index of right child
        
        # Check if left child exists and is greater than the root
        if l < len(arr) and arr[l] > arr[large]:
            large = l
        
        # Check if right child exists and is greater than the largest so far
        if r < len(arr) and arr[r] > arr[large]:
            large = r
        
        # If the largest is not the root, swap and continue heapifying down
        if large != i:
            arr[large], arr[i] = arr[i], arr[large]
            self.heapify_down(large, arr)
