"""
Grocery assistant.
Note, it may be only 0-30 apples.
If other quantity is required, the answer is "Столько нет"
"""
from termcolor import colored


def main():
    """Add "яблоко" word."""
    n = int(input("Сколько яблок Вам нужно?\n"))
    if n == 0 or (n >= 5 and n <= 20) or (n >= 25 and n <= 30):
        print("Пожалуйста,", n, "яблок")
    elif (n >= 2 and n <= 4) or (n >= 22 and n <= 24):
        print("Пожалуйста,", n, "яблока")
    elif n == 1 or n == 21:
        print("Пожалуйста,", n, "яблоко")
    else:
        print("Столько нет")


if __name__ == "__main__":
    print(colored("Grocery assistant", "red"))  # color this caption
    main()
