"""Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1."""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        """
        Finds the nearest smaller element to the left for each element in the array.

        Args:
        A: list[int] - The input array.

        Returns:
        list[int] - An array where each element is the nearest smaller element to the left 
                    for the corresponding index in the input array. If no such element exists, append -1.
        """

        S = list()  # Stack to keep track of elements in decreasing order
        res = []    # Result list to store the nearest smaller elements

        # Iterate through the array
        for i in range(len(A)):
            # Remove elements from the stack that are not smaller than A[i]
            while len(S) > 0 and S[-1] >= A[i]:
                S.pop()

            # If the stack is empty, no smaller element exists
            if len(S) == 0:
                res.append(-1)
            else:
                # The top of the stack is the nearest smaller element
                res.append(S[-1])

            # Push the current element onto the stack
            S.append(A[i])

        return res
