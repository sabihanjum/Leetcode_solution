class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0

        if n==1:
            return 1
        prev1, prev2 = 0,1
        temp = 0
        for i in range(2, n+2):
            temp = prev1 + prev2
            prev2 = prev1
            prev1 = temp
        return temp