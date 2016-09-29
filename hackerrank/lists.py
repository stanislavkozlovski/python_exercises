"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.
"""


def main():
    myList = []
    commandsCount = int(input())

    for i in range(0, commandsCount):
        command = input()
        if command[:6] == 'insert':
            insertCommand(command, myList)
        elif command[:6] == 'remove':
            removeCommand(command, myList)
        elif command[:6] == 'append':
            appendCommand(command, myList)
        elif command == 'sort':
            myList.sort()
        elif command == 'pop':
            myList.pop()
        elif command == 'reverse':
            myList.reverse()
        elif command == 'print':
            print(myList)


def insertCommand(command: str, lst: list):
    """
    command example: insert 0 5
    extract the numbers and call the function insert onto the list
    """
    index, value = [int(n) for n in command.split(' ')[1:]]
    lst.insert(index, value)


def removeCommand(command: str, lst: list):
    """
    command example: remove 6
    extract the numbers and call the function remove onto the list
    """
    value = int(command.split(' ')[-1])
    lst.remove(value)


def appendCommand(command: str, lst: list):
    """
    command example: append 9
    extract the number and call the function append onto the list
    """
    value = int(command.split(' ')[-1])
    lst.append(value)


if __name__ == '__main__':
    main()