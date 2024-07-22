class solution:
    def insert(self, alist, n, index):
        key = alist[index]
        j = index-1
        while j >= 0 and alist[j]>key:
            alist[j+1] = alist[j]
            j -= 1
            alist[j+1] = key

    def insertionSort(self, alist, n):
        for i in range(1,n):
            self.insert(alist,n,i)
        return alist


    