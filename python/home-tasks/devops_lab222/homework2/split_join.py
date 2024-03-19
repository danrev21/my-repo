def main():
    """Split revert join sentence"""
    inputString = str(input())
    splitedString = inputString.split(" ")
    reversedString = []
    for i in splitedString:
        reversedString += [i[::-1]]
    print(" ".join(map(str, reversedString)))


if __name__ == "__main__":
    main()
