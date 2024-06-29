class solution:
    def printSaba(self, n, i=1):
        if i>n:
            return
        i+=1
        print("Saba", end=" ")
        self.printSaba(n, i)
    