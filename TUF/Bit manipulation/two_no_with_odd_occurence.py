"""Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers. Find the two numbers in decreasing order which has odd occurrences."""

class Solution:

    def twoOddNum(self, Arr, N):
        # The function finds two odd occurring numbers in an array `Arr` of length `N`
        # that appear an odd number of times. We will return the two numbers in ascending order.

        # If there are only 2 elements in the array
        if N == 2:
            # If the first element is smaller than the second, we swap them to ensure ascending order
            if Arr[0] < Arr[1]:
                Arr[0], Arr[1] = Arr[1], Arr[0]
                return Arr  # Return the swapped array
        
        else:
            # For cases where there are more than 2 elements, we first sort the array
            Arr.sort()

            # Initialize an empty list `b` which will be used to store the odd occurring elements
            b = []

            # Iterate through the array
            for i in range(0, N):
                # If the current element is already in `b`, it means it appeared before
                if Arr[i] in b:
                    # Remove the element from `b`, indicating that it appeared twice (even number of times)
                    b.remove(Arr[i])
                else:
                    # If the element is not in `b`, add it to `b` (indicating it appeared once)
                    b.append(Arr[i])

                # If there are exactly 2 odd occurring numbers in `b` and we are not at the end of the array
                if i < N - 1 and Arr[i] != Arr[i + 1] and len(b) == 2:
                    break  # Exit the loop once we find both numbers with odd occurrences

            # Ensure the two numbers in `b` are sorted in ascending order
            if b[0] < b[1]:
                b[0], b[1] = b[1], b[0]

            return b  # Return the two odd occurring numbers in ascending order
