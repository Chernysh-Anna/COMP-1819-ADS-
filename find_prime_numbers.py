"""
Title: Unique Prime Numbers “Hidden” in Binary Strings

write a Python program that finds all unique --prime numbers-- hidden within a
given --binary string--, and --less-- than a given integer number --N--.

"""
"------------------------------------------------------------------------------------"
"""
№1
Idea:
1.Check if valid (contains only 0 or 1)

2.find all possible combo in our binary string , but has limit --len(bin(n)) - 2 -- (all strings len(1), len(2) ... len(n))
(need a set to store results)

3.turn each combo to decimal and check if it prime and <n
(need a set to store results)


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
    max_length = len(bin(n)) - 2  # limit for search --might need to be change to  root(n)+1?
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
"""

"------------------------------------------------------------------------------------"


"""
№2
Idea: 
1.Search all primes number <= N
2.Find them (if exist) in lst

#check primes
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#find all prime numbers <=n
def generate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            binary_ver = bin(i)[2:]
            primes.append(binary_ver)
    return primes



#check if prime number <=n in our binary lst
def find_matching_primes(binary_str, binary_primes):
    answer = []
    for binary_prime in binary_primes:
        if binary_prime in binary_str:
            answer.append(int(binary_prime, 2))
    return answer


def format_output(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    primes = generate_primes(n)
    matching_primes = find_matching_primes(binary_str, primes)

    if not matching_primes:
        return "0: No prime numbers found"

    total = len(matching_primes)
    if total < 6:
        return f"{total}: {', '.join(map(str, matching_primes))}"
    else:
        first_three = matching_primes[:3]
        last_three = matching_primes[-3:]
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"

# Example usage
binary_str = "101011"
n = 100
print(format_output(binary_str, n))
"""

"--------------------------------------------"

"""
№3
idea:
use dictonary --> find each number in binary string, and store it in dictonary
find number in binary string
"10110"
len 1 --> [1],[0]
len 2 --> [10], [01],[11],[10]
.....


                         **is value new(not in dictionary) ** 
Yes                                       | No
1.add to dictionary + change to base 10   |skip
2.Check is_prime                          |
Yes                 | No                  |
Add to result set   |skip/next number     |
3.check if it prime and <n                |


"""

#check primes
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#main
def find_primes_dp(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    substr_map = {}  # dictionary
    primes = set()

    for i in range(len(binary_str)):
        for j in range(i + 1, len(binary_str) + 1):
            sub = binary_str[i:j]
            if sub not in substr_map:
                substr_map[sub] = int(sub, 2)

            decimal_value = substr_map[sub]
            if decimal_value < n and is_prime(decimal_value):
                primes.add(decimal_value)

    return primes

def format_output(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    answer = find_primes_dp(binary_str, n)
    if not answer:
        return "0: No prime numbers found"

    total = len(answer)
    if total < 6:
        return f"{total}: {', '.join(map(str, answer))}"
    else:
        first_three = answers[:3]
        last_three = answer[-3:]
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"


# Example usage
binary_str = "101011"
n = 100
print(format_output(binary_str, n))




