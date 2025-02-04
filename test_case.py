import find_prime_numbers  # Ensure both files are in the same folder
import time

def run_tests():
    test_cases = [
        ("0100001101001111", 999999),
        ("01000011010011110100110101010000", 999999),
        ("1111111111111111111111111111111111111111", 999999),
        ("010000110100111101001101010100000011000100111000", 999999999),
        ("01000011010011110100110101010000001100010011100000110001", 123456789012),
        ("0100001101001111010011010101000000110001001110000011000100111001", 123456789012345),
    ]

    for i, (binary_str, n) in enumerate(test_cases, 1):
        start_time = time.time()
        primes = find_prime_numbers.find_primes(binary_str, n)
        result = find_prime_numbers.format_output(sorted(primes))  # Sort to maintain order
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Test {i}: {result} (Time: {elapsed_time:.6f} seconds)")

if __name__ == "__main__":
    run_tests()



