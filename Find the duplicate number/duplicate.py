class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]  # Initialize both tortoise and hare to the first element of nums.
        while True:  # Loop indefinitely until a break condition is met.
            tortoise = nums[tortoise]  # Move the tortoise pointer one step forward.
            hare = nums[nums[hare]]  # Move the hare pointer two steps forward.
            if tortoise == hare:  # If tortoise and hare meet, indicating the presence of a cycle:
                break  # Exit the loop.

        # Find the "entrance" to the cycle.
        tortoise = nums[0]  # Reset the tortoise pointer to the beginning of nums.
        while tortoise != hare:  # Loop until tortoise and hare meet again.
            tortoise = nums[tortoise]  # Move the tortoise pointer one step forward.
            hare = nums[hare]  # Move the hare pointer one step forward.

        return hare  # Return the duplicate element found (the "entrance" to the cycle).
