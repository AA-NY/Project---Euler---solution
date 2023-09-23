def sum_of_primes(n):
    """
    Returns the sum of all primes below n.
    """
    # Initialize a boolean array to mark all numbers as prime
    is_prime = [True] * n

    # 0 and 1 are not prime
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes algorithm to mark non-prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i ** 2, n, i):
                is_prime[j] = False

    # Sum all prime numbers
    return sum(i for i in range(n) if is_prime[i])

# Test the function with n = 2000000
print(sum_of_primes(2000000))  

# Output: 142913828922