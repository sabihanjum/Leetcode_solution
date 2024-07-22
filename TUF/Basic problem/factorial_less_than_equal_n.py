class solution:
    def factorialNumbers(self, n):
        arr = []
        def helper(fac_of, nxt):
            if fac_of <= n:
                arr.append(fac_of)
                helper(fac_of*(nxt+1), nxt+1)
            helper(1,1)
            return arr