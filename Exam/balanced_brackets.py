"""
Given a string, check if the brackets used are valid (each opening one has a closing one after it)
nested brackets are allowed

sample input:
а * (1 + (b + c) / (c - b)) = 0
sample output where 3 is the number of brackets:
OK 3

sample input 2:
Здравей :о)
sample output 2 where 11 is the length of the string:
WRONG 11
"""

def wrong(user_input: str):
    print("WRONG {}".format(len(user_input)))
    exit()

user_input = input()

opening_brackets, closing_brackets = 0, 0

for char in user_input:
    if char in "()":
        if char == "(" and opening_brackets >= closing_brackets:
            opening_brackets += 1
        elif char == ")" and opening_brackets > closing_brackets:
            closing_brackets += 1
        else:
            wrong(user_input)

if opening_brackets != closing_brackets:
    wrong(user_input)

print("OK {}".format(opening_brackets))