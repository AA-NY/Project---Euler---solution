def get_triangle_number(n):
    return (n * (n + 1)) // 2

def get_divisors_count(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 2
    # Adjust the count if num is a perfect square
    if num ** 0.5 == int(num ** 0.5):
        count -= 1
    return count

def find_triangle_number(divisors):
    n = 1
    while True:
        triangle_number = get_triangle_number(n)
        divisors_count = get_divisors_count(triangle_number)
        if divisors_count > divisors:
            return triangle_number
        n += 1

divisors = 500
result = find_triangle_number(divisors)
print(f"The first triangle number with over {divisors} divisors is: {result}")

#The first triangle number with over 500 divisors is: 76576500