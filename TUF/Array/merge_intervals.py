class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on the starting time (first element of each interval)
        intervals.sort(key = lambda x: x[0])

        # Initialize an empty list to store merged intervals
        merged = []
        
        # Iterate through each interval in the sorted list
        for interval in intervals:
            # If the merged list is empty or the last interval in the merged list does not overlap with the current interval
            if not merged or merged[-1][1] < interval[0]:
                # Append the current interval to the merged list as there is no overlap
                merged.append(interval)
            else:
                # If the current interval overlaps with the last merged interval, merge them by updating the end time
                # The end time will be the maximum of the two overlapping intervals' end times
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Return the merged list of intervals
        return merged
