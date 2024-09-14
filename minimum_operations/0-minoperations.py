#!/usr/bin/python3
"""
This module contains a function `minOperations(n)` that calculates
the fewest number of operations needed to achieve exactly `n` 'H'
characters in a text file. The allowed operations are:
    - Copy All
    - Paste
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to result in exactly
    `n` 'H' characters in the file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The fewest number of operations needed to reach `n` 'H' characters.
             If `n` is impossible to achieve, returns 0.

    Example:
        For n = 9, the function would return 6 since it requires 6 operations
        (Copy All and Paste multiple times).
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations


if __name__ == "__main__":
    # Test the minOperations function with example values
    n = 4
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")

    n = 12
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")
