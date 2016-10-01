"""
Check out the resources on the page's right side to learn more about tries. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.

find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.

Input Format
The first line contains a single integer,n , denoting the number of operations to perform.
Each line  of the  subsequent lines contains an operation in one of the two forms defined above.

Constraints
1 <= n <= 10^5
1 <= |name| <= 21
1 <= |partial| <= 21

It is guaranteed that name and partial contain lowercase English letters only.

Output Format
For each [find partial] operation, print the number of contact names starting with partial on a new line.

Sample Input

4
add hack
add hackerrank
find hac
find hak

Sample Output
2
0

Explanation
We perform the following sequence of operations:

Add a contact named hack.
Add a contact named hackerrank.
Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print 2 on a new line.
Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print 0 on a new line.
"""
# Solution: use a Dictionary with {'h': [words starting with h], 'k': [words starting with k]} for faster searching
# and another Dictionary with {'ha': [words starting with ha]} for the bigger inputs.
operations_count = int(input().strip())
contacts = {}  # key -> one or two letters, value -> list of all contact names starting with that letter ex: 'h':['helen','hell']

for _ in range(operations_count):
    # read input
    operation, name = input().strip().split(' ')

    # create lists in the dictionary if such do not exist yet
    first_letter = name[0]
    if first_letter not in contacts.keys():
        contacts[first_letter] = []

    first_two_letters =  None
    if len(name) > 1:
        first_two_letters = name[:2]
        if first_two_letters not in contacts.keys():
            contacts[first_two_letters] = []


    if operation == 'add':
        # add the name to the corresponding dictionary keys
        contacts[first_letter].append(name)
        if first_two_letters:
            contacts[first_two_letters].append(name)
    elif operation == 'find':
        # find all the names starting with the given name, while prefering to use the lists starting with
        # two letters for better efficiency
        if first_two_letters:
            print(len(list(filter(lambda x: x.startswith(name), contacts[first_two_letters]))))
        else:
            print(len(list(filter(lambda x: x.startswith(name), contacts[first_letter]))))
