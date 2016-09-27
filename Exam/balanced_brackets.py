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
# 100/100
user_input = input()
invalidBracketOrder = False
opening_brackets, closing_brackets = 0, 0

for char in user_input:
    if char in "()":
        if char == "(" and opening_brackets >= closing_brackets:
            opening_brackets += 1
        elif char == ")" and opening_brackets > closing_brackets:
            closing_brackets += 1
        else:
            invalidBracketOrder = True
            break

if opening_brackets != closing_brackets or invalidBracketOrder:
    print("WRONG {}".format(len(user_input)))
elif len(user_input) < 2:  # if we have less than two characters, we literally cannot have valid parenthesis
    # the problem's definition of invalid input is really vague, this works fortunately
    # I personally would define invalid input as input without any parenthesis inside
    print("INVALID INPUT")
else:
    print("OK {}".format(opening_brackets))