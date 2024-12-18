"""A binary heap is a Binary Tree with the following properties:
1) Its a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to MinHeap.

You are given an empty Binary Min Heap and some queries and your task is to implement the three methods insertKey,  deleteKey,  and extractMin on the Binary Min Heap and call them as per the query given below:
1) 1  x  (a query of this type means to insert an element in the min-heap with value x )
2) 2  x  (a query of this type means to remove an element at position x from the min-heap)
3) 3  (a query like this removes the min element from the min-heap and prints it )."""

'''
heap = [0 for i in range(101)]  # our heap to be used
'''
def parent(ind):
    return ((ind - 1)//2)

def left_child(ind):
    return (ind*2)+1

def right_child(ind):
    return (ind*2)+2 
def decrease_key(ind):
    while(ind > 0 and heap[parent(ind)] > heap[ind]):
        heap[ind], heap[parent(ind)] = heap[parent(ind)], heap[ind]
        ind = parent(ind)    
#Function to insert a value in Heap.
def insertKey (x):
    global curr_size
    heap[curr_size] = x
    curr_size += 1
    decrease_key(curr_size-1)

#Function to delete a key at ith index.
def deleteKey(i):
    global curr_size
    if i >= curr_size:
        return
    heap[i] = float('-inf')
    decrease_key(i)
    extractMin()
def min_heapify(ind=0):
    
    while True:
        lch_ind = left_child(ind)
        rch_ind = right_child(ind)
        min_ind = ind
        
        if lch_ind < curr_size and heap[lch_ind] < heap[min_ind]:
            min_ind = lch_ind
        
        if rch_ind < curr_size and heap[rch_ind] < heap[min_ind]:
            min_ind = rch_ind
        
        if min_ind != ind:
            heap[min_ind], heap[ind] = heap[ind], heap[min_ind]
            ind = min_ind
        else:
            break
#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if curr_size == 0:
        return -1       
    heap[0], heap[curr_size-1] = heap[curr_size-1], heap[0]
    curr_size -= 1
    min_heapify()
    return heap[curr_size]