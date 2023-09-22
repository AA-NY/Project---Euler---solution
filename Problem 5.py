def smallest_multiple(n):
    """
    Returns the smallest positive number that is evenly divisible by all of the numbers from 1 to n.
    """
    # Start with n and increment by n until we find a number that is divisible by all numbers from 1 to n
    i = n
    while True:
        if all(i % j == 0 for j in range(1, n+1)):
            return i
        i += n

# Test the function with n = 20
print(smallest_multiple(20)) 

 # Output: 232792560