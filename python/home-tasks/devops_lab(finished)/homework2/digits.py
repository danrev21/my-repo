"""
Find sum of n-integer digits. n >= 0.
"""


def main():
    """Sum of number digits."""
    n = int(input())
    sum = 0
    for digit in str(n):
        sum = sum + int(digit)
    print(sum)


if __name__ == "__main__":
    main()
