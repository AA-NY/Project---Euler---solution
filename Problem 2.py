def sum_even_fibonacci(n):
    """
    Returns the sum of all even Fibonacci numbers below n.
    """
    # Initialize variables
    a, b = 1, 2
    total = 0

    # Loop through Fibonacci sequence
    while b < n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    return total

# Test the function with n = 4000000
print(sum_even_fibonacci(4000000))  

# Output: 4613732