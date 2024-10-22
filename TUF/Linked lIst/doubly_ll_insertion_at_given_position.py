"""Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at 
the position just after pth node in the doubly linked list and return the head of updated list."""

def addNode(self, head, p, x):
    # Initialize a counter to track the current position
    count = 0
    # Create a temporary pointer to traverse the list starting from head
    tmp = head

    # Traverse the list until you reach the desired position 'p' or end of the list
    while count <= p and tmp != None:
        # Increment the counter as you move to the next node
        count += 1
        tmp = tmp.next
        
        # When the desired position 'p' is reached
        if count == p:
            # Create a new node 'ptr' with data 'x'
            ptr = Node(x)  # Assuming Node is a predefined class
            # Link the new node with the next node in the list
            ptr.next = tmp.next
            # Link the new node with the previous node (current node at 'p')
            ptr.prev = tmp
            # Update the current node's next pointer to point to the new node
            tmp.next = ptr

    # Update the head of the list to reflect changes (if applicable)
    head = tmp
    return head
