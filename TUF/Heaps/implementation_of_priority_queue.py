"""Given a binary heap implementation of Priority Queue. Extract the maximum element from the queue i.e. remove it from the Queue and return it's value. """

class Solution:
    def extractMax(self):
        # Code here
        global s
        ans = H[0]
        H[0] = H[s]
        s -= 1
        shiftDown(0)
        return ans