"""There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children."""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Initialize an array to keep track of the candies for each child.
        # Every child gets at least 1 candy.
        arr = [1] * len(ratings)

        # Traverse from left to right.
        # If the current child's rating is higher than the previous child's rating,
        # give them one more candy than the previous child.
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        # Traverse from right to left.
        # If the current child's rating is higher than the next child's rating,
        # make sure they get at least one more candy than the next child.
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)

        # Return the total number of candies distributed.
        return sum(arr)
