class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set to remove duplicates and allow O(1) lookups
        nums = set(nums)

        # Initialize a variable to keep track of the longest streak found
        longest_streak = 0

        # Iterate over each number in the set
        for num in nums:
            # Check if the current number is the start of a sequence
            # (i.e., the previous number is not in the set)
            if num - 1 not in nums:
                current = num  # Start a new sequence from the current number
                current_streak = 1  # Initialize the streak length to 1

                # Continue to extend the sequence by checking consecutive numbers
                while current + 1 in nums:
                    current_streak += 1  # Increment the streak length
                    current += 1  # Move to the next consecutive number

                # Update the longest streak if the current streak is longer
                longest_streak = max(longest_streak, current_streak)

        # Return the length of the longest consecutive sequence found
        return longest_streak
