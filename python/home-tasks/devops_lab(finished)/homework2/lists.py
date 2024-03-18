"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of followed by lines of commands
where each command will be of the  types listed above. Iterate through each command
in order and perform the corresponding operation on your list.
The first line contains an integer, denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.
"""


def main():
    """Perform list commands."""
    n = int(input())
    mylist = []
    while n > 0:
        command = list(input().split())
        if command[0] == 'print':
            print(mylist)
        elif command[0] == 'sort':
            mylist.sort()
        elif command[0] == 'remove':
            mylist.remove(int(command[1]))
        elif command[0] == 'append':
            mylist.append(int(command[1]))
        elif command[0] == 'insert':
            mylist.insert(int(command[1]), int(command[2]))
        elif command[0] == 'reverse':
            mylist.reverse()
        elif command[0] == 'pop':
            mylist.pop()
        n -= 1


if __name__ == "__main__":
    main()
