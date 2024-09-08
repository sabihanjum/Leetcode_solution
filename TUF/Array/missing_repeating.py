class Solution:
    def findTwoElement(self, arr, n):
        # Step 1: Find the duplicate number using a dictionary
        ans1 = {}
        duplicate = -1
        for num in arr:
            if num in ans1:
                duplicate = num
            else:
                ans1[num] = True

        # Step 2: Calculate the sum of the array
        actual_sum = sum(arr)
        
        # Step 3: Calculate the expected sum of numbers from 1 to n
        expected_sum = (n * (n + 1)) // 2
        
        # Step 4: Find the missing number using the difference between expected and actual sums
        # Since one number is duplicated, subtracting the actual sum from the expected sum will
        # give the missing number.
        missing = expected_sum - (actual_sum - duplicate)
        
        # Return the duplicate and missing numbers as a list
        return [duplicate, missing]