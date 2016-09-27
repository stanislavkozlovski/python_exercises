"""
You are playing a coin-flipping game with your friend.

The rules are:

You toss a coin n times, writing down the results. H for heads and T for tails.
After n tosses, the winner is the one who has the longest consecutive win-streak.
Write a program that reads from the standard input one line - a comma-separated string of H and T and outputs:

H wins! if H wins according to the game rules.
T wins! if T wins according to the game rules.
Draw! if there is no winner.
Examples:

Input: H, H, H, H, T, T, T
Output: H wins!
Input: H, H, H, H, T, T, T, T
Output: Draw!
Input: H, T, H, T, T, H, T
Output: T wins!
Input: T, T, T, H, T, T, T, H, T, T, T, H, H, H, H
Output: H wins!

Solution:
Iterate through the array once and count the consecutive coins. After done counting, compare them and output
the appropriate winner or draw
"""

coinTosses = input().split(', ')

maxHeads, maxTails = 0, 0
currHeads, currTails = 0, 0
lastWasTails = False

for coin in coinTosses:
    if coin == 'H':
        if lastWasTails:
            # we're ending a tails streak, so we reset the curr variable
            currTails = 0
            lastWasTails = False

        currHeads += 1

    if coin == 'T':
        if not lastWasTails:
            # we're ending a heads streak, so we reset the curr variable
            currHeads = 0
            lastWasTails = True

        currTails += 1

    if currTails > maxTails:
        maxTails = currTails
    if currHeads > maxHeads:
        maxHeads = currHeads

if maxHeads == maxTails:
    print("Draw!")
else:
    print("H wins!") if maxHeads > maxTails else print("T wins!")