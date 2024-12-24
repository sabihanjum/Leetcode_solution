"""Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python)."""
import heapq

class Solution:
    
    def mergeKArrays(self, arr, K):
        """
        Function to merge K sorted arrays into one sorted array.
        :param arr: List of K sorted arrays
        :param K: Number of sorted arrays (and the maximum length of any array)
        :return: A single sorted array containing all elements
        """
        minHeap = []  # Min-heap to store elements with their source array and index
        res = []  # Resultant list to store the merged sorted elements
        
        # Step 1: Initialize the heap with the first element of each array
        for i in range(K):
            if arr[i]:  # Check if the current array is non-empty
                heapq.heappush(minHeap, (arr[i][0], i, 0))  # Push (value, array_index, element_index)
        
        # Step 2: Extract the smallest element from the heap and add the next element from the same array
        while minHeap:
            val, row, col = heapq.heappop(minHeap)  # Pop the smallest element
            res.append(val)  # Add it to the result
            
            # If the current array has more elements, push the next element into the heap
            if col + 1 < len(arr[row]):  # Ensure the index is within bounds for the array
                heapq.heappush(minHeap, (arr[row][col + 1], row, col + 1))
        
        # Step 3: Return the merged sorted array
        return res
