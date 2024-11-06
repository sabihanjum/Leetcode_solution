"""Given an integer, K. Generate all binary strings of size k without consecutive 1’s."""

def generate_binary_strings(n: int):
    # Base case: if n is 0, return an empty string in a list as there's no binary digit
    if n == 0:
        return [""]
    # Base case: if n is 1, return the list ["0", "1"] representing one-bit binary numbers
    if n == 1:
        return ["0", "1"]
    
    # Initialize an empty list to hold all binary strings of length n
    result = []
    
    # Recursive call to generate binary strings of length n-1
    for s in generate_binary_strings(n - 1):
        # Append "0" to the current string `s` and add to the result
        result.append(s + "0")
        
        # Conditionally append "1" to the current string `s` if the last character is not "1"
        # This ensures that there are no consecutive "1"s in the result
        if s[-1] != "1":
            result.append(s + "1")
    
    return result
