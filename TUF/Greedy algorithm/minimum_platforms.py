"""You are given the arrival times arr[] and departure times dep[] of all trains that arrive at a railway station on the same day. Your task is to determine the minimum number of platforms required at the station to ensure that no train is kept waiting.

At any given time, the same platform cannot be used for both the arrival of one train and the departure of another. Therefore, when two trains arrive at the same time, or when one arrives before another departs, additional platforms are required to accommodate both trains."""

class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        # Sort the arrival and departure times to process them in order
        arr.sort()
        dep.sort()
        
        # Initialize pointers for arrival and departure arrays
        i, j = 0, 0
        
        # Initialize variables to track the maximum platforms needed (`maxi`)
        # and the current number of platforms in use (`cnt`)
        maxi, cnt = 0, 0
        
        # Iterate through all the arrival times
        while i < len(arr):
            # If the current train arrives before or at the same time the last train departs,
            # increment the platform count (`cnt`) and move to the next train arrival
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            else:
                # Otherwise, the current train departs, so decrement the platform count (`cnt`)
                # and move to the next train departure
                cnt -= 1
                j += 1
            
            # Update the maximum platforms needed (`maxi`)
            maxi = max(maxi, cnt)
        
        # Return the maximum number of platforms needed at any time
        return maxi
