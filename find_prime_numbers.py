"""
Title: Unique Prime Numbers “Hidden” in Binary Strings

Task: extracts all unique prime numbers hidden within a given binary string
that are less than a given integer N.
"""
"------------------------------------------------------------------------------------"

"""
№1
Base Solution:

Idea:
1. Validate the binary string (contains only 0s and 1s).
2. Generate all possible substrings up to length `len(bin(N)) - 2`.
3. Convert each substring to decimal, check if it's prime and less than N.
4. Store results in a set to avoid duplicates.
5. Sort and format output accordingly.

"""

"""
Test result: It seems to give the correct answers, but only passes tests 8 and 10 (the last 2 ->Timeout)


Better Approaches:
1.Avoid repeated substrings
2.Precompute primes using 6k ± 1 rule for numbers up to N and use a lookup table.
3.If a binary substring starts with 0, it can often be skipped.
4.Use a sliding window technique to reduce redundant substring checks.
"""


def is_prime(n):
    """
      Determines whether a given integer n is a prime number.

      A prime number is a number greater than 1 that has no divisors other than 1 and itself.

      Parameters:
      n (int): The number to check if it is prime.

      Returns:
      bool: True if n is a prime number, False otherwise.
      """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(binary_str, n):
    """
      The function extracts all possible substrings of the binary string, converts each substring to
      a decimal number, checks if it is prime and less than n, and returns a sorted list of unique primes.

      Parameters:
      binary_str (str): A string of 0s and 1s (binary representation).
      n (int): The upper limit to check primes against.

      Returns:
      list: A sorted list of unique prime numbers less than n, formed from substrings of binary_str.
      """
    # Validate binary_str input
    if not all(c in '01' for c in binary_str):
        return []

    # Set max substring length based on n
    max_length = len(bin(n)) - 2
    substring = set()

    # Generate all possible substrings from binary_str
    for length in range(1, max_length + 1):
        for i in range(len(binary_str) - length + 1):
            substring.add(binary_str[i:i + length])  # Extract substrings

    primes = set()
    for s in substring:
        decimal = int(s, 2)
        if  decimal < n and is_prime(decimal):
            primes.add(decimal)

    return sorted(primes)


# Format answer
def format_output(binary_str, n):
    """
       The function returns the number of unique prime numbers found, as well as the first three and last
       three primes in a sorted list. If there are fewer than six primes, it returns all of them.

       Parameters:
       binary_str (str): A binary string containing only '0' and '1'.
       n (int): The upper limit for the prime number search.

       Returns:
       str: A formatted string showing the count of primes and the first and last few primes found.

       Reference:
       Bala Priya C (2024) How to check if a number is prime in Python. Available at: https://geekflare.com/dev/prime-number-in-python/ (Accessed: 6/03/2025).
       Stack Overflow (2025) How to join values of map in Python. Available at: https://stackoverflow.com/questions/21517024/how-to-join-values-of-map-in-python (Accessed: 9/03/2025).
       Unknown (2025) Python Program to Check Prime Number with Examples. Available at: https://www.ccbp.in/blog/articles/python-program-to-check-prime-number (Accessed: 10/03/2025).
       """
    # Validate binary string
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    # Find prime numbers
    primes = find_primes(binary_str, n)

    if not primes:
        return "0: No prime numbers found"

    total = len(primes)

    primes = sorted(primes)  # Sorting even though it's already sorted

    # Get first three primes
    first_three = []
    for i in range(3):
        if i < len(primes):
            first_three.append(primes[i])

    # Get last three primes
    last_three = []
    for i in range(len(primes) - 3, len(primes)):
        if i >= 0:
            last_three.append(primes[i])

    # Format the output based on the number of primes found
    if total < 6:
        return f"{total}: {', '.join(map(str, primes))}"
    else:
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"









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
"""

#check primes
#def is_prime(n):

#main
def find_primes_3(binary_str, n):
    """
       Finds all unique prime numbers that can be formed from substrings of a given binary string,
       where the prime numbers are less than the given integer n.

       The function iterates through all possible substrings of the binary string, converts each substring
       to a decimal number, checks if it is prime, and stores the unique prime numbers.

       Parameters:
       binary_str (str): A string containing only '0' and '1'.
       n (int): The upper limit for the prime numbers.

       Returns:
       set: A set of unique prime numbers found from substrings of binary_str.

       References:
       NeetCodeIO (2024), Split a String Into the Max Number of Unique Substrings - Leetcode 1593 - Python,
         https://www.youtube.com/watch?v=fLjeVALxzjg
        Javier Canales Luna(2024), A Guide to Python Hashmaps, https://www.datacamp.com/tutorial/guide-to-python-hashmaps
       """
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    substr_map = {}
    primes = set()

    # Generate all possible substrings from binary_str
    for i in range(len(binary_str)):
        for j in range(i + 1, len(binary_str) + 1):
            sub = binary_str[i:j]

            # Convert substring to decimal only if not already computed
            if sub not in substr_map:
                substr_map[sub] = int(sub, 2)

            decimal_value = substr_map[sub]

            # Check if decimal_value is prime and within the limit
            if decimal_value < n and is_prime(decimal_value):
                primes.add(decimal_value)

    return primes

def format_output3(binary_str, n):
    """

      The function returns the number of unique prime numbers found, along with the first three
      and last three primes in sorted order. If fewer than six primes are found, it returns all of them.

      Parameters:
      binary_str (str): A binary string containing only '0' and '1'.
      n (int): The upper limit for the prime number search.

      Returns:
      str: A formatted string showing the count of primes and the first and last few primes found.

      References:
       GeeksforGeeks (2025), Python List Slicing, https://www.geeksforgeeks.org/python-list-slicing/
       Stack Overflow (2025), How to join values of map in Python,
        https://stackoverflow.com/questions/21517024/how-to-join-values-of-map-in-python
      """
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"
    #  sorted list of unique primes
    answer = sorted(find_primes_3(binary_str, n))

    # case where no primes are found
    if not answer:
        return "0: No prime numbers found"

    total = len(answer)

    # Format output based on the number of primes found
    if total < 6:
        return f"{total}: {', '.join(map(str, answer))}"
    else:
        first = answer[:3]
        last = answer[-3:]
        return f"{total}: {', '.join(map(str, first))}, {', '.join(map(str, last))}"





"----------------------------OPTIJMISM--------------------------"
"""
Prime checking optimization:
    ~Added early returns for 2 and 3
    ~Added checks for divisibility by 2 and 3
    ~Implemented the 6k±1 optimization to reduce iterations

