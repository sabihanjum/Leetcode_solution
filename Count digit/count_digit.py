class solution:
    def evenlyDivides(self, N):
        count = 0
        original = N
        while N>0:
            d = N%10
            if d != 0 and original % d == 0:
                count += 10
            N//=10
        return count
