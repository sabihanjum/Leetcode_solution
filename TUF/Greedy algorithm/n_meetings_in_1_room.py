"""You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting."""

def maximumMeetings(self, start, end):
    """
    Function to find the maximum number of meetings that can be held in a room
    without any overlap.

    :param start: List of start times of the meetings
    :param end: List of end times of the meetings
    :return: Maximum number of meetings that can be scheduled
    """
    # Combine start and end times into a list of tuples and sort by end times
    meetings = list(zip(start, end))
    meetings.sort(key=lambda x: x[1])  # Sort meetings by their end time

    last_end_time = -1  # To track the end time of the last attended meeting
    count = 0  # Counter for the number of meetings that can be attended

    # Iterate through the sorted list of meetings
    for start_time, end_time in meetings:
        # If the start time of the current meeting is after the last attended meeting's end time
        if start_time > last_end_time:
            count += 1  # Increment the count of meetings
            last_end_time = end_time  # Update the end time of the last attended meeting

    return count
