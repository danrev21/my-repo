"""
 Drop empty items from a dictionary.
"""
import json


def main():
    """Drop empty items from a dictionary."""
    d = json.loads(input("Input JSON\n"))
    drop = []
    for key, value in d.items():
        if value is None:
            drop.append(key)
    for i in drop:
        del d[i]
    print(d)


if __name__ == "__main__":
    main()
