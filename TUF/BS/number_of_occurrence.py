"""Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr."""
class Solution:
    # Function to count occurrences of a given number 'x' in an array 'arr'
    def count(self, arr, n, x):
        # Initialize an empty dictionary to store the frequency of elements
        dict = {}
        
        # Iterate through the array 'arr'
        for i in arr:
            if i not in dict:
                # If the element is not already in the dictionary, add it with count 1
                dict[i] = 1
            else:
                # If the element already exists, increment its count by 1
                dict[i] += 1
        
        # After building the dictionary, check if 'x' is in the dictionary
        if x in dict:
            # If 'x' exists, return its count from the dictionary
            return dict[x]
        
        # If 'x' is not found in the dictionary, return 0 (indicating no occurrences)
        return 0
