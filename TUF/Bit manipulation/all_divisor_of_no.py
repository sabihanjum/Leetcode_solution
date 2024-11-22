"""Given an integer N, print all the divisors of N in the ascending order."""

class Solution:
    def print_divisors(self, N):
        # Initialize two lists to store divisors
        # 'st' for smaller divisors and 'end' for larger divisors
        st = []  
        end = []
        
        # Calculate the square root of N (rounded down) to limit the iteration range
        x = round(N**(1/2))
        
        # Iterate from 1 to the square root of N
        for i in range(1, x + 1):
            # Check if 'i' is a divisor of N
            if N % i == 0:
                # Add 'i' to the smaller divisors list
                st.append(i)
                
                # Check if the corresponding larger divisor is distinct and valid
                if N % (N // i) == 0 and N // i != i:
                    # Add the larger divisor to the 'end' list
                    end.append(N // i)
        
        # Combine smaller divisors and reversed larger divisors for proper order
        y = st + end[::-1]
        
        # Print all divisors in order
        for i in range(len(y)):
            print(y[i], end=" ")
