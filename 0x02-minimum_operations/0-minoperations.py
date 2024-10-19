#!/usr/bin/python3
"""
0-minoperations.py
This module contains the minOperations function that calculates the minimum
number of operations required to reach exactly n 'H' characters using only
Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n 'H' characters in the file.

    Args:
        n (int): Target number of H characters.

    Returns:
        int: The minimum number of operations required to reach n H characters.
             Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0  # Impossible to achieve less than 1 'H'

    operations = 0
    factor = 2  # Start with the smallest prime factor

    while n > 1:
        # Check if n is divisible by the current factor
        while n % factor == 0:
            operations += factor  # Add the factor to operations
            n //= factor  # Reduce n by dividing it by the factor
        factor += 1  # Move to the next factor

    return operations
