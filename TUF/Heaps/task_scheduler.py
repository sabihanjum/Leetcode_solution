"""You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks."""

from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Function to find the minimum time required to complete all tasks with a cooling period `n`.
        
        :param tasks: List[str] - A list of tasks represented by uppercase letters.
        :param n: int - The cooling period during which the same task cannot be executed.
        :return: int - The minimum time required to execute all tasks.
        """
        # Count the frequency of each task
        count = Counter(tasks)

        # Create a max heap (invert counts for max heap behavior in Python's min heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0  # Track the total time taken
        q = deque()  # Queue to store tasks that are cooling down with their ready time

        # Process tasks while there are tasks in the heap or in the cooling queue
        while maxHeap or q:
            time += 1  # Increment time at each unit

            # Process the next available task if the heap is not empty
            if maxHeap:
                # Get the task with the highest frequency
                cnt = 1 + heapq.heappop(maxHeap)  # Decrement count as task is executed
                if cnt:  # If the task still has remaining occurrences
                    # Add it to the cooling queue with its ready time (current time + cooling period)
                    q.append([cnt, time + n])

            # Check if the task at the front of the queue is ready to be added back to the heap
            if q and q[0][1] == time:  # If the task's ready time matches the current time
                # Push the task back into the heap
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
