class solution:
    def printNo(self, N):
        if N <= 0:
            return
        
        self.printNo(N-1)
        print(N, end=" ")