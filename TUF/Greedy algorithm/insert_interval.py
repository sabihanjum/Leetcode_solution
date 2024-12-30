"""You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it."""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Result list to store the merged intervals
        res = []

        # Iterate through each interval in the given list
        for i in range(len(intervals)):
            # Case 1: The new interval is completely before the current interval
            if newInterval[1] < intervals[i][0]:
                # Add the new interval to the result and append the remaining intervals
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2: The new interval is completely after the current interval
            elif newInterval[0] > intervals[i][1]:
                # Add the current interval to the result
                res.append(intervals[i])

            # Case 3: The new interval overlaps with the current interval
            else:
                # Merge the intervals by taking the minimum start and maximum end
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # Add the merged interval to the result after processing all intervals
        res.append(newInterval)
        return res
