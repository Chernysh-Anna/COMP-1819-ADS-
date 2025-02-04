"""
Title: Unique Prime Numbers “Hidden” in Binary Strings

write a Python program that finds all unique --prime numbers-- hidden within a
given --binary string--, and --less-- than a given integer number --N--.

"""
"""
Idea:
1.Check if valid (contains only 0 or 1)

2.find all possible combo in our binary string , but has limit --len(bin(n)) - 2 -- (all strings len(1), len(2) ... len(n))
(need a set to store results)

3.turn each combo to decimal and check if it prime and <n
(need a set to store results)

"""
#Check if a number is prime
#is 1 and 0 prime?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#main
#Find all unique prime numbers from substrings of the binary str that are less than N
def find_primes(binary_str, n):
    #check
    if not all(c in '01' for c in binary_str):
        return []

    # find all substrings until  len(bin(n))
    max_length = len(bin(n)) - 2  # limit for search
    substring = set()
    for length in range(1, max_length + 1):
        for i in range(len(binary_str) - length + 1):
            substring.add(binary_str[i:i + length]) # [0,1] [1,2],[2,3] .....

    primes = set()
    #main check
    for s in substring:
        decimal = int(s, 2)
        if decimal < n and is_prime(decimal):
            primes.add(decimal)

    return primes

#Format answer
def format_output(primes):
    if not primes:
        return "0: Invalid binary string" #--> if string is valid but no prime numbers?

    total = len(primes)
    if total < 6:
        return f"{total}: {', '.join(map(str, primes))}"
    else:
        first_three = primes[:3]
        last_three = primes[-3:]
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"


"""example"""
# example
binary_str = "101011"
N = 99
primes = find_primes(binary_str, N)
print(format_output(primes))

binary_str = "0110"
N = 5
primes = find_primes(binary_str, N)
print(format_output(primes))

binary_str = "COMP"
N = 4
primes = find_primes(binary_str, N)
print(format_output(primes))








