from typing import List

class Solution:
    def merge(self, v: List[List[int]]) -> List[List[int]]:
        # Check if the input list is empty
        if not v:
            return []

        # Sort the intervals based on the start value of each interval
        v.sort(key=lambda interval: interval[0])
        # Initialize the merged intervals list with the first interval
        ans = [v[0]]

        # Iterate over the intervals starting from the second one
        for start, end in v[1:]:
            # Get the end value of the last interval in the merged list
            last_end = ans[-1][1]

            # If the current interval overlaps with the last interval in the merged list
            if start <= last_end:
                # Merge the intervals by updating the end value of the last interval
                ans[-1][1] = max(last_end, end)
            else:
                # If there's no overlap, add the current interval to the merged list
                ans.append([start, end])

        # Return the merged intervals list
        return ans
