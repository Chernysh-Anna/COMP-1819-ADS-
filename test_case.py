"""
Title: Test cases

Reference: W3schools(2024) Python Try Except. Availiable at: https://www.w3schools.com/python/python_try_except.asp
"""

import time

import find_prime_numbers


# Test cases

test_cases = [
    ("0100001101001111", 999999, "15: 2, 3, 5, 269, 2153, 17231"),  # Test Case 1
    ("01000011010011110100110101010000", 999999, "28: 2, 3, 5, 10729, 17231, 85837"),  # Test Case 2
    ("1111111111111111111111111111111111111111", 999999, "7: 3, 7, 31, 8191, 131071, 524287"),  # Test Case 3
    ("010000110100111101001101010100000011000100111000", 999999999, "44: 2, 3, 5, 5571347, 41577089, 55398449"),  # Test Case 4
    ("01000011010011110100110101010000001100010011100000110001", 123456789012, "52: 2, 3, 5, 84087683, 3920234023, 5625434161"),  # Test Case 5
    ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345, "64: 2, 3, 5, 2724796139969, 5841981288761, 45810224399911"),  # Test Case 6
    ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678, "71: 2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977"),  # Test Case 7
    ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789, "76: 2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977"),  # Test Case 8
    ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 1234567890123456789, "81: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661"),  # Test Case 9
    ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890, "89: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661"),  # Test Case 10
]
"""
test_cases = [
    ("1010", 7, "2: 2, 5"),  # Test Case 1
    ("1101", 7, "3: 2, 3, 5"),  # Test Case 2
    ("10110", 3, "1: 2"),  # Test Case 3
    ("011011", 4, "2: 2, 3"),  # Test Case 4
    ("1111111", 30, "2: 3, 7"),  # Test Case 5

]
"""
def run_test_cases():
    for idx, (binary_str, n, expected) in enumerate(test_cases, start=1):
        print(f"Test Case {idx}:")
        print(f" Input: binary_str = '{binary_str}', n = {n}")

        try:
            #  execution time
            start_time = time.time()
            result = find_prime_numbers.format_output(binary_str, n)
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Check if the program took more than 60 s
            if elapsed_time > 60:
                print(f" FAIL (Timeout: >60 seconds)")
                continue

            # Compare the result with the expected output
            if result == expected:
                print(f" PASS (Time: {elapsed_time:.6f} seconds)")
            else:
                print(f" FAIL")
                print(f"    Expected: {expected}")
                print(f"    Got:      {result}")
                print(f"    Time:     {elapsed_time:.6f} seconds")

        except Exception as e:
            print(f" FAIL (Error: {str(e)})")

        print("-" * 60)



def run_test_cases3():
    for idx, (binary_str, n, expected) in enumerate(test_cases, start=1):
        print(f"Test Case {idx}:")
        print(f" Input: binary_str = '{binary_str}', n = {n}")

        try:
            # execution time
            start_time = time.time()
            result = find_prime_numbers.format_output3(binary_str, n)
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Check if the program took more than 60 s
            if elapsed_time > 60:
                print(f" FAIL (Timeout: >60 seconds)")
                continue

            # Compare  with  expected output
            if result == expected:
                print(f"PASS (Time: {elapsed_time:.6f} seconds)")
            else:
                print(f" FAIL")
                print(f"    Expected: {expected}")
                print(f"    Got:      {result}")
                print(f"    Time:     {elapsed_time:.6f} seconds")

        except Exception as e:
            print(f" FAIL (Error: {str(e)})")

        print("-" * 60)

def run_test_cases_v3():
    for idx, (binary_str, n, expected) in enumerate(test_cases, start=1):
        print(f"Test Case {idx}:")
        print(f" Input: binary_str = '{binary_str}', n = {n}")

        try:
            # execution time
            start_time = time.time()
            result = find_prime_numbers.format_output_v3(binary_str, n)
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Check if  took more than 60 s
            if elapsed_time > 60:
                print(f" FAIL (Timeout: >60 seconds)")
                continue

            # Compare  with  expected output
            if result == expected:
                print(f"PASS (Time: {elapsed_time:.6f} seconds)")
            else:
                print(f" FAIL")
                print(f"    Expected: {expected}")
                print(f"    Got:      {result}")
                print(f"    Time:     {elapsed_time:.6f} seconds")

        except Exception as e:
            print(f" FAIL (Error: {str(e)})")

        print("-" * 60)


# Run the test cases
if __name__ == "__main__":
    run_test_cases()
    #run_test_cases_v3()
    #run_test_cases3()

