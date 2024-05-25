class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0  # Initialize two variables to keep track of the maximum amount robbed from the previous two houses
        
        for n in nums:  # Iterate through each house in the input list
            temp = max(n + rob1, rob2)  # Calculate the maximum amount that can be robbed by either robbing the current house (n + rob1) or not robbing it (rob2)
            rob1 = rob2  # Update rob1 to be the previous rob2 (moving the window one step forward)
            rob2 = temp  # Update rob2 to the new calculated maximum amount (temp)
        
        return rob2  # Return the maximum amount that can be robbed from all houses
