"""
This is a program which helps you decide. How it works is you input two options on which you can't decide upon and the
program tells you which one to pick :)
"""
import random

option_a = input()
option_b = input()
decider = round(random.random(), 1)

if decider != 0.5:
    print("The correct choice is {}".format(option_a if decider > 0.5 else option_b))
else:
    print("There is no correct choice. You're left with two options now, maybe enter them in this program again.")
    print("Option A: Do both of your original options.")
    print("Kill yourself because there is no answer.")