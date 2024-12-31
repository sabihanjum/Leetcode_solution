"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping."""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Function to find the minimum number of intervals that need to be removed 
        to make the rest of the intervals non-overlapping.
        
        :param intervals: List of intervals [start, end]
        :return: Minimum number of intervals to remove
        """
        # Sort intervals by their start time
        intervals.sort()

        res = 0  # Counter for the number of intervals removed
        prevEnd = intervals[0][1]  # End time of the last non-overlapping interval

        # Iterate through the intervals starting from the second one
        for start, end in intervals[1:]:
            # If the current interval starts after or when the previous interval ends
            if start >= prevEnd:
                prevEnd = end  # Update prevEnd to the current interval's end
            else:
                # There is an overlap, increment the removal counter
                res += 1
                # Retain the interval with the smaller end time to minimize overlap
                prevEnd = min(end, prevEnd)

        return res
