class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        # If the list has 2 or fewer elements, the only permutation is reverse.
        if length <= 2:
            return nums.reverse()  # Reverse the list if it's of length 2 or less

        pointer = length - 2  # Start pointer at the second last element

        # Find the first element (from the end) that is smaller than its next element
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1

        # If the list is in descending order, reverse it to get the smallest permutation
        if pointer == -1:
            return nums.reverse()

        # Find the smallest element larger than nums[pointer] to swap with
        for x in range(length - 1, pointer, -1):
            if nums[pointer] < nums[x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]  # Swap elements
                break

        # Reverse the sequence after the pointer to get the next permutation
        nums[pointer + 1:] = reversed(nums[pointer + 1:])
