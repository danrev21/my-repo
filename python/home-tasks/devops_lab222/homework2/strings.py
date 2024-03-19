"""
Check whether the input string is palindrome.
"""


def main():
    """Check palindrome."""
    s = str(input())
    rev = ''.join(reversed(s))
    if s == rev:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
