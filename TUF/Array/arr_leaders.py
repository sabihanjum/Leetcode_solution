class Solution:
    # Back-end complete function Template for Python 3
    
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        # Code here
        n = len(arr)  # Get the length of the array
        leaders = []  # Initialize an empty list to store leaders
        max_from_right = arr[-1]  # Start with the last element as the max from the right
        
        # Iterate from the end of the array to the beginning
        for i in range(n-1, -1, -1):
            # If the current element is greater than or equal to max_from_right,
            # it is a leader
            if arr[i] >= max_from_right:
                leaders.append(arr[i])  # Append the leader to the list
                max_from_right = arr[i]  # Update max_from_right to the current element
        
        # Return the leaders in the original order
        return reversed(leaders)  # Since leaders are appended in reverse order, reverse the list
