def printArray(arr, n):
    print("The reverse array is: ")
    for i in range(n):
        print(arr[i], end =" ")
    print()

def reverseArray(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseArray(arr, start + 1, end - 1)