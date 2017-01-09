#  https://www.hackerrank.com/challenges/camelcase
string = input()
upper_case_words = 1
for char in string:
    if char.isupper():
        upper_case_words += 1
print(upper_case_words)
