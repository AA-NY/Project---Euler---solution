def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

number = 600851475143
largest_factor = largest_prime_factor(number)

print("The largest prime factor of", number, "is:", largest_factor)

#The largest prime factor of 600851475143 is: 6857