"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""
class Solution:
    def searchInsert(self, arr: List[int], x: int) -> int:
        # Get the length of the input array
        n = len(arr)
        
        # Initialize two pointers for binary search: low (start of array) and high (end of array)
        low = 0
        high = n - 1
        
        # Variable to store the position where the element should be inserted or found
        ans = n

        # Perform binary search
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # If the current mid element is greater than or equal to x
            # Set ans to mid and reduce the search space to the left half
            if arr[mid] >= x:
                ans = mid
                high = mid - 1  # Move the 'high' pointer to search the left half

            # If the current mid element is less than x
            # Search in the right half by moving the 'low' pointer
            else:
                low = mid + 1

        # Return the position where the element is found or should be inserted
        return ans


