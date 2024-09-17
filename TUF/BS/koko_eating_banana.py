"""Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum speed of eating is 1 (Koko can eat at least 1 banana per hour).
        # The maximum speed of eating is the largest pile (Koko can finish a whole pile in 1 hour).
        l, r = 1, max(piles)
        
        # Initialize the result to the maximum possible eating speed (upper bound).
        res = r
        
        # Binary search to find the minimum possible eating speed.
        while l <= r:
            # Calculate the middle value (potential eating speed) as a candidate.
            k = (l + r) // 2
            
            # Calculate the total hours Koko will need to finish all piles at speed 'k'.
            hours = 0
            for p in piles:
                # Use math.ceil to determine how many full hours are required to finish pile 'p' at speed 'k'.
                hours += math.ceil(p / k)
            
            # If the total hours are less than or equal to the allowed hours 'h':
            if hours <= h:
                # Update the result to the minimum speed found so far.
                res = min(res, k)
                # Try to search for a smaller eating speed by adjusting the upper bound.
                r = k - 1
            else:
                # If the total hours exceed 'h', Koko needs to eat faster, so adjust the lower bound.
                l = k + 1
        
        # Return the minimum speed that allows Koko to finish all piles in 'h' or fewer hours.
        return res
