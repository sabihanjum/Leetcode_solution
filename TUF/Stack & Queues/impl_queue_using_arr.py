"""Implement a Queue using an Array. Queries in the Queue are of the following type:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the popped element. If the queue is empty then return -1)

We just have to implement the functions push and pop and the driver code will handle the output."""

from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()  # Initialize with deque for efficient operations

    def push(self, x):
        self.queue.append(x)  # Append to the end of the deque

    def pop(self):
        if not self.queue:  # Check if the queue is empty
            return -1
        else:
            return self.queue.popleft()  # Pop the front element efficiently
