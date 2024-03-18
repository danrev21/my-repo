"""
Calculate n!. n! = 1 * 2 * 3 * … * (n-1) * n,  0! = 1. n >= 0.
"""


def main():
    """Factorial calculation."""
    n = int(input())
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)


if __name__ == "__main__":
    main()
