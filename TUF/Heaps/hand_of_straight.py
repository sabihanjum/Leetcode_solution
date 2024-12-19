"""Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise."""

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # Count the occurrences of each card in the hand
        count = collections.Counter(hand)

        # Iterate through the sorted keys of the count dictionary (unique card values)
        for start in sorted(count):
            value = count[start]  # The number of groups we need to form starting with this card
            if value > 0:  # Only process if there are cards of this value left
                # Attempt to form groups of size `groupSize` starting from this card
                for i in range(start, start + groupSize):
                    count[i] -= value  # Deduct `value` from each card in the group
                    # If any card count goes below zero, it means the group cannot be formed
                    if count[i] < 0:
                        return False

        # If all groups can be formed successfully, return True
        return True
