"""Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present."""


class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # Initialize floor and ceil variables
        floor = -float('inf')  # Floor starts as negative infinity (to find largest <= x)
        ceil = float('inf')    # Ceil starts as positive infinity (to find smallest >= x)
        
        # Traverse through the array
        for i in arr:
            # Check if the current element is smaller or equal to x
            if i <= x:
                # Update floor if the current element is greater than the previous floor
                floor = max(i, floor)
            # Check if the current element is greater or equal to x
            if i >= x:
                # Update ceil if the current element is smaller than the previous ceil
                ceil = min(i, ceil)
        
        # If no valid floor was found, reset floor to -1
        if floor == -float('inf'):
            floor = -1
        # If no valid ceil was found, reset ceil to -1
        if ceil == float('inf'):
            ceil = -1
        
        return [floor, ceil]
