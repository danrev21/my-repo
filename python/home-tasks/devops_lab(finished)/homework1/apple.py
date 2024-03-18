"""
Grocery assistant.
Note, it may be only 0-30 apples.
If other quantity is required, the answer is "Столько нет"
"""
from termcolor import colored


def main():
    """Add "яблоко" word."""
    n = int(input("Сколько яблок Вам нужно?\n"))
    if n == 0:
        print("Пожалуйста,", n, "яблок")
    elif n == 1:
        print("Пожалуйста,", n, "яблоко")
    elif n >= 2 and n <= 4:
        print("Пожалуйста,", n, "яблока")
    elif n >= 5 and n <= 20:
        print("Пожалуйста,", n, "яблок")
    elif n == 21:
        print("Пожалуйста,", n, "яблоко")
    elif n >= 22 and n <= 24:
        print("Пожалуйста,", n, "яблока")
    elif n >= 25 and n <= 30:
        print("Пожалуйста,", n, "яблок")
    else:
        print("Столько нет")


if __name__ == "__main__":
    print(colored("Grocery assistant", "magenta"))  # color this caption
    main()
