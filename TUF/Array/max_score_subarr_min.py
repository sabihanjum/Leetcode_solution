"""Given an array arr[], with 0-based indexing, select any two indexes, i and j such that i < j.
From the subarray arr[i...j], select the smallest and second smallest numbers and add them, you 
will get the score for that subarray. Return the maximum possible score across all the subarrays of array arr[]."""

class Solution:
    def pairWithMaxSum(self, arr):
        # Your code goes here
        s=0
        m=-1
        for i in range(len(arr)-1):
            s=arr[i]+arr[i+1]
            if s>m:
                m=s
        return m
    