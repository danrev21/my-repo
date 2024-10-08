"""
Find common items in 2 lists without duplicates. Sort the result list before output.
"""


def main():
    """Find common numbers."""
    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))
    li3 = set(li1) & set(li2)
    print(list(li3))


if __name__ == "__main__":
    main()
