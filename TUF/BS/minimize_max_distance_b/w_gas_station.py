"""ou are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis. You are also given an integer ‘k’. You have to place 'k' new gas stations on the X-axis. You can place them anywhere on the non-negative side of the X-axis, even on non-integer positions. Let 'dist' be the maximum value of the distance between adjacent gas stations after adding k new gas stations.
Find the minimum value of ‘dist’."""

def numberOfGasStationsRequired(dist, arr):
    """
    Function to calculate the number of gas stations required between points in the array 'arr' 
    such that the maximum distance between any two gas stations is less than or equal to 'dist'.
    
    Parameters:
    dist (float): Maximum allowed distance between gas stations.
    arr (list of int): Sorted array of positions of existing gas stations.

    Returns:
    int: Number of gas stations required to ensure the distance between any two consecutive gas stations 
         does not exceed 'dist'.
    """
    n = len(arr)  # size of the array
    cnt = 0  # count of gas stations to be added

    # Loop through each pair of consecutive gas stations:
    for i in range(1, n):
        # Calculate the number of gas stations needed between arr[i - 1] and arr[i]
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)

        # If the distance between two gas stations is exactly divisible by 'dist',
        # we need one less station since no extra one is needed at the end.
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1

        # Add the calculated number of stations needed:
        cnt += numberInBetween

    return cnt  # return total stations required


def minimiseMaxDistance(arr, k):
    """
    Function to find the minimum possible value of the maximum distance between any two consecutive gas stations,
    after adding at most 'k' gas stations between existing stations.

    Parameters:
    arr (list of int): Sorted array of positions of existing gas stations.
    k (int): Maximum number of gas stations that can be added.

    Returns:
    float: The minimized maximum distance between any two consecutive gas stations.
    """
    n = len(arr)  # size of the array
    low = 0
    high = 0

    # Find the initial maximum distance between any two consecutive gas stations:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Binary search to minimize the maximum distance between gas stations:
    diff = 1e-6  # Precision for the binary search (difference threshold)
    while high - low > diff:
        mid = (low + high) / 2.0  # Calculate the midpoint of current range
        cnt = numberOfGasStationsRequired(mid, arr)  # Count gas stations needed for mid distance

        # If the number of stations needed exceeds 'k', increase the allowed distance (move to higher side)
        if cnt > k:
            low = mid
        else:
            high = mid  # Otherwise, try reducing the distance (move to lower side)

    return high  # Return the minimized maximum distance
