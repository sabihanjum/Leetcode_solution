"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))."""

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        med1 = med2 = i = j = 0  # Initialize medians and array pointers
        n = len(A) + len(B)  # Total number of elements in both arrays combined
        
        # Loop until we reach the middle of the combined arrays
        while (i + j) <= n / 2:
            if i < len(A) and j < len(B):  # If both arrays have elements left
                med2 = med1  # Store the previous median value in med2
                if A[i] < B[j]:  # If current element of A is smaller than B
                    med1 = A[i]  # Set the current median to A[i]
                    i += 1  # Move to the next element in A
                else:  # Otherwise, B[j] is smaller or equal
                    med1 = B[j]  # Set the current median to B[j]
                    j += 1  # Move to the next element in B
            elif i < len(A):  # If B is exhausted but A still has elements
                med2 = med1  # Store previous median
                med1 = A[i]  # Set median to current element in A
                i += 1  # Move to the next element in A
            elif j < len(B):  # If A is exhausted but B still has elements
                med2 = med1  # Store previous median
                med1 = B[j]  # Set median to current element in B
                j += 1  # Move to the next element in B

        # If the total number of elements is even, return the average of med1 and med2
        if n % 2 == 0:
            return (med1 + med2) / 2.0
        else:  # If odd, return med1
            return med1
