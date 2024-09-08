class Solution:
    # User function Template for python3

    def merge(self, l, mid, r, arr):
        # initialization
        arr1 = arr[l:mid+1]
        arr2 = arr[mid+1:r+1]
        
        m, n = len(arr1), len(arr2)
        cnt = 0
        
        k = l
        i = 0
        j = 0
        while i < m and j < n:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                cnt += (mid - l + 1 - i)  # Increment count of inversions
                arr[k] = arr2[j]
                j += 1
            k += 1
        
        # Copy remaining elements from arr1, if any
        while i < m:
            arr[k] = arr1[i]
            i += 1
            k += 1
        
        # Copy remaining elements from arr2, if any
        while j < n:
            arr[k] = arr2[j]
            j += 1
            k += 1
            
        return cnt

    def mergeSort(self, l, r, arr):
        x = 0
        if l < r:
            mid = l + (r - l) // 2
            x += self.mergeSort(l, mid, arr)  # Recursively sort the left half
            x += self.mergeSort(mid + 1, r, arr)  # Recursively sort the right half
            x += self.merge(l, mid, r, arr)  # Merge both halves and count inversions
        return x

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        return self.mergeSort(0, n - 1, arr)  # Closing parenthesis fixed
