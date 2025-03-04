def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):  # Checking divisibility from 2 to num-1
        if num % i == 0:
            return False
    return True  # If no divisor found, the number is prime

# Test cases
print(is_prime(73))  # True