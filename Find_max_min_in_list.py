"""
Find_max_min_in_list.py
This script finds the maximum and minimum numbers in a list provided by the user.
Beginner-friendly and self-contained.

Example:
Input: 3 5 1 9 2
Output: Maximum: 9
        Minimum: 1
"""

# Take input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Find maximum and minimum
max_num = max(numbers)
min_num = min(numbers)

# Print results
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
