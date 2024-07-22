class solution:

    def selectionSort(self, arr, n):
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if arr[j] < arr[min]:
                    min = j
            
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

        return arr