Substring generation improvements:
    ~Skipped leading zeros
    ~Added a seen_substrings set to avoid reprocessing duplicate substrings

Other optimizations:
    ~Simplified the max_length calculation
    ~Cleaned up the format_output function
    ~Used list slicing for first_three and last_three instead of loops
"""

def is_prime_v3(n):
    """
    Checks whether a given integer n is a prime number using the 6k ± 1 optimization.

    Prime numbers are greater than 1 and have no divisors other than 1 and themselves.
    This function optimizes the check by:
    - Returning False for numbers < 2.
    - Handling 2 and 3 as special cases (both are prime).
    - Eliminating even numbers and multiples of 3.
    - Using 6k ± 1 to check divisibility for numbers greater than 3.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is a prime number, False otherwise.



    References:
    Stack Overflow (2023) How do I generate primes using 6k ± 1 rule?*. Available at: https://stackoverflow.com/questions/31837761/how-do-i-generate-primes-using-6k-1-rule (Accessed: 15/03/2025).
     Unknown (2025), Python Program to Check Prime Number With Examples,
      https://www.ccbp.in/blog/articles/python-program-to-check-prime-number
     Nitika Sharma (2024), Prime Number Program in Python,
      https://www.analyticsvidhya.com/blog/2023/09/prime-number-program-in-python/
    """

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisibility using 6k±1 optimization
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes_v3(binary_str, n):

    """
        This function efficiently generates substrings and converts them to decimal values.
        It skips redundant calculations using a set to store already-processed substrings.

        Parameters:
        binary_str (str): A binary string consisting of '0' and '1'.
        n (int): The upper limit for prime numbers.

        Returns:
        list: A sorted list of unique prime numbers found from substrings of binary_str.

        References:
        - GeeksforGeeks (2025), Sliding Window Technique,
          https://www.geeksforgeeks.org/window-sliding-technique/
        """

    #Early validatio
    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    # Determine maximum length
    max_bin_length = len(bin(n - 1)) - 2  # -2 for '0b' prefix
    max_length = min(len(binary_str), max_bin_length)

    # Use set for unique substrings and primes
    primes = set()
    seen_substrings = set()

    # Process substrings more efficiently
    for start in range(len(binary_str)):
        # Skip leading zeros
        if binary_str[start] == '0' and start < len(binary_str) - 1:
            continue

        current = ""
        for end in range(start, min(start + max_length, len(binary_str))):
            current += binary_str[end]

            # Skip if we've seen this substring before
            if current in seen_substrings:
                continue

            seen_substrings.add(current)
            decimal = int(current, 2)

            # Check for prime
            if decimal < n and is_prime_v3(decimal):
                primes.add(decimal)

    return sorted(primes)


def format_output_v3(binary_str, n):
    """
       The function returns the number of unique prime numbers found, along with the first three and
       last three primes in sorted order. If fewer than six primes are found, it returns all of them.

       Parameters:
       binary_str (str): A binary string containing only '0' and '1'.
       n (int): The upper limit for the prime number search.

       Returns:
       str: A formatted string showing the count of primes and the first and last few primes found.
       """

    if not all(c in '01' for c in binary_str):
        return "0: Invalid binary string"

    primes = find_primes_v3(binary_str, n)

    if not primes:
        return "0: No prime numbers found"

    total = len(primes)

  #Format output based on the number of primes found
    if total <= 6:
        return f"{total}: {', '.join(map(str, primes))}"
    else:
        first_three = primes[:3]
        last_three = primes[-3:]
        return f"{total}: {', '.join(map(str, first_three))}, {', '.join(map(str, last_three))}"
