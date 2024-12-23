"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted."""

from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []  # Max heap (simulated with negative values)
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure.
        """
        heappush(self.small, -num)  # Add to max heap
        # Move the largest element of small (max heap) to large (min heap)
        heappush(self.large, -heappop(self.small))

        # If large heap has more elements, move the smallest element of large to small
        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        """
        Returns the median of current data stream
        """
        # If the heaps have equal size, the median is the average of the two heap's top elements
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        # If the small heap has more elements, return the top element of the small heap (which is the max element)
        elif len(self.small) > len(self.large):
            return -self.small[0]
        # Otherwise, return the top element of the large heap (which is the min element)
        else:
            return self.large[0]
