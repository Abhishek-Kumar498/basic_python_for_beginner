"""
Prime_number_check.py
This script checks whether a given number is prime or not.
Beginner-friendly and self-contained.

Example:
Input: 17
Output: 17 is a prime number.

Input: 20
Output: 20 is not a prime number.
"""

# Take input from user
num = int(input("Enter a number to check if it's prime: "))

# Prime check logic
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
