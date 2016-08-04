"""
Write a program that will help you play poker by telling you what kind of hand you have.
input
The first line of input contains the number of test cases (no more than 20).
Each test case consists of one line - five space separated cards. Each card is represented by a two-letter (or digit) word.
The first character is the rank (A,K,Q,J,T,9,8,7,6,5,4,3 or 2),
the second character is the suit (S,H,D,C standing for spades, hearts, diamonds and clubs).
The cards can be in any order (but they will not repeat).
Output
For each test case output one line describing the type of a hand, exactly like in the list above.
"""

"""
Sample input:
2
3S AH KH QC QD
AS KS 3S 4D TD

Sample input 2:
8
3S AH KH QC QD
AS KS 3S 4D TD
KS KH KD KC QC
JH 9C 7C AS AH
2H 2S 2D 5C AC
KS TD TC 8C 5S
7D 7S 4S QH TD
5S AS QH KH TC
"""

# use hardcoded dictionaries to return the proper strings according to rank and suit
rank_strings = {
    'A': 'Ace', 'K': 'King', 'Q':'Queen', 'J':'Jack', 'T': 'Ten', '9':'Nine', '8':'Eight', '7':'Seven', '6':'Six',
    '5':'Five', '4':'Four', '3':'Three', '2':'Two'
}
suit_strings = {'S':' of Spades', 'H':' of Hearts', 'D':' of Diamonds', 'C':' of Clubs'}

test_cases_count = int(input("Number of test cases: "))

for hand_number in range(0, test_cases_count):
    print("Hand #{0} is: ".format(hand_number + 1), end='')
    user_input = input()
    hand = user_input.split()

    """ Explanation:
    1. Use a nested list comprehension to convert the hand list of strings to one containing tuples ["A5"] -> [('A', '5')]
    2. Unpack each tuple in another list comprehension and concatenate a proper string for each card in the hand
    3. Print the Hand
    """
    hand_string = ["{}".format(rank_strings[rank] + suit_strings[suit]) for rank, suit in [tuple(card) for card in hand]]

    print(', '.join(hand_string))

    # a one-liner:
    # print("Hand #{0} is: {1}".format(hand_number + 1,
    #                                  ', '.join(["{}".format(rank_strings[rank] + suit_strings[suit])
    #                                             for rank, suit in [tuple(card) for card in input().split()]])))
    # I would love to use this but it is not readable :(
