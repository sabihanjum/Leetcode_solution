"""There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain."""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k  # Initialize left (l) to start from the beginning and right (r) to start from the k elements from the end
        total = sum(cardPoints[r:])  # Sum the k elements from the end
        res = total  # Initialize the result with this sum

        while r < len(cardPoints):  # Iterate until the right pointer reaches the end of the cardPoints list
            total += (cardPoints[l] - cardPoints[r])  # Update the total by adding the element at the left and subtracting the element at the right
            res = max(res, total)  # Update the result with the maximum sum found so far
            l += 1  # Move the left pointer one step to the right
            r += 1  # Move the right pointer one step to the right
        return res  # Return the maximum score
