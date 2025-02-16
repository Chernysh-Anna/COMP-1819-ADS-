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
 It find all primes until n and dont refer to input bn_string(i dont know why....)
 
"""
"""
info:
test result: It seems to give the correct answers, but only passes tests 8 and 10 (the last 2 ->Timeout)

~ is_prime(n) :
    -Time Complexity:  O(sqr(n))
    -Space Complexity: O (1)

~ Total :
    -Time Complexity:  O(m^2 * sqr(n)) (where m is the length of binary_str).
    -Space Complexity: O (m^2)

Better Approaches:
1.Avoid repeated substrings
2.Precompute primes using the Sieve of Eratosthenes for numbers up to N and use a lookup table.
3.If a binary substring starts with 0, it can often be skipped.
4.Use a sliding window technique to reduce redundant substring checks.
5.Parallelization: Check primality in parallel for large datasets.


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


# Find all unique prime numbers from substrings of the binary string that are less than N
def find_primes(binary_str, n):
    # Check if binary_str is valid
    if not all(c in '01' for c in binary_str):
        return []

    # Find all substrings up to min(len(binary_str), len(bin(n)) - 2)
    max_length = len(bin(n)) - 2
    substring = set()

    for length in range(1, max_length + 1):
        for i in range(len(binary_str) - length + 1):
            substring.add(binary_str[i:i + length])  # Extract substrings

    primes = set()
    for s in substring:
        decimal = int(s, 2)
        if  decimal < n and is_prime(decimal):  # Ignore 0 and 1
            primes.add(decimal)

    return sorted(primes)


# Format answer
def format_output(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    primes = find_primes(binary_str, n)

    if not primes:
        return "0: No prime numbers found"

    total = len(primes)

    if total < 6:
        return f"{total}: {', '.join(map(str, primes))}"
    else:
        first_three = list(primes)[:3]
        last_three = list(primes)[-3:]
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"




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

"""
info:
test result: It seems to give the correct answers, but only passes tests 4 out of 10 (->Timeout)


~ Total
    -Time Complexity:  O(n *sqrt(n)+ p+d)
    -Very slow
   

Possible Improvements:
1.Use a Hash Set for Faster Lookups
2.Use a Sieve to Generate Primes Faster





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

"""
info:
test result: It seems to give the correct answers, but only passes tests 8 out of 10 (the last 2 ->Timeout)


~ Total
    -Time Complexity:  O(m^2 +usqrt(N)) ( m -ength of binary_str, u - number of unique substrings).
    ~Space : O(m^2 +u)  

Possible Improvements:
1.generate primes first (like in format_output2 approach) and check if their binary form exists in binary_str
2.Use a Prime Sieve Instead of Checking Each Number





"""

#check primes
#def is_prime(n):

#main
def find_primes_3(binary_str, n):
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
#remove compare block to independet one so we dont really need set anymore.(maybe + for time)..... add zero front check
#answer
def format_output3(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    answer = sorted(find_primes_3(binary_str, n))  # Convert set to sorted list
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

"""
Modify version
separete check for <n and prime
add ignore substrings that start with '0'
only dictionary
boost for time
perhaps demage for memory
pass: 8/10
"""
def find_primes_4(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    substr_map = {}  # Stores unique substrings with their decimal values

    # Generate substrings while avoiding leading zeros (except for "0")
    for i in range(len(binary_str)):
        if binary_str[i] == '0' and i != len(binary_str) - 1:  # Skip leading zeros
            continue
        for j in range(i + 1, len(binary_str) + 1):
            sub = binary_str[i:j]
            if sub not in substr_map:
                substr_map[sub] = int(sub, 2)

    # Extract prime numbers
    prime_numbers = [value for value in substr_map.values() if value < n and is_prime(value)]

    return prime_numbers  # Return list instead of set


def format_output4(binary_str, n):
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    answer = sorted(set(find_primes_4(binary_str, n)))  # Convert list to sorted unique values
    if not answer:
        return "0: No prime numbers found"

    total = len(answer)
    if total < 6:
        return f"{total}: {', '.join(map(str, answer))}"
    else:
        first_three = answer[:3]
        last_three = answer[-3:]
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"





