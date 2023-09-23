def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    """
    Returns the nth prime number.
    """
    count = 0
    i = 2
    while count < n:
        if is_prime(i):
            count += 1
        i += 1
    return i - 1

# Test the function with n = 10001
print(nth_prime(10001)) 

 # Output: 104743