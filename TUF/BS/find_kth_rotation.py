"""Given an increasing sorted rotated array arr of distinct integers. The array is right-rotated k times. Find the value of k.
Let's suppose we have an array arr = [2, 4, 6, 9], so if we rotate it by 2 times so that it will look like this:
After 1st Rotation : [9, 2, 4, 6]
After 2nd Rotation : [6, 9, 2, 4]"""

class Solution:
    def findKRotation(self, arr):
        # Initialize low and high pointers for binary search
        low = 0
        high = len(arr) - 1
        
        # 'ans' will store the minimum value, initialized to infinity
        # 'index' will store the index of the minimum value (rotation count)
        ans = float('inf')
        index = -1
        
        # Perform binary search while low is less than or equal to high
        while low <= high:
            # Calculate the mid index
            mid = (low + high) // 2
            
            # Case 1: If the subarray is already sorted (arr[low] <= arr[high])
            if arr[low] <= arr[high]:
                # If the element at 'low' is smaller than the current minimum 'ans'
                if arr[low] < ans:
                    # Update 'index' with 'low' and 'ans' with the value at 'low'
                    index = low
                    ans = arr[low]
                break  # Break as the array is sorted
            
            # Case 2: If the left half is sorted (arr[low] <= arr[mid])
            if arr[low] <= arr[mid]:
                # Check if the element at 'low' is smaller than the current minimum 'ans'
                if arr[low] < ans:
                    # Update 'index' with 'low' and 'ans' with the value at 'low'
                    index = low
                    ans = arr[low]
                # Move to the right half by updating 'low' to mid + 1
                low = mid + 1
            # Case 3: If the right half is sorted (arr[mid] <= arr[high])
            else:
                # Check if the element at 'mid' is smaller than the current minimum 'ans'
                if arr[mid] < ans:
                    # Update 'index' with 'mid' and 'ans' with the value at 'mid'
                    index = mid
                    ans = arr[mid]
                # Move to the left half by updating 'high' to mid - 1
                high = mid - 1
        
        # Return the index of the minimum element (rotation count)
        return index
