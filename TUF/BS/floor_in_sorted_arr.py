class Solution:
    # User function Template for python3
    
    # Complete this function to find the floor of X in array A
    def findFloor(self, A, N, X):
        # Initialize left and right pointers for binary search
        left, right = 0, N - 1
        
        # Variable to store the index of the floor element
        floor_index = -1
        
        # Binary search loop
        while left <= right:
            # Calculate the mid-point of the current search range
            mid = left + (right - left) // 2
            
            # If the mid element is exactly X, return its index
            if A[mid] == X:
                return mid
            
            # If mid element is less than X, it could be a possible floor
            # Store the index and move to the right to find a larger floor
            elif A[mid] < X:
                floor_index = mid
                left = mid + 1
                
            # If mid element is greater than X, search in the left half
            else:
                right = mid - 1
                
        # Return the index of the floor element
        return floor_index
