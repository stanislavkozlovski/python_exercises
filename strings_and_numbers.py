"""
Strings and Numbers

You are given a string s that consists of characters, that encode digits & characters that encode nothing. Your goal is to return the sum of all numbers in that string.

Number encoding

In our string s, the digits from 0 to 9 are encoded as follows:

9 is encoded with the most repeated character in s.
8 is encoded with the most repeated character in s, that comes after the one that encodes 9.
...
0 is encoded with the most repeated character in s, that comes after the one that encodes 1.
For example, if 9 is encoded with a, which is repeated 16 times in s, 8 can be encoded with x, which is repeated 15 times in s.

Input details

You read one line from the standard input - the encoded string.
You are guaranteed that there won't be two digits encoded with the same number of repeating characters.
There will always be encoding for all digits between 0 and 9.
Not all digits from 0 to 9 can be encoded. We can have shorter strings that encode small number of digits.
There will always be enough characters to encode digits from 0 to 9.
Input set is "abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~"
If after decoding there are numbers with leading zeroes, ignore them.
Results can get very large. Tackle it with big integers.
Output should be the sum of all numbers in the string.

https://github.com/HackBulgaria/ApplicationFall2016/tree/master/3-Strings-and-Numbers
"""
from collections import Counter
import re

def main():
    sum = 0
    encoded_string = input()
    decoded_string = decode_str(encoded_string)

    # use regex to find the numbers in the string, iterate through them and add them to the sum
    for num in re.findall(r'\d+', decoded_string):
        sum += int(num)

    print(sum)


def decode_str(encoded_string: str):
    """
    This function gets the 10 most repeated characters in the encoded string and replaces them with
    numbers. (most repeated char will be 9, the one after him will be 8... so and so until we get to 0)
    """
    most_common = Counter(encoded_string).most_common(10)  # get a sorted list of tuples

    for i in range(0,10):
        encoded_string = encoded_string.replace(most_common[i][0], str(9-i))

    return encoded_string

if __name__ == "__main__":
    main()