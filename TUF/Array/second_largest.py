class Solution:
    def print2largest(self, arr):
        # Check if there are at least two elements
        if len(arr) < 2:
            return -1
        
        max_num = float('-inf')
        second_max = float('-inf')
        
        # Find the maximum number
        for num in arr:
            if num > max_num:
                max_num = num
        
        # Find the second maximum number
        for num in arr:
            if num > second_max and num != max_num:
                second_max = num
        
        # If second_max is still -inf, it means there was no second maximum
        if second_max == float('-inf'):
            return -1
        else:
            return second_max
