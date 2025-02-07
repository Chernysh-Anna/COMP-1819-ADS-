import time
import find_prime_numbers  # Import the functions from find_prime_numbers.py

#GENERAL CHECK (answers from moodel)

def run_test_cases0():
    test_cases = [
        ("101011", 99, "5: 2, 3, 5, 11, 43"),  # Test Case 1
        ("0110", 5, "2: 2, 3"),  # Test Case 2
        ("COMP", 4, "0: Invalid binary string"),  # Test Case 3
    ]

    print("\n===== Running Test Cases =====\n")

    for idx, (binary_str, n, expected) in enumerate(test_cases, 1):
        print(f"Test Case {idx}:")
        print(f"🔹 Input: binary_str = '{binary_str}', n = {n}")

        start_time = time.time()
        result = find_prime_numbers.format_output(binary_str, n)
        end_time = time.time()
        elapsed_time = end_time - start_time

        if result == expected:
            print(f"✅ PASS (Time: {elapsed_time:.6f} seconds)")
        else:
            print(f"❌ FAIL")
            print(f"   🔹 Expected: {expected}")
            print(f"   🔹 Got:      {result}")
            print(f"   🔹 Time:     {elapsed_time:.6f} seconds\n")

        print("-" * 60)

    print("\n===== Testing Complete =====")


def run_test_cases1():
    test_cases = [
        ("0100001101001111", 999999, "5: 2, 3, 5, 11, 43"),  # Test Case 1
        ("01000011010011110100110101010000", 999999, "6: 2, 3, 5, 11, 43, 173"),  # Test Case 2
        ("1111111111111111111111111111111111111111", 999999, "3: 3, 7, 31"),  # Test Case 3
        ("010000110100111101001101010100000011000100111000", 999999999, "7: 2, 3, 5, 11, 43, 173, 683"),  # Test Case 4
        ("01000011010011110100110101010000001100010011100000110001", 123456789012, "8: 2, 3, 5, 11, 43, 173, 683, 2731"),  # Test Case 5
        ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345, "9: 2, 3, 5, 11, 43, 173, 683, 2731, 10923"),  # Test Case 6
        ("010000110100111101001101010100000011000100111000001100010011100100100001", 123456789012345678, "10: 2, 3, 5, 11, 43, 173, 683, 2731, 10923, 43691"),  # Test Case 7
        ("01000011010011110100110101010000001100010011100000110001001110010010000101000001", 1234567890123456789, "11: 2, 3, 5, 11, 43, 173, 683, 2731, 10923, 43691, 174763"),  # Test Case 8
        ("0100001101001111010011010101000000110001001110000011000100111001001000010100000101000100", 1234567890123456789, "12: 2, 3, 5, 11, 43, 173, ..., 43691, 174763, 699051"),  # Test Case 9
        ("010000110100111101001101010100000011000100111000001100010011100100100001010000010100010001010011", 12345678901234567890, "13: 2, 3, 5, 11, 43, 173, ..., 174763, 699051, 2796203"),  # Test Case 10
    ]

    print("\n===== Running Test Cases =====\n")

    for idx, (binary_str, n, expected) in enumerate(test_cases, 1):
        print(f"Test Case {idx}:")
        print(f"🔹 Input: binary_str = '{binary_str}', n = {n}")

        start_time = time.time()
        result = find_prime_numbers.format_output(binary_str, n)
        end_time = time.time()
        elapsed_time = end_time - start_time

        if result == expected:
            print(f"✅ PASS (Time: {elapsed_time:.6f} seconds)")
        else:
            print(f"❌ FAIL")
            print(f"   🔹 Expected: {expected}")
            print(f"   🔹 Got:      {result}")
            print(f"   🔹 Time:     {elapsed_time:.6f} seconds\n")

        print("-" * 60)

    print("\n===== Testing Complete =====")

if __name__ == "__main__":
    #run_test_cases0()
    run_test_cases1()
