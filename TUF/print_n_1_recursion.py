class solution:
    def printNo(self, n):
        if n<1:
            return
        print(n, end=" ")
        self.printNo(n-1)