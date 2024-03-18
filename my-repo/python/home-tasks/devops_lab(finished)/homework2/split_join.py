def main():
    n = str(input("Input string\n"))
    splited = n.split(" ")

    result = []

    for i in splited:
        result.append(i[::-1])

    print(" ".join(result))


if __name__ == "__main__":
    main()
