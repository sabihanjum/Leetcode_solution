"""Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)"""
        
class MyQueue:
    def __init__(self):
        self.queue=[]
    
    #Function to push an element into the queue.
    def push(self, item): 
        
        self.queue.append(item)
    
    #Function to pop front element from the queue.
    def pop(self):
        if not self.queue:
            return -1
        return self.queue.pop(0)