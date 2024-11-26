"""Let's give it a try! You have a linked list and must implement the functionalities push and pop of stack using this given linked list. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. 
The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.
Note: The input is given in the form of queries. Since there are two operations push() and pop(), there is two types of queries as described below:
(i) 1   (a query of this type takes x as another parameter and pushes it into the stack)
(ii) 2  (a query of this type means to pop an element from the stack and return the popped element)
Input is separated by space and as described above. """

class MyStack:
    def __init__(self):
        self.head = None

    # class StackNode:
    
    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    #Function to push an integer into the stack.
    def push(self, data):
        
        # Add code here
        new = StackNode(data)
        new.next = self.head
        self.head = new


    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if self.head:
            x = self.head.data
            self.head = self.head.next
            return x
        else:
            return -1