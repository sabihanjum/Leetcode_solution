class Solution:
    def sortColors(self, arr):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers
        low = 0          # Pointer for the next position of '0'
        mid = 0          # Pointer for the current element being examined
        high = len(arr) - 1  # Pointer for the next position of '2'

        # Process elements in the array until mid passes high
        while mid <= high:
            if arr[mid] == 0:
                # If the current element is 0, swap it with the element at the low pointer
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1    # Move the low pointer to the right
                mid += 1    # Move the mid pointer to the right
            elif arr[mid] == 1:
                # If the current element is 1, just move the mid pointer to the right
                mid += 1
            else:
                # If the current element is 2, swap it with the element at the high pointer
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1   # Move the high pointer to the left
