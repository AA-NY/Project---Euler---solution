def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2    # Divide even number by 2
        else:
            n = 3 * n + 1   # Multiply odd number by 3 and add 1
        length += 1
    return length

def find_longest_collatz_sequence(limit):
    longest_length = 0
    starting_number = 0
    for n in range(1, limit):
        length = collatz_sequence_length(n)
        if length > longest_length:
            longest_length = length
            starting_number = n
    return starting_number

limit = 1000000
result = find_longest_collatz_sequence(limit)
print("The starting number under", limit, "that produces the longest Collatz chain is:", result)

#The starting number under 1000000 that produces the longest Collatz chain is: 837799