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
"""
"""
info:
 Doesn't work (only for short one)
 It find all primes untill n and dont refer to input bn_string(i dont know why....)
 
"""

#Check if a number is prime
#is 1 and 0 prime?
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(binary_str, n):
    """Find unique prime numbers from binary substrings that are less than N."""
    if not all(c in '01' for c in binary_str):
        return []

    substrings = set()
    length = len(binary_str)

    # Add all valid continuous substrings from start
    for i in range(length):
        sub = binary_str[:i + 1]  # Take from start to i
        if sub[0] != '0' or sub == '0':  # Only add if no leading zero or is just '0'
            substrings.add(sub)

    # Add all valid continuous substrings from end
    for i in range(length):
        sub = binary_str[i:]  # Take from i to end
        if sub[0] != '0' or sub == '0':  # Only add if no leading zero or is just '0'
            substrings.add(sub)

    primes = set()
    for s in substrings:
        decimal = int(s, 2)
        if decimal < n and is_prime(decimal):
            primes.add(decimal)

    return sorted(primes)


def format_output(binary_str, n):
    """Format the output according to task requirements."""
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"
    primes = find_primes(binary_str, n)
    if not primes:
        return "0: No prime numbers found"
    total = len(primes)
    if total < 6:
        return f"{total}: {', '.join(map(str, primes))}"
    else:
        return f"{total}: {', '.join(map(str, primes[:3]))}, ..., {', '.join(map(str, primes[-3:]))}"


# Example usage
#binary_str = "0110"
#n = 5
#print(format_output(binary_str, n))  # Output: "2: 2, 3"




"------------------------------------------------------------------------------------"


"""
№2
Idea: 
1.Search all primes number <= N
2.Find them (if exist) in lst
"""
#check primes
#def is_prime(n):


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


def format_output2(binary_str, n):
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
#binary_str = "101011"
#n = 100
#print('Idea 2:')
#print(format_output2(binary_str, n))



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
#def is_prime(n):

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
#answer
def format_output3(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    answer = find_primes_dp(binary_str, n)
    if not answer:
        return "0: No prime numbers found"

    total = len(answer)
    if total < 6:
        return f"{total}: {', '.join(map(str, answer))}"
    else:
        first_three = answer[:3]
        last_three = answer[-3:]
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"


# Example usage
#print('Idea 3:')
#print(format_output3(binary_str, n))




