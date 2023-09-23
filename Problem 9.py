def pythagorean_triplet(n):
    """
    Returns the product of the Pythagorean triplet (a, b, c) for which a + b + c = n.
    """
    for a in range(1, n):
        for b in range(a + 1, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

# Test the function with n = 1000
print(pythagorean_triplet(1000)) 

 # Output: 31875000