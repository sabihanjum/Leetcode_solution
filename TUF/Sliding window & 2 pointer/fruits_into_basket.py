"""You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array of arr[], where arr[i]  is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow :

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of the baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array of fruits, return the maximum number of fruits you can pick."""

class Solution:
    def totalFruits(self, arr):
        # Get the length of the array
        n = len(arr)
        
        # Initialize variables to keep track of the maximum number of fruits
        maxi = 0
        
        # Dictionary to store the count of each type of fruit in the current window
        m = {}
        
        # Initialize two pointers for the sliding window
        l = 0  # Left pointer
        r = 0  # Right pointer

        # Iterate through the array with the right pointer
        while r < n:
            # Add the current fruit to the dictionary or update its count
            m[arr[r]] = m.get(arr[r], 0) + 1
            
            # If there are more than 2 types of fruits in the window
            if len(m) > 2:
                # Reduce the count of the fruit at the left pointer
                m[arr[l]] -= 1
                
                # If the count becomes 0, remove it from the dictionary
                if m[arr[l]] == 0:
                    del m[arr[l]]
                
                # Move the left pointer forward
                l += 1
            
            # Update the maximum size of the window if it contains at most 2 types of fruits
            if len(m) <= 2:
                maxi = max(maxi, r - l + 1)
            
            # Move the right pointer forward
            r += 1
        
        # Return the maximum number of fruits that can be collected
        return maxi
