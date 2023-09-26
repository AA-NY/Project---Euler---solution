def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum_of_primes = 0
for i in range(2, 2000000):
    if is_prime(i):
        sum_of_primes += i

print(sum_of_primes)

#the output = 142913828922