"""You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far."""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the KthLargest class.
        
        :param k: The k-th largest element to track.
        :param nums: List of integers to initialize the stream.
        """
        # Initialize the min-heap with the given numbers and store k
        self.minHeap, self.k = nums, k

        # Convert nums into a valid min-heap
        heapq.heapify(self.minHeap)

        # Ensure the heap only contains the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        Add a new value to the stream and return the k-th largest element.
        
        :param val: Integer to add to the stream.
        :return: The k-th largest element in the updated stream.
        """
        # Add the new value to the min-heap
        heapq.heappush(self.minHeap, val)

        # If the heap exceeds k elements, remove the smallest one
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The root of the heap is the k-th largest element
        return self.minHeap[0]
