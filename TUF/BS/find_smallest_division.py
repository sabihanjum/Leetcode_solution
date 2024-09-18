"""Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer."""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Initialize the search boundaries for the divisor
        l, r = 1, max(nums)  # The smallest divisor is 1 and the largest is the maximum number in the array
        
        # Perform binary search to find the smallest divisor
        while l <= r:
            # Calculate the middle divisor between the current boundaries
            mid = l + (r - l) // 2
            
            # Calculate the sum of the results of dividing each number by the current mid
            # and rounding up (ceiling division). If this sum exceeds the threshold,
            # it means we need a larger divisor.
            if sum([ceil(num / mid) for num in nums]) > threshold:
                l = mid + 1  # If sum exceeds the threshold, move the left boundary up
            else:
                r = mid - 1  # Otherwise, move the right boundary down to find a smaller divisor
        
        # Return the smallest divisor that satisfies the condition
        return l
